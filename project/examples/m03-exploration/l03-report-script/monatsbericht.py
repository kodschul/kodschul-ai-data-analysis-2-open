"""Monatsbericht v1 (Lab 3.3): eine Umsatzdatei und ein Monat rein, ein HTML-Bericht raus.

Aufruf im Kursordner:
    python project/examples/m03-exploration/l03-report-script/monatsbericht.py data/nordwind_umsatz.csv --monat 2026-09

Ergebnis in ORDNER:  bericht_2026_09.html (Bericht) und kpi_2026_09.csv (KPI-Tabelle).
Prüfen:              python check_zahlen.py <ORDNER>kpi_2026_09.csv

Die Datei ist eigenständig: Sie enthält die Beispiel-Funktionen aus clean.py (Lab 2.2),
features.py (Lab 2.3), analyse.py (Lab 3.1) und diagramme.py (Lab 3.2).
Gleiche Eingabedatei und gleicher Monat ergeben immer denselben Bericht.
"""

import argparse
import re
import sys

import pandas as pd
import plotly.express as px

ORDNER = "project/examples/m03-exploration/l03-report-script/"   # hier landen Bericht und KPI-Tabelle
PLAN_DATEI = "data/nordwind_plan_2026.csv"
MONATSNAMEN = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
               "August", "September", "Oktober", "November", "Dezember"]


# ---------------------------------------------------------------- Bereinigung (Lab 2.2, clean.py)

def clean_umsatz(df):
    """Bereinigt eine Nordwind-Umsatztabelle. Jede Regel steht als eigener Schritt."""
    df = df.copy()
    df = df.drop_duplicates()                                                  # Dubletten entfernen
    deutsch = pd.to_datetime(df["datum"], format="%d.%m.%Y", errors="coerce")  # Onlineshop: TT.MM.JJJJ
    iso = pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce")      # Außendienst: JJJJ-MM-TT
    df["datum"] = deutsch.fillna(iso)
    df["kosten_fehlt"] = df["kosten"].isna()                                   # markieren, nicht löschen
    df["region"] = (
        df["region"].str.strip().str.replace("Region ", "", regex=False)
        .str.capitalize().replace({"Sued": "Süd"})                             # 4 einheitliche Regionen
    )
    return df


# ---------------------------------------------------------------- Kennzahlen (Lab 2.3, features.py)

def add_features(df):
    """Neue Spalten aus vorhandenen Spalten."""
    df = df.copy()
    df["datum"] = pd.to_datetime(df["datum"])
    df["monat"] = df["datum"].dt.strftime("%Y-%m")
    df["quartal"] = df["datum"].dt.to_period("Q").astype(str)
    df["deckungsbeitrag"] = df["umsatz"] - df["kosten"]        # leer, wenn Kosten fehlen
    df["marge"] = df["deckungsbeitrag"] / df["umsatz"]         # Zeilenmarge, nie aufsummieren
    return df


# ---------------------------------------------------------------- Analyse (Lab 3.1, analyse.py)

def wachstum_je_region(df, bis_monat=9):
    """Umsatz Januar bis bis_monat je Region und Jahr, dazu Veränderung zum Vorjahr in %."""
    zeitraum = df[df["datum"].dt.month <= bis_monat]
    tabelle = zeitraum.pivot_table(index="region", columns="jahr", values="umsatz", aggfunc="sum")
    letztes_jahr = tabelle.columns.max()
    veraenderung = tabelle.pct_change(axis="columns") * 100
    tabelle["wachstum_prozent"] = veraenderung[letztes_jahr]
    tabelle.columns = [str(spalte) for spalte in tabelle.columns]
    return tabelle.round(1).sort_values("wachstum_prozent", ascending=False)


def marge_je_produktgruppe(df):
    """Marge je Produktgruppe = Summe Deckungsbeitrag / Summe Umsatz."""
    summen = df.groupby("produktgruppe")[["umsatz", "deckungsbeitrag"]].sum()
    summen["marge_prozent"] = summen["deckungsbeitrag"] / summen["umsatz"] * 100
    return summen.round(1).sort_values("marge_prozent", ascending=False)


def kanal_je_monat(df):
    """Umsatz je Monat und Kanal, dazu der Anteil des Onlineshops in %."""
    tabelle = df.pivot_table(index="monat", columns="kanal", values="umsatz", aggfunc="sum")
    tabelle["anteil_online_prozent"] = tabelle["Onlineshop"] / (tabelle["Außendienst"] + tabelle["Onlineshop"]) * 100
    tabelle.columns.name = None
    return tabelle.round(1)


# ---------------------------------------------------------------- Diagramme (Lab 3.2, diagramme.py)

def diagramm_kanal(kanal_monat, titel):
    return px.line(kanal_monat, x="monat", y=["Außendienst", "Onlineshop"], title=titel,
                   labels={"monat": "Monat", "value": "Umsatz in €", "variable": "Kanal"})


