"""Monatsbericht v2 (Lab 6.2): Lieferungen prüfen, Kennzahlen, Segmente, Auffälligkeiten, Prognose.

Liest alle passenden CSV-Dateien aus einem Datenordner, prüft jede Datei, bereinigt
die Daten und erzeugt einen HTML-Bericht (auf Wunsch zusätzlich eine Excel-Datei).
Das Skript rechnet; jede Ausgabe endet mit zwei festen Prüfzeilen
(Summenkontrolle und Sollwert-Prüfung).

Aufruf im Kursordner (Beispiele):
  python monatsbericht.py --help
  python monatsbericht.py bericht --daten data --monat 2026-09
  python monatsbericht.py bericht --daten data --monat 2026-09 --excel
  python monatsbericht.py auffaelligkeiten --daten data --monat 2026-09 --schwelle 2
  python monatsbericht.py prognose --daten data --monat 2026-09

Exit-Code 0 = fertig, 2 = STOPP (Lieferung nicht verwendbar, kein Bericht).
"""

import argparse
import glob
import os
import sys

import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ===== 1. EINSTELLUNGEN – für einen anderen Datensatz nur diesen Block anpassen ===================
DATEN_STANDARD = "data"                   # Ordner mit den Lieferungen (relativ zum Kursordner)
MUSTER_STANDARD = "nordwind_umsatz*.csv"  # welche Dateien im Ordner gelesen werden
AUSGABE_STANDARD = "berichte"             # hier landen HTML und Excel

LESE_OPTIONEN = {
    "trennzeichen": "auto",               # "auto" erkennt "," oder ";"
    "dezimalzeichen": "auto",             # "auto" erkennt 12.50 und 12,50
    "zeichensatz": "auto",                # "auto" versucht utf-8, dann cp1252 (Excel-Export)
    "datumsformate": ["%d.%m.%Y", "%Y-%m-%d"],  # zuerst TT.MM.JJJJ, dann ISO
}

# Spaltenrollen: Rolle -> Spaltenname in der Datei (None = Spalte gibt es nicht)
SPALTEN = {
    "datum": "datum",       # Pflicht
    "betrag": "umsatz",     # Pflicht
    "gruppe": "region",     # optional: Kennzahlen und Auffälligkeiten je Gruppe
    "kunde": "kunde_id",    # optional: Kundensegmente
    "kosten": "kosten",     # optional: Deckungsbeitrag und Marge
}
PFLICHT = ["datum", "betrag"]
ANZEIGENAMEN = {"betrag": "Umsatz", "gruppe": "Region", "kunde": "Kunde", "kosten": "Kosten"}

GRUPPE_VORSILBEN = ["Region "]            # werden vorne entfernt ("Region Nord" -> "Nord")
GRUPPE_ERSETZEN = {"Sued": "Süd"}         # Schreibweise alt -> neu

SOLLWERT_DATEI = "kontrollsummen.csv"     # im Datenordner; fehlt sie, wird die Prüfung übersprungen
PLAN_DATEI = "nordwind_plan_2026.csv"     # im Datenordner; fehlt sie, entfällt die Plan-Spalte
PLAN_SPALTE = "plan_umsatz"

MAX_FEHLERANTEIL = 0.01                   # mehr als 1 % unlesbare Datums- oder Betragswerte = STOPP
ANZAHL_SEGMENTE = 4                       # Kundensegmente (Lab 5.2)
SCHWELLE_STANDARD = 3                     # Auffälligkeiten: Abstand in Standardabweichungen (Lab 5.3)
PROGNOSE_MONATE = 3                       # Prognose: so viele Monate nach dem Berichtsmonat (Lab 6.1)
MIN_MONATE_PROGNOSE = 24                  # weniger Historie = Prognose wird übersprungen

# ===== 2. HILFSFUNKTIONEN =========================================================================
def stopp(meldung):
    """Bricht mit klarer Meldung und Exit-Code 2 ab (kein Bericht)."""
    print(f"STOPP: {meldung}")
    sys.exit(2)

