"""Antwort A – eine typische KI-Lösung (vorbereitetes Beispiel) auf die Frage:
"Welche Region wuchs 2025 am stärksten?"

Aufruf im Kursordner:  python project/examples/m01-ai-analysis-basics/l02-four-ways/antwort_a.py
"""

import pandas as pd

df = pd.read_csv("data/nordwind_umsatz.csv")

# Umsatz je Region und Jahr (Spalte "jahr" aus der Datei)
umsatz = df.groupby(["region", "jahr"])["umsatz"].sum().unstack()

# Wachstum 2025 gegenüber 2024 in Prozent
wachstum = (umsatz[2025] / umsatz[2024] - 1) * 100
sieger = wachstum.idxmax()

print(f"Antwort A: {sieger} wuchs 2025 am stärksten, um {wachstum[sieger]:+.1f} %.")
print(f"           (gerechnet mit {len(df)} Zeilen)")
