"""Lab 2.1 – Qualitätscheck einer Nordwind-Umsatzdatei als Skript.

Aufruf im Kursordner:
    python project/examples/m02-data-preparation/l01-data-quality/quality_check.py data/nordwind_umsatz.csv

Prüft dieselben Punkte wie das Notebook aus Lab 2.1 und gibt die Problemtabelle aus.
Ändert die Datei nicht.
"""

import sys

import pandas as pd

PFLICHT = ["beleg_nr", "datum", "jahr", "kunde_id", "region", "produktgruppe",
           "kanal", "menge", "umsatz", "kosten"]
REGIONEN = ["Nord", "Süd", "West", "Ost"]
GRENZE_UMSATZ = 5000   # Euro je Zeile; darüber fachlich prüfen


def problemtabelle(df):
    """Eine Zeile je Problem: was, welche Spalte, wie oft, Vorschlag."""
    fehlende_spalten = [s for s in PFLICHT if s not in df.columns]
    if fehlende_spalten:
        return pd.DataFrame([{"Problem": "Pflichtspalte fehlt", "Spalte": ", ".join(fehlende_spalten),
                              "Anzahl": len(fehlende_spalten), "Vorschlag": "Lieferung zurückgeben"}])
    zeilen = [
        ("Dubletten (Zeile doppelt geliefert)", "alle", df.duplicated().sum(), "entfernen"),
        ("Kosten fehlen", "kosten", df["kosten"].isna().sum(), "markieren, nicht löschen"),
        ("Datum als TT.MM.JJJJ statt JJJJ-MM-TT", "datum",
         df["datum"].str.contains(".", regex=False).sum(), "beide Formate lesen"),
        ("Regionsname nicht Nord/Süd/West/Ost", "region",
         (~df["region"].isin(REGIONEN)).sum(), "vereinheitlichen"),
        (f"Umsatz über {GRENZE_UMSATZ} € in einer Zeile", "umsatz",
         (df["umsatz"] > GRENZE_UMSATZ).sum(), "fachlich prüfen"),
    ]
    return pd.DataFrame(zeilen, columns=["Problem", "Spalte", "Anzahl", "Vorschlag"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Aufruf: python quality_check.py <datei.csv>")
    df = pd.read_csv(sys.argv[1])
    print(f"Datei: {sys.argv[1]}, {len(df)} Zeilen, {len(df.columns)} Spalten")
    if "region" in df.columns:
        print(f"Schreibweisen in region: {df['region'].nunique()}")
    print(problemtabelle(df).to_string(index=False))