def zahl(wert, stellen=0):
    """Deutsche Zahlenschreibweise: 343382.31 -> '343.382,31'."""
    if pd.isna(wert):
        return "–"
    text = f"{wert:,.{stellen}f}"
    return text.replace(",", "X").replace(".", ",").replace("X", ".")

def name(rolle):
    """Anzeigename einer Rolle, z. B. betrag -> 'Umsatz'."""
    return ANZEIGENAMEN.get(rolle, rolle)

def monat_plus(monat, schritte):
    """'2026-09' plus 1 -> '2026-10'; minus 12 -> '2025-09'."""
    return (pd.Period(monat, freq="M") + schritte).strftime("%Y-%m")

# ===== 3. LESEN UND QUALITÄTSCHECK ================================================================
def datei_lesen(pfad):
    """Liest eine CSV-Datei als Text; erkennt Zeichensatz und Trennzeichen."""
    zeichensaetze = ["utf-8-sig", "cp1252"] if LESE_OPTIONEN["zeichensatz"] == "auto" else [LESE_OPTIONEN["zeichensatz"]]
    for zeichensatz in zeichensaetze:
        try:
            with open(pfad, encoding=zeichensatz) as datei:
                kopfzeile = datei.read().split("\n")[0]
            break
        except UnicodeDecodeError:
            continue
    else:
        stopp(f"Zeichensatz von {os.path.basename(pfad)} nicht lesbar")
    trennzeichen = LESE_OPTIONEN["trennzeichen"]
    if trennzeichen == "auto":
        trennzeichen = ";" if kopfzeile.count(";") > kopfzeile.count(",") else ","
    return pd.read_csv(pfad, sep=trennzeichen, encoding=zeichensatz, dtype=str)

def zahlen_lesen(werte):
    """Text -> Zahl; versteht 1234.5 und 1.234,5 (Dezimalkomma)."""
    werte = werte.str.strip()
    komma = LESE_OPTIONEN["dezimalzeichen"] == ","
    if LESE_OPTIONEN["dezimalzeichen"] == "auto":
        komma = werte.str.contains(",", regex=False).any()
    if komma:
        werte = werte.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    return pd.to_numeric(werte, errors="coerce")

def datum_lesen(werte):
    """Jeder Wert wird nacheinander mit den Datumsformaten aus den Einstellungen versucht."""
    ergebnis = pd.Series(pd.NaT, index=werte.index, dtype="datetime64[ns]")
    for datumsformat in LESE_OPTIONEN["datumsformate"]:
        ergebnis = ergebnis.fillna(pd.to_datetime(werte.str.strip(), format=datumsformat, errors="coerce"))
    return ergebnis

def daten_laden(ordner, muster):
    """Liest alle passenden Dateien, prüft die Pflichtspalten je Datei und führt sie zusammen."""
    dateien = sorted(glob.glob(os.path.join(ordner, muster)))
    if not dateien:
        stopp(f"keine Datei {muster} im Ordner {ordner}/ gefunden")
    teile, protokoll = [], []
    for pfad in dateien:
        df = datei_lesen(pfad)
        for rolle in PFLICHT:                       # Prüfung VOR dem Zusammenführen
            if SPALTEN[rolle] not in df.columns:
                stopp(f"Pflichtspalte {SPALTEN[rolle]} fehlt in {os.path.basename(pfad)}")
        protokoll.append(f"{os.path.basename(pfad)}: {zahl(len(df))} Zeilen gelesen")
        teile.append(df)
    return pd.concat(teile, ignore_index=True), protokoll

