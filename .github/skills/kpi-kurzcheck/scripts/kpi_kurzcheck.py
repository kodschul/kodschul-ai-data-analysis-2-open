"""KPI-Kurzcheck: Zeilen, Monatsbereich und Gesamtumsatz der Nordwind-Rohdatei.

Aufruf im Kursordner:  python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py
Rechnet auf den Rohdaten (vor der Bereinigung), nur zum schnellen Überblick.
"""

import sys
from pathlib import Path

import pandas as pd

DATEI = "data/nordwind_umsatz.csv"

if not Path(DATEI).exists():
    sys.exit(f"STOPP: {DATEI} nicht gefunden – im Kursordner ausführen.")

df = pd.read_csv(DATEI)
datum = pd.to_datetime(df["datum"], format="%d.%m.%Y", errors="coerce")
datum = datum.fillna(pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce"))
monate = datum.dt.strftime("%Y-%m")
summe = f"{df['umsatz'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(f"KPI-Kurzcheck {DATEI} (Rohdaten, vor Bereinigung)")
print(f"Zeilen:        {len(df)}")
print(f"Monate:        {monate.min()} bis {monate.max()} ({monate.nunique()} Monate)")
print(f"Umsatz gesamt: {summe} €")
