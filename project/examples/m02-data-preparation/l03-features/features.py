"""Lab 2.3 – Kennzahlen ableiten.

Aufruf im Kursordner:  python project/examples/m02-data-preparation/l03-features/features.py
Liest die bereinigte Datei aus dem Beispiel von Lab 2.2, schreibt
umsatz_features.csv und kunden_rfm.csv in ORDNER.
"""

import pandas as pd

EINGABE = "project/examples/m02-data-preparation/l02-cleaning/umsatz_clean.csv"
ORDNER = "project/examples/m02-data-preparation/l03-features/"


def add_features(df):
    """Neue Spalten aus vorhandenen Spalten."""
    df = df.copy()
    df["datum"] = pd.to_datetime(df["datum"])
    df["monat"] = df["datum"].dt.strftime("%Y-%m")                # z. B. 2026-09
    df["quartal"] = df["datum"].dt.to_period("Q").astype(str)     # z. B. 2026Q3
    df["deckungsbeitrag"] = df["umsatz"] - df["kosten"]           # leer, wenn Kosten fehlen
    df["marge"] = df["deckungsbeitrag"] / df["umsatz"]            # Anteil, z. B. 0.25 = 25 %
    return df


def kunden_rfm(df, stichtag):
    """Je Kunde: wie lange her (Tage), wie oft (Buchungen), wie viel (Umsatz)."""
    bis = df[df["datum"] <= stichtag]
    rfm = bis.groupby("kunde_id").agg(
        letzter_kauf=("datum", "max"),
        haeufigkeit=("beleg_nr", "count"),
        umsatz=("umsatz", "sum"),
    )
    rfm["tage_seit_kauf"] = (pd.Timestamp(stichtag) - rfm["letzter_kauf"]).dt.days
    return rfm[["tage_seit_kauf", "haeufigkeit", "umsatz"]].round(2).reset_index()


if __name__ == "__main__":
    df = add_features(pd.read_csv(EINGABE))
    df.to_csv(ORDNER + "umsatz_features.csv", index=False)
    print("Gespeichert:", ORDNER + "umsatz_features.csv", f"({len(df)} Zeilen)")

    rfm = kunden_rfm(df, "2026-09-30")
    rfm.to_csv(ORDNER + "kunden_rfm.csv", index=False)
    print("Gespeichert:", ORDNER + "kunden_rfm.csv", f"({len(rfm)} Kunden)")