def bereinigen(roh):
    """Dubletten, Schreibweisen, Datum und Zahlen; danach heißen die Spalten wie ihre Rollen."""
    hinweise = []
    df = roh.drop_duplicates()
    hinweise.append(f"Dubletten entfernt: {zahl(len(roh) - len(df))}")

    rollen = {SPALTEN[r]: r for r in SPALTEN if SPALTEN[r] and SPALTEN[r] in df.columns}
    df = df[list(rollen)].rename(columns=rollen)     # z. B. umsatz -> betrag

    df["datum"] = datum_lesen(df["datum"])
    df["betrag"] = zahlen_lesen(df["betrag"])
    for rolle in PFLICHT:                            # Qualitätscheck als Sperre
        anteil = df[rolle].isna().mean()
        if anteil > MAX_FEHLERANTEIL:
            stopp(f"{anteil:.1%} der Werte in Spalte {SPALTEN[rolle]} nicht lesbar (erlaubt: höchstens 1 %)")
        if anteil > 0:
            hinweise.append(f"Zeilen mit unlesbarem Wert in {SPALTEN[rolle]} entfernt: {zahl(df[rolle].isna().sum())}")
        df = df[df[rolle].notna()].copy()

    if "kosten" in df:
        df["kosten"] = zahlen_lesen(df["kosten"])
        hinweise.append(f"Zeilen ohne {name('kosten')} (zählen für {name('betrag')}, nicht für den Deckungsbeitrag): "
                        f"{zahl(df['kosten'].isna().sum())}")
    else:
        hinweise.append("Deckungsbeitrag und Marge übersprungen: keine Spalte für die Rolle kosten")
    if "gruppe" in df:
        vorher = df["gruppe"].nunique()
        gruppe = df["gruppe"].str.strip()
        for vorsilbe in GRUPPE_VORSILBEN:
            gruppe = gruppe.str.removeprefix(vorsilbe).str.strip()
        gruppe = gruppe.replace(GRUPPE_ERSETZEN)
        # gleiche Gruppe in anderer Groß-/Kleinschreibung -> häufigste Schreibweise
        haeufigste = gruppe.groupby(gruppe.str.lower()).agg(lambda s: s.value_counts().index[0])
        df["gruppe"] = gruppe.str.lower().map(haeufigste)
        hinweise.append(f"Schreibweisen {name('gruppe')}: {vorher} -> {df['gruppe'].nunique()}")
    else:
        df["gruppe"] = "Gesamt"                      # ohne Gruppe: eine einzige Zeile je Monat
    df["monat"] = df["datum"].dt.strftime("%Y-%m")
    hinweise.append(f"Zeilen nach Bereinigung: {zahl(len(df))}, Monate {df['monat'].min()} bis {df['monat'].max()}")
    return df, hinweise

# ===== 4. KENNZAHLEN: Ist, Vormonat, Vorjahr, Plan ================================================
def summen(df):
    """Betrag (und Deckungsbeitrag, falls Kosten vorhanden) je Monat und Gruppe."""
    df = df.copy()
    spalten = ["betrag"]
    if "kosten" in df:
        df["deckungsbeitrag"] = df["betrag"] - df["kosten"]   # leer, wenn Kosten fehlen
        spalten.append("deckungsbeitrag")
    return df.groupby(["monat", "gruppe"])[spalten].sum()

def plan_lesen(ordner, monat):
    """Planwerte je Gruppe für den Monat oder None, wenn es keine Plan-Datei gibt."""
    pfad = os.path.join(ordner, PLAN_DATEI)
    if not os.path.exists(pfad) or not SPALTEN["gruppe"]:
        return None
    plan = pd.read_csv(pfad, dtype={"monat": str})
    plan = plan[plan["monat"] == monat]
    return plan.set_index(SPALTEN["gruppe"])[PLAN_SPALTE] if len(plan) else None

def kpi_tabelle(df, monat, plan):
    """Eine Zeile je Gruppe plus Gesamt; Abweichungen in Prozent."""
    s = summen(df)
    je_monat = s["betrag"].unstack("monat")          # Zeilen = Gruppen, Spalten = Monate
    kpi = pd.DataFrame({"betrag": je_monat[monat]}).dropna()
    for spalte, vergleich in [("vormonat", monat_plus(monat, -1)), ("vorjahr", monat_plus(monat, -12))]:
        if vergleich in je_monat:
            kpi[spalte] = je_monat[vergleich]
    if plan is not None:
        kpi["plan"] = plan
    if "deckungsbeitrag" in s:
        kpi["deckungsbeitrag"] = s["deckungsbeitrag"].unstack("monat")[monat]
    if len(kpi) > 1:
        kpi.loc["Gesamt"] = kpi.sum()                # Summen, nie Prozentwerte addieren
    for spalte in ["vormonat", "vorjahr", "plan"]:
        if spalte in kpi:
            kpi[spalte + "_proz"] = (kpi["betrag"] / kpi[spalte] - 1) * 100
    if "deckungsbeitrag" in kpi:
        kpi["marge_proz"] = kpi["deckungsbeitrag"] / kpi["betrag"] * 100   # Marge aus Summen
    reihenfolge = ["betrag", "vormonat", "vormonat_proz", "vorjahr", "vorjahr_proz",
                   "plan", "plan_proz", "deckungsbeitrag", "marge_proz"]
    return kpi[[s for s in reihenfolge if s in kpi]]

