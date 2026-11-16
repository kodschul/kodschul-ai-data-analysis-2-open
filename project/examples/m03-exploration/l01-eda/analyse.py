"""Lab 3.1 – die drei Analysefragen als Funktionen.

Aufruf im Kursordner:  python project/examples/m03-exploration/l01-eda/analyse.py
Liest umsatz_features.csv aus dem Beispiel von Lab 2.3, gibt die drei Ergebnistabellen
aus und speichert sie als CSV in ORDNER (Eingabe für Lab 3.2).
Dieselben Funktionen stehen in Lab 3.3 in monatsbericht.py.
"""

import pandas as pd

EINGABE = "project/examples/m02-data-preparation/l03-features/umsatz_features.csv"
ORDNER = "project/examples/m03-exploration/l01-eda/"


def wachstum_je_region(df, bis_monat=9):
    """Frage 1: Umsatz Januar bis bis_monat je Region und Jahr, dazu Veränderung zum Vorjahr in %."""
    zeitraum = df[df["datum"].dt.month <= bis_monat]              # gleiche Monate in jedem Jahr
    tabelle = zeitraum.pivot_table(index="region", columns="jahr", values="umsatz", aggfunc="sum")
    letztes_jahr = tabelle.columns.max()
    veraenderung = tabelle.pct_change(axis="columns") * 100       # Jahr gegen Vorjahr in %
    tabelle["wachstum_prozent"] = veraenderung[letztes_jahr]
    tabelle.columns = [str(spalte) for spalte in tabelle.columns]  # 2024 -> "2024"
    return tabelle.round(1).sort_values("wachstum_prozent", ascending=False)


def marge_je_produktgruppe(df):
    """Frage 2: Marge je Produktgruppe = Summe Deckungsbeitrag / Summe Umsatz (nie Mittelwert der Zeilen)."""
    summen = df.groupby("produktgruppe")[["umsatz", "deckungsbeitrag"]].sum()
    summen["marge_prozent"] = summen["deckungsbeitrag"] / summen["umsatz"] * 100
    return summen.round(1).sort_values("marge_prozent", ascending=False)


def kanal_je_monat(df):
    """Frage 3: Umsatz je Monat und Kanal, dazu der Anteil des Onlineshops in %."""
    tabelle = df.pivot_table(index="monat", columns="kanal", values="umsatz", aggfunc="sum")
    tabelle["anteil_online_prozent"] = tabelle["Onlineshop"] / (tabelle["Außendienst"] + tabelle["Onlineshop"]) * 100
    tabelle.columns.name = None                                    # Überschrift "kanal" entfernen
    return tabelle.round(1)


if __name__ == "__main__":
    df = pd.read_csv(EINGABE, parse_dates=["datum"])
    ergebnisse = {
        "wachstum_region.csv": wachstum_je_region(df),
        "marge_produktgruppe.csv": marge_je_produktgruppe(df),
        "kanal_monat.csv": kanal_je_monat(df),
    }
    for datei, tabelle in ergebnisse.items():
        print(f"\n{datei}\n{tabelle.tail(6)}")
        tabelle.to_csv(ORDNER + datei)
    print("\nGespeichert in", ORDNER)
