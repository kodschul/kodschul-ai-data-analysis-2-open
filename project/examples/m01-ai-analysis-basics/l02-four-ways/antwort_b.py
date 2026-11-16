"""Antwort B – eine zweite typische KI-Lösung (vorbereitetes Beispiel) auf dieselbe Frage:
"Welche Region wuchs 2025 am stärksten?"

Aufruf im Kursordner:  python project/examples/m01-ai-analysis-basics/l02-four-ways/antwort_b.py
"""

import pandas as pd

df = pd.read_csv("data/nordwind_umsatz.csv")

# Datum umwandeln; Werte, die nicht passen, werden entfernt
df["datum"] = pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce")
df = df.dropna(subset=["datum"])
df["jahr"] = df["datum"].dt.year

umsatz = df.groupby(["region", "jahr"])["umsatz"].sum().unstack()
wachstum = (umsatz[2025] / umsatz[2024] - 1) * 100
sieger = wachstum.idxmax()

print(f"Antwort B: {sieger} wuchs 2025 am stärksten, um {wachstum[sieger]:+.1f} %.")
print(f"           (gerechnet mit {len(df)} Zeilen)")