def kpi_anzeigen(kpi):
    """Spaltennamen für Menschen; Beträge auf 2, Prozente auf 1 Stelle gerundet."""
    namen = {"betrag": name("betrag"), "vormonat": "Vormonat", "vormonat_proz": "Δ Vormonat %",
             "vorjahr": "Vorjahr", "vorjahr_proz": "Δ Vorjahr %", "plan": "Plan", "plan_proz": "Δ Plan %",
             "deckungsbeitrag": "Deckungsbeitrag", "marge_proz": "Marge %"}
    tabelle = kpi.copy()
    for spalte in tabelle:
        tabelle[spalte] = tabelle[spalte].round(1 if spalte.endswith("_proz") else 2)
    tabelle.index.name = name("gruppe")
    return tabelle.rename(columns=namen)

# ===== 5. ML-BAUSTEINE: Segmente (Lab 5.2), Auffälligkeiten (Lab 5.3), Prognose (Lab 6.1) =========
def segmente(df, monat):
    """Kunden nach RFM in feste Segmente teilen; 1 = höchster Ø Betrag."""
    stichtag = pd.Period(monat, freq="M").end_time.normalize()
    bis = df[df["datum"] <= stichtag]
    rfm = bis.groupby("kunde").agg(letzter_kauf=("datum", "max"), haeufigkeit=("betrag", "count"),
                                   betrag=("betrag", "sum"))
    rfm["tage_seit_kauf"] = (stichtag - rfm["letzter_kauf"]).dt.days
    merkmale = StandardScaler().fit_transform(rfm[["tage_seit_kauf", "haeufigkeit", "betrag"]])
    rfm["segment"] = KMeans(n_clusters=ANZAHL_SEGMENTE, random_state=42, n_init=10).fit_predict(merkmale)
    reihenfolge = rfm.groupby("segment")["betrag"].mean().sort_values(ascending=False).index
    rfm["segment"] = rfm["segment"].map({alt: neu for neu, alt in enumerate(reihenfolge, start=1)})
    tabelle = rfm.groupby("segment").agg(
        kunden=("betrag", "count"), tage_seit_kauf=("tage_seit_kauf", "mean"),
        haeufigkeit=("haeufigkeit", "mean"), betrag=("betrag", "mean"), betrag_summe=("betrag", "sum"))
    tabelle = tabelle.round(0).rename(columns={
        "kunden": "Kunden", "tage_seit_kauf": "Ø Tage seit Kauf", "haeufigkeit": "Ø Buchungen",
        "betrag": f"Ø {name('betrag')}", "betrag_summe": f"{name('betrag')} gesamt"})
    tabelle.index.name = "Segment"
    return rfm.reset_index(), tabelle

def find_anomalies(df, schwelle=SCHWELLE_STANDARD):
    """Tagessumme je Gruppe; auffällig = mehr als `schwelle` Standardabweichungen vom Monatsmittel."""
    tage = df.groupby(["datum", "gruppe"], as_index=False)["betrag"].sum()
    tage["monat"] = tage["datum"].dt.strftime("%Y-%m")
    je_gruppe_monat = tage.groupby(["gruppe", "monat"])["betrag"]
    tage["mittel"] = je_gruppe_monat.transform("mean")
    tage["streuung"] = je_gruppe_monat.transform("std")
    tage["abstand"] = (tage["betrag"] - tage["mittel"]) / tage["streuung"]
    tage["auffaellig"] = tage["abstand"].abs() > schwelle
    return tage

