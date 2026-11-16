<div align="center">

<img src="assets/kodschul-logo.png" alt="Kodschul" width="220" />

# Generative KI in der Datenanalyse

2-Tage-Workshop · Python · Deutsch

**Daten mit KI aufbereiten, auswerten und als prüfbaren Bericht automatisieren**

</div>

---

[Worum es geht](#worum-es-geht) · [Start](#start) · [Tag 1](#tag-1) · [Tag 2](#tag-2) · [Hilfe](#hilfe)

## Worum es geht

- Jeden Monat kommt eine neue Datei, und derselbe Bericht entsteht wieder von Hand.
- KI hilft beim Aufbereiten, Analysieren und Erklären, rechnet aber nicht zuverlässig.
- Der Workshop baut daraus ein Python-Skript, das rechnet und sich selbst prüft, und einen Skill, mit dem der KI-Assistent es per Satz startet.
- Ergebnis: ein Monatsbericht mit Prognose und Auffälligkeiten, dazu ein zweiter Skill für einen weiteren Datensatz.

| | |
| --- | --- |
| **Für** | Controlling, BI und Reporting, Datenanalyse, Marketing |
| **Vorkenntnisse** | Python-Grundlagen; pandas, Notebooks und Machine Learning nicht nötig |
| **Werkzeuge** | VS Code mit GitHub Copilot Chat oder Claude Code, Python 3.11, pandas, plotly, scikit-learn, PandasAI |
| **Szenario** | Nordwind Handel, Großhandel mit vier Regionen und einer Umsatzdatei pro Monat |
| **Material** | Handout pro Lab, Spickzettel pro Modul, Start- und Ergebnisdateien für jedes Lab |

## Start

1. Umgebung prüfen: [Setup und Installation](00-setup-and-installation.md)
2. Ziel und Tagesablauf lesen: [Kursüberblick](m00-overview/overview.md)
3. Im Terminal von VS Code ausführen:

```bash
python check_setup.py
```

## Tag 1

| Modul | Kernthemen | Ergebnis |
| --- | --- | --- |
| 1 [KI in der Datenanalyse](m01-ai-analysis-basics/l01-ai-landscape/l01-ai-landscape-thx.md) | Ablauf einer Analyse, Landkarte der KI, vier Wege, Copilot Chat | erste Zahlen, drei Antworten im Vergleich |
| 2 [Datenaufbereitung mit KI](m02-data-preparation/l01-data-quality/l01-data-quality-thx.md) | Datenqualität, Bereinigung als Skript, Kennzahlen, Kontrollsummen | bereinigte Daten, Prüfung bestanden |
| 3 [Explorative Analyse und Visualisierung](m03-exploration/l01-eda/l01-eda-thx.md) | Muster finden, Diagramme mit Aussage, Bericht als Skript | Monatsbericht v1 im Browser |
| 4 [Sprachmodelle in der Analyse](m04-llm-analysis/l01-pandasai/l01-pandasai-thx.md) | PandasAI, Antworten prüfen, Kundenfeedback einordnen | geprüfte Antwort, klassifiziertes Feedback |

## Tag 2

| Modul | Kernthemen | Ergebnis |
| --- | --- | --- |
| 5 [Machine Learning](m05-ml-basics/l01-classification/l01-classification-thx.md) | Lernen aus Daten, Kundensegmente, Auffälligkeiten | Vorhersage, Segmente, auffällige Tage |
| 6 [Prognose und erweiterter Bericht](m06-forecast-report/l01-forecast/l01-forecast-thx.md) | Prognose mit Backtest, Bericht v2, Excel-Export | Monatsbericht v2 mit Prüfung |
| 7 [Die Analyse als Skill](m07-analysis-skill/l01-skill-anatomy/l01-skill-anatomy-thx.md) | Aufbau eines Skills, Skill bauen, neue Lieferung | Oktober-Bericht per Satz im Chat |
| 8 [KI-Ergebnisse validieren](m08-validation/l01-fact-check/l01-fact-check-thx.md) | Sollwerte, Gegenprobe, Bias, Verantwortung | korrigierter Managementkommentar |
| 9 [Abschlussprojekt](m09-final-project/l01-cost-report/l01-cost-report-thx.md) | Muster übertragen, Einsatz im Unternehmen | zweiter Skill für Kostenstellen |

- Jedes Lab ist eine Seite mit Leitfragen und Kerninhalt, dazu eine Übung mit Lösung.
- Spickzettel liegen im jeweiligen Modulordner.
- Alle Labs mit Zeiten: [Module und Labs](m00-overview/topics.md).

## Hilfe

- **Weiterarbeiten nach einer Lücke:** Jedes Lab liest seine Eingaben aus dem fertigen Beispiel des vorigen Labs in `project/examples/`; eigene Abweichungen blockieren also nichts.
- **Neu anfangen:** den Starter aus `project/starters/` erneut in `project/playground/` kopieren; Daten zurücksetzen mit `python project/data/generate_data.py`.
- **Lösungen vergleichen:** Jede Übung hat eine Lösungsseite; die fertigen Dateien liegen im [Projektordner](project/README.md).
- **Nachschlagen:** [Glossar](m00-overview/glossary.md) · [FAQ](m00-overview/faq.md) · [Best Practices](m00-overview/best-practices.md)

---

<div align="center">

<sub>© Nextise GmbH · <a href="https://www.kodschul.com">kodschul.com</a> · Kompetenz aufbauen – von der sicheren KI-Anwendung bis zur modernen IT-Basis</sub>

</div>
