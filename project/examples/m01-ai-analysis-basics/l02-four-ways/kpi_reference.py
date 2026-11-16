"""Referenzrechnung: Welche Region wuchs 2025 am stärksten?

Aufruf im Kursordner:  python project/examples/m01-ai-analysis-basics/l02-four-ways/kpi_reference.py

Vor dem Rechnen werden die Daten bereinigt, mit denselben vier Regeln wie in
Lab 2.2 (clean.py): Dubletten entfernen, beide Datumsformate lesen,
fehlende Kosten markieren, Regionsnamen vereinheitlichen.
"""

import pandas as pd

roh = pd.read_csv("data/nordwind_umsatz.csv")

# 1. Dubletten entfernen
df = roh.drop_duplicates().copy()
# 2. Datum lesen: Onlineshop TT.MM.JJJJ, Außendienst JJJJ-MM-TT
deutsch = pd.to_datetime(df["datum"], format="%d.%m.%Y", errors="coerce")
iso = pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce")
df["datum"] = deutsch.fillna(iso)
# 3. fehlende Kosten markieren (für den Umsatz ohne Bedeutung)
df["kosten_fehlt"] = df["kosten"].isna()
# 4. Regionen vereinheitlichen: "Region Nord", "nord", "Nord " -> "Nord"; "Sued" -> "Süd"
df["region"] = (df["region"].str.strip().str.replace("Region ", "", regex=False)
                .str.capitalize().replace({"Sued": "Süd"}))

df["jahr"] = df["datum"].dt.year
umsatz = df.groupby(["region", "jahr"])["umsatz"].sum().unstack()
wachstum = (umsatz[2025] / umsatz[2024] - 1) * 100

print(f"Zeilen roh: {len(roh)}, nach Bereinigung: {len(df)}, Regionen: {', '.join(umsatz.index)}")
print("Wachstum 2025 gegenüber 2024 je Region:")
for region, wert in wachstum.sort_values(ascending=False).items():
    print(f"  {region:<5} {wert:+6.1f} %")
sieger = wachstum.idxmax()
print(f"Referenz:  {sieger} wuchs 2025 am stärksten, um {wachstum[sieger]:+.1f} %.")
