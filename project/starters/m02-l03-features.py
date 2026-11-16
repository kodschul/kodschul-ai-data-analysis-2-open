"""Lab 2.3 – Kennzahlen ableiten (Starter).

Aufruf im Kursordner:  python project/playground/m02-l03-features.py
Liest die bereinigte Datei aus dem Beispiel von Lab 2.2 und schreibt
umsatz_features.csv in ORDNER.
"""

import pandas as pd

EINGABE = "project/examples/m02-data-preparation/l02-cleaning/umsatz_clean.csv"
ORDNER = "project/playground/"   # hier landet das Ergebnis


def add_features(df):
    """Neue Spalten aus vorhandenen Spalten."""
    df = df.copy()
    df["datum"] = pd.to_datetime(df["datum"])
    df["monat"] = df["datum"].dt.strftime("%Y-%m")                # z. B. 2026-09
    df["quartal"] = df["datum"].dt.to_period("Q").astype(str)     # z. B. 2026Q3
    df["deckungsbeitrag"] = df["umsatz"] - df["kosten"]           # leer, wenn Kosten fehlen
    # >>> AUFGABE 1: Spalte marge = Deckungsbeitrag / Umsatz – Prompt siehe Übung, Aufgabe 2
    # <<< ENDE AUFGABE 1
    return df


def pruefen(df):
    """Eingebaute Prüfung für Aufgabe 1."""
    print(f"Zeilen:               {len(df):>6}")
    print(f"Zeilen ohne Kosten:   {df['deckungsbeitrag'].isna().sum():>6}")
    if "marge" not in df.columns:
        print("nicht OK  Spalte marge fehlt – Code aus Aufgabe 1 zwischen die Markierungen setzen")
        return
    erwartet = df["deckungsbeitrag"] / df["umsatz"]
    gleich = ((df["marge"] - erwartet).abs() < 1e-9) | (df["marge"].isna() & erwartet.isna())
    if gleich.all():
        print("OK        marge = Deckungsbeitrag / Umsatz in jeder Zeile (leer, wo Kosten fehlen)")
    else:
        print(f"nicht OK  marge weicht in {(~gleich).sum()} Zeilen von Deckungsbeitrag / Umsatz ab")


if __name__ == "__main__":
    df = add_features(pd.read_csv(EINGABE))
    pruefen(df)
    df.to_csv(ORDNER + "umsatz_features.csv", index=False)
    print("Gespeichert:", ORDNER + "umsatz_features.csv")