def diagramm_marge(marge, titel):
    return px.bar(marge, x="produktgruppe", y="marge_prozent", title=titel, text="marge_prozent",
                  labels={"produktgruppe": "Produktgruppe", "marge_prozent": "Marge in %"})


def diagramm_wachstum(wachstum, titel):
    return px.bar(wachstum, x="region", y="wachstum_prozent", title=titel, text="wachstum_prozent",
                  labels={"region": "Region", "wachstum_prozent": "Veränderung zum Vorjahr in %"})


# ---------------------------------------------------------------- KPI-Tabelle (neu in Lab 3.3)

def kpi_tabelle(df, monat, plan):
    """Ist, Vormonat, Vorjahr und Plan je Region für einen Monat (JJJJ-MM)."""
    m = pd.Period(monat, freq="M")                    # Monatsrechnung: 2026-09 minus 1 = 2026-08
    vormonat, vorjahr = str(m - 1), str(m - 12)

    kpi = df[df["monat"] == monat].groupby("region")[["umsatz", "deckungsbeitrag"]].sum()
    kpi["marge"] = kpi["deckungsbeitrag"] / kpi["umsatz"]                       # aus den Summen
    kpi["vormonat"] = df[df["monat"] == vormonat].groupby("region")["umsatz"].sum()
    kpi["vorjahr"] = df[df["monat"] == vorjahr].groupby("region")["umsatz"].sum()
    kpi["plan"] = plan[plan["monat"] == monat].set_index("region")["plan_umsatz"]
    kpi = kpi.reset_index()
    kpi.insert(0, "monat", monat)
    return kpi.round({"umsatz": 2, "deckungsbeitrag": 2, "marge": 4, "vormonat": 2, "vorjahr": 2, "plan": 2})


def mit_gesamt(kpi):
    """Hängt eine Zeile Gesamt an (nur für den Bericht; die Marge wieder aus den Summen)."""
    summe = kpi[["umsatz", "deckungsbeitrag", "vormonat", "vorjahr", "plan"]].sum(min_count=1)
    gesamt = {"monat": kpi["monat"].iloc[0], "region": "Gesamt", **summe.to_dict()}
    gesamt["marge"] = gesamt["deckungsbeitrag"] / gesamt["umsatz"]
    return pd.concat([kpi, pd.DataFrame([gesamt])], ignore_index=True)


# ---------------------------------------------------------------- HTML-Bericht

def euro(wert):
    """12345.6 -> '12.346 €' (deutsches Zahlenformat); fehlender Wert -> '–'."""
    return "–" if pd.isna(wert) else f"{wert:,.0f} €".replace(",", ".")


def prozent(anteil):
    """0.2034 -> '20,3 %'."""
    return "–" if pd.isna(anteil) else f"{anteil * 100:.1f} %".replace(".", ",")


def veraenderung(prozentwert):
    """9.8 -> '+9,8 %'."""
    return f"{prozentwert:+.1f} %".replace(".", ",")


def html_tabelle(kpi):
    kopf = ["Region", "Umsatz", "Deckungsbeitrag", "Marge", "Vormonat", "Vorjahresmonat", "Plan"]
    zeilen = ["<tr>" + "".join(f"<th>{k}</th>" for k in kopf) + "</tr>"]
    for _, z in mit_gesamt(kpi).iterrows():
        klasse = ' class="gesamt"' if z["region"] == "Gesamt" else ""
        zellen = [z["region"], euro(z["umsatz"]), euro(z["deckungsbeitrag"]), prozent(z["marge"]),
                  euro(z["vormonat"]), euro(z["vorjahr"]), euro(z["plan"])]
        zeilen.append(f"<tr{klasse}>" + "".join(f"<td>{c}</td>" for c in zellen) + "</tr>")
    return "<table>\n" + "\n".join(zeilen) + "\n</table>"