def auffaellige_tage(tage, monat):
    """Die auffälligen Tage des Monats als Tabelle für Menschen."""
    treffer = tage[tage["auffaellig"] & (tage["monat"] == monat)]
    tabelle = pd.DataFrame({
        "Datum": treffer["datum"].dt.strftime("%d.%m.%Y"), name("gruppe"): treffer["gruppe"],
        name("betrag"): treffer["betrag"].round(2), "Monatsmittel": treffer["mittel"].round(2),
        "Abstand (Std.-Abw.)": treffer["abstand"].round(1)})
    return tabelle.reset_index(drop=True)

def prognose(df, monat):
    """Vorjahresmonat × Trendfaktor (letzte 12 Monate / 12 Monate davor); None, wenn zu wenig Historie."""
    je_monat = df[df["monat"] <= monat].groupby("monat")["betrag"].sum()
    if len(je_monat) < MIN_MONATE_PROGNOSE:
        return je_monat, None, None
    faktor = je_monat.iloc[-12:].sum() / je_monat.iloc[-24:-12].sum()
    zeilen = []
    for schritt in range(1, PROGNOSE_MONATE + 1):
        ziel = monat_plus(monat, schritt)
        vorjahr = je_monat[monat_plus(ziel, -12)]
        zeilen.append({"Monat": ziel, "Vorjahresmonat": round(vorjahr, 2), "Prognose": round(vorjahr * faktor, 2)})
    return je_monat, pd.DataFrame(zeilen), faktor

# ===== 6. PRÜFZEILEN: Summenkontrolle und Sollwert-Prüfung ========================================
def summenkontrolle(df, monat, kpi):
    zeilen = df[df["monat"] == monat]
    summe = zeilen["betrag"].sum()
    passt = abs(summe - kpi["betrag"].iloc[-1]) < 0.01     # letzte Zeile = Gesamt
    return (f"Summenkontrolle: {monat} – {zahl(len(zeilen))} Zeilen, Summe {name('betrag')} {zahl(summe, 2)}"
            f" – {'stimmt mit der Kennzahlentabelle überein' if passt else 'weicht von der Kennzahlentabelle ab'}")

def sollwert_pruefung(df, monat, ordner):
    pfad = os.path.join(ordner, SOLLWERT_DATEI)
    if not os.path.exists(pfad):
        return "Sollwert-Prüfung: keine Sollwert-Datei – übersprungen"
    soll = pd.read_csv(pfad, dtype={"monat": str})
    soll = soll[soll["monat"] == monat].set_index(SPALTEN["gruppe"] or "monat")
    if soll.empty:
        return f"Sollwert-Prüfung: keine Sollwerte für {monat} in {SOLLWERT_DATEI} – übersprungen"
    ist = summen(df[df["monat"] == monat]).loc[monat]
    if "deckungsbeitrag" in ist:
        ist["marge"] = ist["deckungsbeitrag"] / ist["betrag"]
    vergleiche = [("betrag", SPALTEN["betrag"], 0.05), ("deckungsbeitrag", "deckungsbeitrag", 0.05),
                  ("marge", "marge", 0.0001)]
    anzahl, abweichungen = 0, 0
    for spalte_ist, spalte_soll, toleranz in vergleiche:
        if spalte_ist in ist and spalte_soll in soll:
            differenz = (ist[spalte_ist] - soll[spalte_soll]).abs()   # fehlende Gruppe -> leer
            anzahl += len(differenz)
            abweichungen += int((differenz.isna() | (differenz > toleranz)).sum())
    ergebnis = "bestanden" if abweichungen == 0 else f"{abweichungen} Abweichungen"
    return f"Sollwert-Prüfung: {ergebnis} ({anzahl} Werte für {monat} gegen {SOLLWERT_DATEI})"

