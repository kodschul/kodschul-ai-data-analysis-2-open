"""Vergleicht Umsatz, Deckungsbeitrag und Marge einer Tabelle mit den Sollwerten.

Aufruf im Kursordner:  python check_zahlen.py <datei.csv>

Die Tabelle braucht die Spalten region, umsatz und deckungsbeitrag (oder kosten)
sowie monat (JJJJ-MM) oder datum. Summiert wird je Monat und Region; die Marge
wird aus den Summen berechnet (Deckungsbeitrag / Umsatz), nie aufsummiert.
Verglichen werden nur die Monate, die in der Tabelle vorkommen.
"""

import sys

import pandas as pd

SOLLWERTE = "data/kontrollsummen.csv"
TOLERANZ_EURO = 0.05      # Rundung
TOLERANZ_MARGE = 0.0001   # 0,01 Prozentpunkte


def monat_spalte(df):
    if "monat" in df.columns:
        return df["monat"].astype(str).str[:7]
    datum = pd.to_datetime(df["datum"], format="%d.%m.%Y", errors="coerce")
    datum = datum.fillna(pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce"))
    return datum.dt.strftime("%Y-%m")


def main():
    if len(sys.argv) != 2:
        sys.exit("Aufruf: python check_zahlen.py <datei.csv>")
    df = pd.read_csv(sys.argv[1])
    df["monat"] = monat_spalte(df)
    if "deckungsbeitrag" not in df.columns:
        df["deckungsbeitrag"] = df["umsatz"] - df["kosten"]

    ist = df.groupby(["monat", "region"], as_index=False)[["umsatz", "deckungsbeitrag"]].sum()
    ist["marge"] = ist["deckungsbeitrag"] / ist["umsatz"]
    soll = pd.read_csv(SOLLWERTE)
    soll = soll[soll["monat"].isin(ist["monat"])]
    v = soll.merge(ist, on=["monat", "region"], how="outer", suffixes=("_soll", "_ist"), indicator=True)

    print(f"Prüfung von {sys.argv[1]} gegen {SOLLWERTE}")
    print(f"Monate: {ist['monat'].nunique()} ({ist['monat'].min()} bis {ist['monat'].max()}), "
          f"Regionen: {', '.join(sorted(ist['region'].astype(str).unique()))}")

    abweichungen = []
    for _, z in v.iterrows():
        if z["_merge"] != "both":
            wo = "fehlt in der Datei" if z["_merge"] == "left_only" else "nicht in den Sollwerten"
            abweichungen.append((z["monat"], z["region"], "Region", wo))
            continue
        for kz, tol in [("umsatz", TOLERANZ_EURO), ("deckungsbeitrag", TOLERANZ_EURO), ("marge", TOLERANZ_MARGE)]:
            diff = z[f"{kz}_ist"] - z[f"{kz}_soll"]
            if abs(diff) > tol:
                abweichungen.append((z["monat"], z["region"], kz, f"ist {z[f'{kz}_ist']:.4f}, soll {z[f'{kz}_soll']:.4f}"))

    if not abweichungen:
        print(f"Verglichen: {len(v)} Monat-Region-Werte je Kennzahl")
        print("Ergebnis: 0 Abweichungen – Prüfung bestanden")
        return
    print(f"Ergebnis: {len(abweichungen)} Abweichungen – Prüfung NICHT bestanden")
    for monat, region, kz, text in abweichungen[:10]:
        print(f"  {monat}  {region:<12} {kz:<16} {text}")
    if len(abweichungen) > 10:
        print(f"  … und {len(abweichungen) - 10} weitere")
    sys.exit(1)


if __name__ == "__main__":
    main()
