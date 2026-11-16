# Projektdateien: Nordwind Handel

Alle Befehle laufen im Terminal von VS Code im Kursordner (dem Ordner mit `README.md`, `data/` und `check_setup.py`).

## Ordner

| Ordner | Inhalt |
| --- | --- |
| `data/` (Kursordner) | Startbestand: `nordwind_umsatz.csv`, `nordwind_plan_2026.csv`, `nordwind_feedback.csv`, `kontrollsummen.csv` |
| `lieferungen/` (Kursordner) | spätere Lieferungen: Oktober 2026, defekte Oktober-Lieferung, `kostenstellen.csv` |
| `project/data/` | `generate_data.py`: erzeugt alle Daten neu (fester Zufallswert, immer gleiches Ergebnis) |
| `project/starters/` | Startdatei je Übung; in `project/playground/` kopieren und dort bearbeiten |
| `project/examples/` | fertiges Ergebnis je Lab; das nächste Lab liest seine Eingaben von hier |
| `project/playground/` | eigener Arbeitsbereich |
| `.github/skills/` (Kursordner) | Skills für den KI-Assistenten, zu Beginn nur `kpi-kurzcheck` |

## Lab, Beispiel, Starter

| Lab | Beispiel in `project/examples/` | Starter in `project/starters/` |
| --- | --- | --- |
| 1.1 | `m01-ai-analysis-basics/l01-ai-landscape/`: `ki_landkarte.py`, `erste_zahlen.ipynb` | `m01-l01-erste-zahlen.ipynb` |
| 1.2 | `m01-ai-analysis-basics/l02-four-ways/`: `antwort_a.py`, `antwort_b.py`, `kpi_reference.py` | – |
| 2.1 | `m02-data-preparation/l01-data-quality/`: `datenqualitaet.ipynb`, `quality_check.py`, `probleme.csv` | `m02-l01-datenqualitaet.ipynb` |
| 2.2 | `m02-data-preparation/l02-cleaning/`: `clean.py`, `umsatz_clean.csv` | `m02-l02-clean.py` |
| 2.3 | `m02-data-preparation/l03-features/`: `features.py`, `umsatz_features.csv`, `kunden_rfm.csv` | `m02-l03-features.py` |
| 3.1 | `m03-exploration/l01-eda/`: `eda.ipynb`, `analyse.py`, drei Ergebnistabellen | `m03-l01-eda.ipynb` |
| 3.2 | `m03-exploration/l02-charts/`: `diagramme.ipynb`, `diagramme.py`, drei HTML-Diagramme | `m03-l02-diagramme.ipynb` |
| 3.3 | `m03-exploration/l03-report-script/`: `monatsbericht.py` (v1), `bericht_2026_09.html`, `kpi_2026_09.csv` | `m03-l03-monatsbericht.py` |
| 4.1 | `m04-llm-analysis/l01-pandasai/`: `pandasai_fragen.ipynb` | `m04-l01-pandasai.ipynb` |
| 4.2 | `m04-llm-analysis/l02-feedback/`: `feedback.ipynb`, `feedback_klassifiziert.csv`, `diagramm_themen.html` | `m04-l02-feedback.ipynb` |
| 5.1 | `m05-ml-basics/l01-classification/`: `wiederkauf.ipynb` | `m05-l01-wiederkauf.ipynb` |
| 5.2 | `m05-ml-basics/l02-clustering/`: `segmente.ipynb`, `kunden_segmente.csv`, `segmente.html` | `m05-l02-segmente.ipynb` |
| 5.3 | `m05-ml-basics/l03-anomalies/`: `auffaelligkeiten.ipynb`, `auffaellige_tage.csv` | `m05-l03-auffaelligkeiten.ipynb` |
| 6.1 | `m06-forecast-report/l01-forecast/`: `prognose.ipynb`, `prognose_2026.csv`, `prognose_2026.html` | `m06-l01-prognose.ipynb` |
| 6.2 | `m06-forecast-report/l02-report-v2/`: `monatsbericht.py` (v2), `berichte/` | `m06-l02-monatsbericht.py` |
| 7.1 | Beispiel-Skill `.github/skills/kpi-kurzcheck/` im Kursordner | – |
| 7.2 | `m07-analysis-skill/l02-report-skill/monatsbericht/`: `SKILL.md`, `scripts/monatsbericht.py` | `m07-l02-SKILL.md` |
| 7.3 | `m07-analysis-skill/l03-new-delivery/`: Oktober-Bericht in `berichte/`, `stopp_meldung.txt` | – |
| 8.1 | `m08-validation/l01-fact-check/`: `gegenproben.ipynb`, `kommentar_oktober_korrigiert.md` | `m08-l01-kommentar_oktober.md`, `m08-l01-gegenproben.ipynb` |
| 9.1 | `m09-final-project/l01-cost-report/`: Skill `kostenbericht/`, `gegenrechnung.ipynb`, `berichte/` | `m09-l01-gegenrechnung.ipynb` |

Die fertigen Skills in `examples/` liegen bewusst nicht in `.github/skills/`, damit der KI-Assistent sie nicht vorzeitig findet.

## Häufige Befehle

```bash
python check_setup.py                                     # Umgebung prüfen
python check_zahlen.py project/playground/umsatz_features.csv   # Zahlen gegen Kontrollsummen
python project/playground/monatsbericht.py data/nordwind_umsatz.csv --monat 2026-09   # Bericht v1
python project/examples/m06-forecast-report/l02-report-v2/monatsbericht.py --help    # Bericht v2
python project/data/generate_data.py                      # Daten auf den Startzustand setzen
```

Notebooks öffnen sich in VS Code per Doppelklick; Zellen laufen mit `Umschalt+Enter`.