# ===== 7. AUSGABE: HTML-Bericht und Excel =========================================================
def als_text(tabelle):
    """Zahlen in einer Tabelle deutsch formatieren (Prozentspalten mit Vorzeichen)."""
    tabelle = tabelle.copy()
    for spalte in tabelle.select_dtypes("number"):
        if spalte.startswith("Δ"):                  # Abweichung mit Vorzeichen: +4,7
            tabelle[spalte] = tabelle[spalte].map(lambda x: "–" if pd.isna(x) else f"{x:+.1f}".replace(".", ","))
        else:
            stellen = 1 if "%" in spalte or "Abstand" in spalte else 0
            tabelle[spalte] = tabelle[spalte].map(lambda x: zahl(x, stellen))
    return tabelle.to_html(classes="tabelle", border=0)

def html_bericht(pfad, titel, abschnitte):
    """abschnitte: Liste von (Überschrift, HTML-Inhalt) -> eine HTML-Datei."""
    stil = ("body{font-family:Arial,sans-serif;margin:32px;color:#222;max-width:1100px}"
            ".tabelle{border-collapse:collapse;margin:8px 0}.tabelle td,.tabelle th{padding:4px 10px;"
            "border-bottom:1px solid #ddd;text-align:right}.pruefung{background:#eef6ee;padding:10px 14px;"
            "border-left:4px solid #3a7d44;font-family:monospace}")
    teile = [f"<html><head><meta charset='utf-8'><title>{titel}</title><style>{stil}</style></head><body>",
             f"<h1>{titel}</h1>"]
    teile += [f"<h2>{ueberschrift}</h2>{inhalt}" for ueberschrift, inhalt in abschnitte]
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write("\n".join(teile) + "</body></html>")

def diagramm(fig, erstes):
    """Diagramm als HTML-Baustein; das erste lädt plotly aus dem Netz ("cdn", wie in Lab 3.2)."""
    fig.update_layout(height=420, margin=dict(l=20, r=20, t=60, b=20))
    return fig.to_html(full_html=False, include_plotlyjs="cdn" if erstes else False)

def export_excel(kpi, auffaellige, pfad):
    """Schreibt die Kennzahlentabelle als Blatt "Kennzahlen" in die Excel-Datei pfad.

    kpi: Kennzahlen je Region (Index = Region), auffaellige: auffällige Tage (Erweiterung: zweites Blatt).
    """
    with pd.ExcelWriter(pfad) as writer:
        kpi.to_excel(writer, sheet_name="Kennzahlen")
        auffaellige.to_excel(writer, sheet_name="Auffaelligkeiten", index=False)

def excel_pruefen(pfad, kpi):
    """Eingebaute Prüfung nach export_excel: Datei, Blatt und Zeilenzahl."""
    if not os.path.exists(pfad):
        return f"nicht OK – {pfad} fehlt: Funktion export_excel schreibt noch keine Datei"
    blaetter = pd.read_excel(pfad, sheet_name=None)
    if "Kennzahlen" not in blaetter:
        return f"nicht OK – Blatt 'Kennzahlen' fehlt, gefunden: {', '.join(blaetter)}"
    if len(blaetter["Kennzahlen"]) != len(kpi):
        return f"nicht OK – Blatt 'Kennzahlen' hat {len(blaetter['Kennzahlen'])} statt {len(kpi)} Zeilen"
    return f"OK – {pfad} mit {len(kpi)} Zeilen im Blatt 'Kennzahlen' (Blätter: {', '.join(blaetter)})"

# ===== 8. ABLAUF: Befehle bericht, auffaelligkeiten, prognose =====================================
def befehle():
    gemeinsam = argparse.ArgumentParser(add_help=False)
    gemeinsam.add_argument("--daten", default=DATEN_STANDARD, help=f"Datenordner (Standard: {DATEN_STANDARD})")
    gemeinsam.add_argument("--muster", default=MUSTER_STANDARD, help=f"Dateimuster (Standard: {MUSTER_STANDARD})")
    gemeinsam.add_argument("--monat", help="Berichtsmonat JJJJ-MM (Standard: letzter Monat in den Daten)")
    gemeinsam.add_argument("--schwelle", type=float, default=SCHWELLE_STANDARD,
                           help=f"Auffälligkeiten ab so vielen Standardabweichungen (Standard: {SCHWELLE_STANDARD})")
    gemeinsam.add_argument("--ausgabe", default=AUSGABE_STANDARD, help=f"Ordner für HTML und Excel (Standard: {AUSGABE_STANDARD})")
    parser = argparse.ArgumentParser(prog="monatsbericht.py", description="Monatsbericht v2: Kennzahlen, "
                                     "Segmente, Auffälligkeiten und Prognose aus allen Lieferungen eines Ordners.")
    unter = parser.add_subparsers(dest="befehl", required=True, metavar="{bericht,auffaelligkeiten,prognose}")
    bericht = unter.add_parser("bericht", parents=[gemeinsam], help="HTML-Bericht mit allen Abschnitten")
    bericht.add_argument("--excel", action="store_true", help="zusätzlich kpi_JJJJ_MM.xlsx schreiben")
    unter.add_parser("auffaelligkeiten", parents=[gemeinsam], help="nur die auffälligen Tage des Monats")
    unter.add_parser("prognose", parents=[gemeinsam], help="nur die Prognose der nächsten Monate")
    return parser

