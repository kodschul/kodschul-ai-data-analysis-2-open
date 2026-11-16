"""Lab 2.2 – Bereinigung der Nordwind-Umsatzdatei.

Aufruf im Kursordner:  python project/examples/m02-data-preparation/l02-cleaning/clean.py
Liest data/nordwind_umsatz.csv, schreibt umsatz_clean.csv in ORDNER.
"""

import pandas as pd

EINGABE = "data/nordwind_umsatz.csv"
ORDNER = "project/examples/m02-data-preparation/l02-cleaning/"   # hier landet das Ergebnis


def clean_umsatz(df):
    """Bereinigt eine Nordwind-Umsatztabelle. Jede Regel steht als eigener Schritt."""
    df = df.copy()

    # Schritt 1: Dubletten entfernen (gleiche Zeile doppelt geliefert)
    df = df.drop_duplicates()

    # Schritt 2: Datum lesen – Onlineshop liefert TT.MM.JJJJ, Außendienst JJJJ-MM-TT
    deutsch = pd.to_datetime(df["datum"], format="%d.%m.%Y", errors="coerce")
    iso = pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce")
    df["datum"] = deutsch.fillna(iso)

    # Schritt 3: fehlende Kosten markieren (nicht löschen: der Umsatz zählt trotzdem)
    df["kosten_fehlt"] = df["kosten"].isna()

    # Schritt 4: Regionen vereinheitlichen ("Region Nord", "nord", "Sued" …)
    df["region"] = (
        df["region"]
        .str.strip()                                   # Leerzeichen am Rand weg
        .str.replace("Region ", "", regex=False)       # Vorsilbe "Region " weg
        .str.capitalize()                              # "nord" -> "Nord"
        .replace({"Sued": "Süd"})                      # Umschreibung ersetzen
    )
    return df


def pruefen(vorher, nachher):
    """Zeilenbilanz und drei feste Prüfungen."""
    print(f"Zeilen vorher:        {len(vorher):>6}")
    print(f"Dubletten entfernt:   {len(vorher) - len(nachher):>6}")
    print(f"Zeilen nachher:       {len(nachher):>6}")
    print(f"Zeilen ohne Kosten:   {nachher['kosten_fehlt'].sum():>6}")
    regionen = sorted(nachher["region"].unique())
    pruefungen = {
        "keine Dubletten mehr": not nachher.duplicated().any(),
        "jedes Datum gelesen": nachher["datum"].notna().all(),
        "genau 4 Regionen": regionen == ["Nord", "Ost", "Süd", "West"],
    }
    for name, ok in pruefungen.items():
        print(f"{'OK      ' if ok else 'nicht OK'}  {name}")
    if not pruefungen["genau 4 Regionen"]:
        print("          gefunden:", regionen)


if __name__ == "__main__":
    roh = pd.read_csv(EINGABE)
    sauber = clean_umsatz(roh)
    pruefen(roh, sauber)
    sauber.to_csv(ORDNER + "umsatz_clean.csv", index=False)
    print("Gespeichert:", ORDNER + "umsatz_clean.csv")
