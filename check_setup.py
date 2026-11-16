"""Prüft die Kursumgebung. Aufruf im Kursordner:  python check_setup.py
Mit Test des Sprachmodells (braucht den Kurs-API-Schlüssel):  python check_setup.py --llm
"""

import importlib
import importlib.metadata
import os
import sys
from pathlib import Path

PAKETE = {"pandas": "pandas", "numpy": "numpy", "openpyxl": "openpyxl", "plotly": "plotly", "sklearn": "scikit-learn",
          "pandasai": "pandasai", "matplotlib": "matplotlib", "ipykernel": "ipykernel"}  # Modul: Paketname
DATEIEN = ["data/nordwind_umsatz.csv", "data/nordwind_plan_2026.csv", "data/nordwind_feedback.csv",
           "data/kontrollsummen.csv", "lieferungen/nordwind_umsatz_2026_10.csv",
           "lieferungen/nordwind_umsatz_2026_10_defekt.csv", "lieferungen/kostenstellen.csv",
           ".github/skills/kpi-kurzcheck/SKILL.md"]
MODELL = "gpt-4.1-mini"  # Kursmodell für PandasAI und classify(), vor Kursbeginn prüfen

fehler = 0


def zeile(ok, text):
    global fehler
    fehler += 0 if ok else 1
    print(("OK          " if ok else "NICHT OK    ") + text)


zeile(sys.version_info[:2] == (3, 11), f"Python {sys.version.split()[0]} (erwartet 3.11)")
for modul, paket in PAKETE.items():
    try:
        importlib.import_module(modul)
        zeile(True, f"{paket} {importlib.metadata.version(paket)}")
    except ImportError:
        zeile(False, f"{paket} fehlt – python -m pip install -r requirements.txt")
for datei in DATEIEN:
    zeile(Path(datei).exists(), datei)
zeile("OPENAI_API_KEY" in os.environ, "Umgebungsvariable OPENAI_API_KEY gesetzt (Wert wird nicht angezeigt)")

if "--llm" in sys.argv:
    try:
        import litellm
        antwort = litellm.completion(model=MODELL, messages=[{"role": "user", "content": "Antworte nur mit OK."}])
        zeile(True, f"Sprachmodell {MODELL} antwortet: {antwort.choices[0].message.content.strip()}")
    except Exception as e:  # noqa: BLE001 – jede Störung soll sichtbar werden
        zeile(False, f"Sprachmodell nicht erreichbar: {type(e).__name__}")

print()
print("Alles bereit." if fehler == 0 else f"{fehler} Punkt(e) nicht OK – siehe oben.")