def main():
    args = befehle().parse_args()
    roh, protokoll = daten_laden(args.daten, args.muster)
    df, hinweise = bereinigen(roh)
    monat = args.monat or df["monat"].max()
    if monat not in set(df["monat"]):
        stopp(f"keine Daten für den Monat {monat} in {args.daten}/")
    df = df[df["monat"] <= monat]                   # spätere Lieferungen stören den Bericht nicht
    plan = plan_lesen(args.daten, monat)
    if plan is None:
        hinweise.append(f"Plan-Spalte übersprungen: keine Planwerte für {monat} ({PLAN_DATEI})")
    print(f"Monatsbericht {monat} – {name('betrag')} – Daten: {args.daten}/{args.muster}")
    for zeile in protokoll + hinweise:
        print("  " + zeile)

    kpi = kpi_tabelle(df, monat, plan)
    tage = find_anomalies(df, args.schwelle)
    auffaellige = auffaellige_tage(tage, monat)
    pruefzeilen = [summenkontrolle(df, monat, kpi), sollwert_pruefung(df, monat, args.daten)]

    if args.befehl == "auffaelligkeiten":
        print(f"\nAuffällige Tage {monat} (Schwelle {args.schwelle:g}): {len(auffaellige)}")
        print(auffaellige.to_string(index=False) if len(auffaellige) else "  keine")
    if args.befehl == "prognose":
        je_monat, vorschau, faktor = prognose(df, monat)
        if vorschau is None:
            print(f"\nPrognose übersprungen: nur {len(je_monat)} Monate Historie (mindestens {MIN_MONATE_PROGNOSE})")
        else:
            print(f"\nPrognose (Vorjahresmonat × Trendfaktor {zahl(faktor, 3)}):")
            print(vorschau.to_string(index=False))
    if args.befehl == "bericht":
        bericht_schreiben(args, df, monat, kpi, tage, auffaellige, protokoll + hinweise, pruefzeilen)

    print()
    for zeile in pruefzeilen:
        print(zeile)

