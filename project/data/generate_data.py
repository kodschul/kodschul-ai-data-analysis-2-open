"""Erzeugt alle Kursdaten für Nordwind Handel (synthetisch, fester Seed).

Aufruf aus dem Kursordner:  python project/data/generate_data.py
Schreibt nach data/ (Startbestand) und lieferungen/ (spätere Lieferungen).
Bestehende Dateien werden überschrieben – so lässt sich der Startzustand
jederzeit wiederherstellen.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
ROOT = Path(__file__).resolve().parents[2]          # Kursordner output/
DATA = ROOT / "data"
LIEFERUNGEN = ROOT / "lieferungen"

REGIONEN = ["Nord", "Süd", "West", "Ost"]
REGION_ANTEIL = {"Nord": 0.30, "Süd": 0.25, "West": 0.25, "Ost": 0.20}
REGION_TREND = {"Nord": 0.04, "Süd": 0.07, "West": 0.10, "Ost": -0.03}  # pro Jahr
SCHREIBWEISEN = {
    "Nord": ["Region Nord", "nord", "Nord "],
    "Süd": ["Region Süd", "Sued", "süd"],
    "West": ["Region West", "west"],
    "Ost": ["Region Ost", "ost"],
}
GRUPPEN = {  # Produktgruppe: (Stückpreis, Marge)
    "Papier": (9.5, 0.18), "Schreibwaren": (3.2, 0.36), "Ordnung": (5.8, 0.30),
    "Reinigung": (7.4, 0.25), "Küche": (6.1, 0.28), "Technik": (24.0, 0.15),
}
SAISON = {1: 1.05, 2: 0.95, 3: 1.00, 4: 0.95, 5: 0.95, 6: 0.90,
          7: 0.85, 8: 1.10, 9: 1.05, 10: 1.00, 11: 1.10, 12: 0.90}
RELAUNCH = pd.Timestamp("2026-03-01")               # Onlineshop-Relaunch
ZEILEN_PRO_TAG = 44


def kunden_erzeugen(rng):
    """400 Geschäftskunden mit Heimatregion und Kaufverhalten."""
    typen = rng.choice(["Großkunde", "Stammkunde", "Gelegenheit", "Abwanderer"],
                       size=400, p=[0.08, 0.35, 0.40, 0.17])
    gewicht = {"Großkunde": 5.0, "Stammkunde": 2.0, "Gelegenheit": 0.5, "Abwanderer": 1.5}
    korb = {"Großkunde": 1.8, "Stammkunde": 1.1, "Gelegenheit": 0.8, "Abwanderer": 1.0}
    kunden = pd.DataFrame({
        "kunde_id": [f"K{i:04d}" for i in range(1, 401)],
        "region": rng.choice(REGIONEN, size=400, p=list(REGION_ANTEIL.values())),
        "typ": typen,
    })
    kunden["gewicht"] = [gewicht[t] * rng.lognormal(0, 0.5) for t in typen]
    kunden["korb"] = [korb[t] for t in typen]
    # Abwanderer kaufen ab einem Datum zwischen 07/2025 und 05/2026 nicht mehr
    ende = pd.to_datetime(rng.integers(pd.Timestamp("2025-07-01").value // 10**9,
                                       pd.Timestamp("2026-05-31").value // 10**9, 400), unit="s")
    kunden["aktiv_bis"] = pd.Series(ende.normalize()).where(kunden["typ"] == "Abwanderer", pd.Timestamp("2099-01-01"))
    return kunden


def buchungen(rng, kunden, start, ende):
    """Saubere Buchungen (eine Zeile je Position) für einen Zeitraum."""
    tage = pd.bdate_range(start, ende)
    zeilen = []
    for tag in tage:
        jahre = (tag - pd.Timestamp("2024-01-01")).days / 365
        for region in REGIONEN:
            faktor = SAISON[tag.month] * (1 + REGION_TREND[region]) ** jahre
            n = int(round(ZEILEN_PRO_TAG * REGION_ANTEIL[region] * faktor * rng.normal(1, 0.08)))
            aktiv = kunden[(kunden["region"] == region) & (kunden["aktiv_bis"] > tag)]
            if n == 0 or aktiv.empty:
                continue
            idx = rng.choice(aktiv.index, size=n, p=aktiv["gewicht"] / aktiv["gewicht"].sum())
            online_anteil = 0.22 * (1.30 if tag >= RELAUNCH else 1.0)
            for k in idx:
                gruppe = rng.choice(list(GRUPPEN), p=[0.25, 0.2, 0.17, 0.15, 0.13, 0.10])
                preis, marge = GRUPPEN[gruppe]
                menge = max(1, int(rng.gamma(6.0, 5 * kunden.at[k, "korb"])))
                umsatz = round(menge * preis * rng.uniform(0.95, 1.05), 2)
                kanal = "Onlineshop" if rng.random() < online_anteil else "Außendienst"
                m = marge - (0.02 if kanal == "Onlineshop" else 0) + rng.normal(0, 0.03)
                zeilen.append((tag, kunden.at[k, "kunde_id"], region, gruppe, kanal,
                               menge, umsatz, round(umsatz * (1 - m), 2)))
    df = pd.DataFrame(zeilen, columns=["datum", "kunde_id", "region", "produktgruppe",
                                       "kanal", "menge", "umsatz", "kosten"])
    return df


def anomalien_einbauen(df, rng, kunden):
    """Zwei dokumentierte Auffälligkeiten."""
    # 1) 27.11.2025, Region West: echter Großauftrag (Technik für einen Schulträger)
    gross = pd.DataFrame({
        "datum": pd.Timestamp("2025-11-27"), "kunde_id": "K0007", "region": "West",
        "produktgruppe": "Technik", "kanal": "Außendienst",
        "menge": [120, 110, 95, 130], "umsatz": [5880.00, 5390.00, 4655.00, 6370.00],
    })
    gross["kosten"] = (gross["umsatz"] * 0.86).round(2)
    df = pd.concat([df, gross], ignore_index=True)
    # 2) 10.02.2026, Region Ost: Kommafehler, Betrag 100-fach erfasst
    mask = (df["datum"] == "2026-02-10") & (df["region"] == "Ost")
    i = df[mask].index[0]
    for spalte in ["umsatz", "kosten"]:
        df.loc[i, spalte] = round(float(df.loc[i, spalte]) * 100, 2)
    return df


def kosten_entfernen(df, rng, anteil=0.02):
    df = df.copy()
    df.loc[rng.random(len(df)) < anteil, "kosten"] = np.nan
    return df


def roh_machen(sauber, rng, start_nr):
    """Baut die Qualitätsprobleme der Lieferdatei ein."""
    roh = sauber.copy()
    roh.insert(0, "beleg_nr", [f"B{start_nr + i:06d}" for i in range(len(roh))])
    roh.insert(2, "jahr", roh["datum"].dt.year)
    # Datumsformat: Onlineshop-Export TT.MM.JJJJ, Außendienst ISO
    roh["datum"] = np.where(roh["kanal"] == "Onlineshop",
                            roh["datum"].dt.strftime("%d.%m.%Y"),
                            roh["datum"].dt.strftime("%Y-%m-%d"))
    # Uneinheitliche Regionsnamen seit dem neuen Vertriebssystem 2025
    for region, varianten in SCHREIBWEISEN.items():
        m = (roh["region"] == region) & (roh["jahr"] >= 2025) & (rng.random(len(roh)) < 0.08)
        roh.loc[m, "region"] = rng.choice(varianten, size=m.sum())
    # Dubletten: gut 1 % der Zeilen doppelt geliefert
    dubletten = roh.sample(frac=0.012, random_state=SEED)
    roh = pd.concat([roh, dubletten]).sort_values(["beleg_nr"]).reset_index(drop=True)
    return roh


def kontrollsummen(sauber):
    """Sollwerte je Monat und Region – Zeilen ohne Kosten zählen beim Umsatz mit,
    beim Deckungsbeitrag nicht (so rechnet auch das Vorsystem)."""
    d = sauber.assign(monat=sauber["datum"].dt.strftime("%Y-%m"),
                      deckungsbeitrag=sauber["umsatz"] - sauber["kosten"])
    k = d.groupby(["monat", "region"], as_index=False).agg(
        umsatz=("umsatz", "sum"), deckungsbeitrag=("deckungsbeitrag", "sum"))
    k["marge"] = (k["deckungsbeitrag"] / k["umsatz"]).round(4)
    return k.round({"umsatz": 2, "deckungsbeitrag": 2})


def plan_2026(sauber):
    """Plan je Region und Monat: Vorjahr + Planwachstum (Ost mit Wachstumsziel)."""
    vj = sauber[sauber["datum"].dt.year == 2025]
    vj = vj.groupby([vj["datum"].dt.month, "region"])["umsatz"].sum().reset_index()
    ziel = {"Nord": 1.05, "Süd": 1.06, "West": 1.08, "Ost": 1.03}
    vj["plan_umsatz"] = (vj.apply(lambda r: r["umsatz"] * ziel[r["region"]], axis=1) / 1000).round() * 1000
    vj["monat"] = "2026-" + vj["datum"].astype(str).str.zfill(2)
    return vj[["monat", "region", "plan_umsatz"]]


def feedback(rng):
    """300 Kundenkommentare; von den ersten 50 sind 20 von Hand gelabelt."""
    texte = {
        ("Lieferung", "positiv"): ["Lieferung kam pünktlich und vollständig.", "Super schnelle Lieferung, danke!",
                                   "Ware war schon am nächsten Morgen da.", "Lieferung wie immer zuverlässig."],
        ("Lieferung", "negativ"): ["Lieferung kam drei Tage zu spät.", "Paket unvollständig, zwei Kartons fehlen.",
                                   "Lieferung kam, endlich.", "Schon wieder Verspätung beim Versand."],
        ("Preis", "positiv"): ["Preise sind fair für die Qualität.", "Gutes Angebot beim Kopierpapier."],
        ("Preis", "negativ"): ["Die Preise sind deutlich gestiegen.", "Bei der Konkurrenz ist Toner billiger.",
                               "Preiserhöhung ohne Vorwarnung, ärgerlich."],
        ("Qualität", "positiv"): ["Ordner sind stabil und gut verarbeitet.", "Reinigungsmittel wirkt sehr gut."],
        ("Qualität", "negativ"): ["Kugelschreiber schreiben nach einer Woche nicht mehr.", "Papier staut ständig im Drucker.",
                                  "Qualität der Müllbeutel hat nachgelassen."],
        ("Onlineshop", "positiv"): ["Der neue Onlineshop ist viel übersichtlicher.", "Bestellung im Shop ging schnell.",
                                    "Nachbestellen im Shop klappt jetzt mit zwei Klicks."],
        ("Onlineshop", "negativ"): ["Im Shop finde ich die Artikelnummern nicht mehr.", "Login im Onlineshop klappt nicht.",
                                    "Warenkorb wurde beim Bezahlen gelöscht."],
        ("Service", "positiv"): ["Außendienst hat sich toll gekümmert.", "Schnelle Antwort vom Kundenservice."],
        ("Service", "negativ"): ["Niemand ruft zurück.", "Hotline ist dauernd besetzt."],
        ("Service", "neutral"): ["Bitte Rechnung künftig als PDF schicken.", "Gibt es einen neuen Ansprechpartner?"],
        ("Lieferung", "neutral"): ["Lieferung bitte nur vormittags.", "Ist eine Teillieferung möglich?"],
    }
    schluessel = list(texte)
    rows = []
    for i in range(1, 301):
        thema, stimmung = schluessel[rng.integers(len(schluessel))]
        text = rng.choice(texte[(thema, stimmung)])
        rows.append((i, pd.Timestamp("2026-04-01") + pd.Timedelta(days=int(rng.integers(0, 183))),
                     rng.choice(["Onlineshop", "Außendienst"]), text, thema, stimmung))
    fb = pd.DataFrame(rows, columns=["id", "datum", "kanal", "kommentar", "thema_label", "stimmung_label"])
    gelabelt = set(rng.choice(np.arange(1, 51), size=20, replace=False))
    fb.loc[~fb["id"].isin(gelabelt), ["thema_label", "stimmung_label"]] = ""
    fb["datum"] = fb["datum"].dt.strftime("%Y-%m-%d")
    return fb


def kostenstellen(rng):
    """Zweiter, fremder Datensatz: Kostenbuchungen im deutschen Excel-Format."""
    stellen = {"Vertrieb": 4200, "Marketing": 2600, "IT": 3100, "Fuhrpark": 1800,
               "Gebäude": 2900, "Personalentwicklung": 900}
    rows = []
    for tag in pd.bdate_range("2023-10-01", "2026-09-30"):
        jahre = (tag - pd.Timestamp("2023-10-01")).days / 365
        for stelle, basis in stellen.items():
            if rng.random() < 0.35:
                betrag = basis / 7 * SAISON[tag.month] * (1.04 ** jahre) * rng.lognormal(0, 0.35)
                rows.append((tag, stelle, round(betrag, 2)))
    df = pd.DataFrame(rows, columns=["Buchungsdatum", "Kostenstelle", "Betrag"])
    df["Buchungsdatum"] = df["Buchungsdatum"].dt.strftime("%d.%m.%Y")
    return df


def main():
    rng = np.random.default_rng(SEED)
    DATA.mkdir(exist_ok=True)
    LIEFERUNGEN.mkdir(exist_ok=True)
    kunden = kunden_erzeugen(rng)

    alles = buchungen(rng, kunden, "2024-01-01", "2026-10-31")
    alles = anomalien_einbauen(alles, rng, kunden)
    alles = kosten_entfernen(alles, rng).sort_values(["datum", "region"], kind="stable").reset_index(drop=True)
    historie = alles[alles["datum"] < "2026-10-01"]
    oktober = alles[alles["datum"] >= "2026-10-01"]

    roh_hist = roh_machen(historie, rng, 1)
    roh_okt = roh_machen(oktober, rng, len(historie) + 1)
    roh_hist.to_csv(DATA / "nordwind_umsatz.csv", index=False)
    roh_okt.to_csv(LIEFERUNGEN / "nordwind_umsatz_2026_10.csv", index=False)
    roh_okt.rename(columns={"umsatz": "umsatz_eur"}).to_csv(
        LIEFERUNGEN / "nordwind_umsatz_2026_10_defekt.csv", index=False)

    kontrollsummen(alles).to_csv(DATA / "kontrollsummen.csv", index=False)
    plan_2026(alles).to_csv(DATA / "nordwind_plan_2026.csv", index=False)
    feedback(rng).to_csv(DATA / "nordwind_feedback.csv", index=False)
    kostenstellen(rng).to_csv(LIEFERUNGEN / "kostenstellen.csv", sep=";", decimal=",",
                              index=False, encoding="cp1252")

    print(f"data/nordwind_umsatz.csv          {len(roh_hist):>6} Zeilen (01/2024–09/2026)")
    print(f"lieferungen/nordwind_umsatz_2026_10.csv {len(roh_okt):>6} Zeilen")
    print("data/kontrollsummen.csv, data/nordwind_plan_2026.csv, data/nordwind_feedback.csv")
    print("lieferungen/nordwind_umsatz_2026_10_defekt.csv, lieferungen/kostenstellen.csv")


if __name__ == "__main__":
    main()