def html_bericht(kpi, diagramme, monat, datei, buchungen):
    jahr, nr = monat.split("-")
    titel = f"Monatsbericht {MONATSNAMEN[int(nr) - 1]} {jahr}"
    anzahl = f"{buchungen:,}".replace(",", ".")                 # 1234 -> 1.234
    teile = [fig.to_html(full_html=False, include_plotlyjs="cdn" if i == 0 else False)
             for i, fig in enumerate(diagramme)]
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>{titel} – Nordwind Handel</title>
<style>
  body {{ font-family: Arial, Helvetica, sans-serif; max-width: 1000px; margin: 2rem auto; padding: 0 1rem; color: #222; }}
  h1 {{ margin-bottom: 0.2rem; }}
  .info {{ color: #666; margin-top: 0; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
  th, td {{ padding: 0.45rem 0.7rem; border-bottom: 1px solid #ddd; text-align: right; }}
  th:first-child, td:first-child {{ text-align: left; }}
  th {{ background: #f3f5f8; }}
  tr.gesamt td {{ font-weight: bold; border-top: 2px solid #999; }}
</style>
</head>
<body>
<h1>{titel}</h1>
<p class="info">Nordwind Handel · Datei: {datei} · {anzahl} Buchungen im Monat · erstellt mit monatsbericht.py v1</p>
<h2>Kennzahlen je Region</h2>
{html_tabelle(kpi)}
<p class="info">Marge = Deckungsbeitrag / Umsatz aus den Monatssummen. Buchungen ohne Kosten zählen beim Umsatz, nicht beim Deckungsbeitrag.</p>
<h2>Diagramme</h2>
{"".join(teile)}
</body>
</html>
"""


# ---------------------------------------------------------------- Ablauf

def lies_argumente():
    parser = argparse.ArgumentParser(description="Monatsbericht v1: CSV + Monat -> HTML-Bericht")
    parser.add_argument("datei", help="Umsatzdatei, z. B. data/nordwind_umsatz.csv")
    parser.add_argument("--monat", required=True, help="Berichtsmonat als JJJJ-MM, z. B. 2026-09")
    args = parser.parse_args()
    if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", args.monat):        # vier Ziffern, Bindestrich, Monat 01–12
        parser.error(f"--monat {args.monat}: Format JJJJ-MM erwartet, z. B. 2026-09")
    return args


def stopp(text):
    print(text)
    sys.exit(1)


def pruefe_aufgabe(sauber, df, kpi, monat):
    """Eingebaute Prüfung: meldet OK oder nicht OK mit Hinweis."""
    if not isinstance(sauber, pd.DataFrame) or sauber["region"].nunique() != 4:
        stopp("nicht OK – sauber fehlt oder hat nicht genau 4 Regionen: clean_umsatz(roh) aufrufen.")
    if not isinstance(df, pd.DataFrame) or "deckungsbeitrag" not in df.columns:
        stopp("nicht OK – df fehlt oder hat keine Spalte deckungsbeitrag: add_features(sauber) aufrufen.")
    if not isinstance(kpi, pd.DataFrame) or "vorjahr" not in kpi.columns:
        stopp("nicht OK – kpi fehlt: kpi_tabelle(df, args.monat, plan) aufrufen.")
    summe = df.loc[df["monat"] == monat, "umsatz"].sum()
    if summe == 0:
        stopp(f"nicht OK – keine Buchungen für den Monat {monat} in der Datei.")
    if len(kpi) != 4 or abs(kpi["umsatz"].sum() - summe) > 0.05:
        stopp("nicht OK – die Summe der Regionen in kpi passt nicht zum Monatsumsatz.")
    print(f"OK – 4 Regionen, Summe der Regionen = Umsatz aller Buchungen im Monat ({euro(summe)})")


def main():
    args = lies_argumente()
    roh = pd.read_csv(args.datei)
    plan = pd.read_csv(PLAN_DATEI)

    sauber = clean_umsatz(roh)
    df = add_features(sauber)
    kpi = kpi_tabelle(df, args.monat, plan)
    pruefe_aufgabe(sauber, df, kpi, args.monat)

    # Diagramme bis einschließlich Berichtsmonat; der Titel (Befund) entsteht aus den Zahlen
    bis = df[df["monat"] <= args.monat]
    im_monat = df[df["monat"] == args.monat]
    monatsname = MONATSNAMEN[int(args.monat[5:]) - 1]
    kanal = kanal_je_monat(bis).reset_index()
    marge = marge_je_produktgruppe(im_monat).reset_index()
    wachstum = wachstum_je_region(bis, bis_monat=int(args.monat[5:])).reset_index()
    diagramme = [
        diagramm_kanal(kanal, f"Onlineshop-Anteil im {monatsname}: "
                              f"{prozent(kanal['anteil_online_prozent'].iloc[-1] / 100)}"),
        diagramm_marge(marge, f"Marge im {monatsname}: {marge['produktgruppe'].iloc[0]} am höchsten "
                              f"({prozent(marge['marge_prozent'].iloc[0] / 100)}), "
                              f"{marge['produktgruppe'].iloc[-1]} am niedrigsten "
                              f"({prozent(marge['marge_prozent'].iloc[-1] / 100)})"),
        diagramm_wachstum(wachstum, f"Januar bis {monatsname} zum Vorjahr: {wachstum['region'].iloc[0]} wächst "
                                    f"am stärksten ({veraenderung(wachstum['wachstum_prozent'].iloc[0])})"),
    ]

    name = args.monat.replace("-", "_")
    kpi.to_csv(ORDNER + f"kpi_{name}.csv", index=False)
    with open(ORDNER + f"bericht_{name}.html", "w", encoding="utf-8") as f:
        f.write(html_bericht(kpi, diagramme, args.monat, args.datei, len(im_monat)))
    print("Gespeichert:", ORDNER + f"bericht_{name}.html")
    print("Gespeichert:", ORDNER + f"kpi_{name}.csv")
    print("Prüfen mit:  python check_zahlen.py", ORDNER + f"kpi_{name}.csv")


if __name__ == "__main__":
    main()