def bericht_schreiben(args, df, monat, kpi, tage, auffaellige, hinweise, pruefzeilen):
    os.makedirs(args.ausgabe, exist_ok=True)
    tabelle = kpi_anzeigen(kpi)
    print("\n" + tabelle.to_string())
    abschnitte = [("Prüfung", "<p class='pruefung'>" + "<br>".join(pruefzeilen) + "</p>"),
                  ("Qualitätscheck", "<ul>" + "".join(f"<li>{h}</li>" for h in hinweise) + "</ul>")]
    balken = kpi.drop(index="Gesamt", errors="ignore").reset_index()
    balken = balken.rename(columns={"betrag": f"Ist {monat}", "vorjahr": "Vorjahr", "plan": "Plan"})
    werte = [s for s in [f"Ist {monat}", "Vorjahr", "Plan"] if s in balken]
    fig = px.bar(balken, x="gruppe", y=werte, barmode="group",
                 labels={"gruppe": name("gruppe"), "value": name("betrag"), "variable": ""},
                 title=f"{name('betrag')} {monat} je {name('gruppe')}: Ist, Vorjahr, Plan")
    abschnitte.append(("Kennzahlen", als_text(tabelle) + diagramm(fig, True)))

    if "kunde" in df:                               # Abschnitt Segmente (Lab 5.2)
        kunden, seg_tabelle = segmente(df, monat)
        kunden["Segment"] = kunden["segment"].astype(str)
        fig = px.scatter(kunden.sort_values("segment"), x="haeufigkeit", y="betrag", color="Segment",
                         labels={"haeufigkeit": "Buchungen", "betrag": name("betrag")},
                         title=f"{ANZAHL_SEGMENTE} Kundensegmente (Stichtag Ende {monat})")
        abschnitte.append(("Kundensegmente", als_text(seg_tabelle) + diagramm(fig, False)))
        print(f"\nSegmente: {seg_tabelle['Kunden'].astype(int).tolist()} Kunden je Segment 1–{ANZAHL_SEGMENTE}")
    else:
        abschnitte.append(("Kundensegmente", "<p>übersprungen: keine Spalte für die Rolle kunde</p>"))
        print("\nSegmente übersprungen: keine Spalte für die Rolle kunde")

    monatstage = tage[tage["monat"] == monat]       # Abschnitt Auffälligkeiten (Lab 5.3)
    fig = px.line(monatstage, x="datum", y="betrag", color="gruppe", markers=True,
                  labels={"datum": "Tag", "betrag": name("betrag"), "gruppe": name("gruppe")},
                  title=f"{len(auffaellige)} auffällige Tage {monat} (Schwelle {args.schwelle:g})")
    treffer = monatstage[monatstage["auffaellig"]]
    fig.add_scatter(x=treffer["datum"], y=treffer["betrag"], mode="markers", name="auffällig",
                    marker=dict(size=14, color="red", symbol="circle-open", line=dict(width=3)))
    inhalt = als_text(auffaellige.set_index("Datum")) if len(auffaellige) else "<p>keine auffälligen Tage</p>"
    abschnitte.append(("Auffälligkeiten", inhalt + diagramm(fig, False)))
    print(f"Auffällige Tage (Schwelle {args.schwelle:g}): {len(auffaellige)}")

    je_monat, vorschau, faktor = prognose(df, monat)  # Abschnitt Prognose (Lab 6.1)
    if vorschau is None:
        text = f"übersprungen: nur {len(je_monat)} Monate Historie (mindestens {MIN_MONATE_PROGNOSE})"
        abschnitte.append(("Prognose", f"<p>{text}</p>"))
        print("Prognose " + text)
    else:
        verlauf = pd.DataFrame({"Monat": je_monat.index, name("betrag"): je_monat.values, "Art": "Ist"})
        anschluss = verlauf.tail(1).assign(Art="Prognose")      # letzter Ist-Monat verbindet beide Linien
        verlauf = pd.concat([verlauf, anschluss, vorschau.rename(columns={"Prognose": name("betrag")}).assign(Art="Prognose")])
        fig = px.line(verlauf, x="Monat", y=name("betrag"), color="Art", markers=True,
                      title=f"Prognose: Vorjahresmonat × Trendfaktor {zahl(faktor, 3)}")
        abschnitte.append(("Prognose", als_text(vorschau.set_index("Monat")) + diagramm(fig, False)))
        print(f"Prognose {vorschau['Monat'].iloc[0]} bis {vorschau['Monat'].iloc[-1]}: "
              + ", ".join(zahl(x) for x in vorschau["Prognose"]))

    pfad = os.path.join(args.ausgabe, f"bericht_{monat.replace('-', '_')}_v2.html")
    html_bericht(pfad, f"Monatsbericht {monat} – {name('betrag')}", abschnitte)
    print(f"\nBericht: {pfad}")
    if args.excel:
        excel_pfad = os.path.join(args.ausgabe, f"kpi_{monat.replace('-', '_')}.xlsx")
        if os.path.exists(excel_pfad):
            os.remove(excel_pfad)                   # alte Datei weg, damit die Prüfung nur die neue sieht
        export_excel(tabelle, auffaellige, excel_pfad)
        print(excel_pruefen(excel_pfad, tabelle))


if __name__ == "__main__":
    main()
