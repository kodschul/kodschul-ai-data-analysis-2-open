# Lab 1.2 – Übung: Vier Wege, KI einzusetzen

**Dauer:** ca. 15 Minuten
**Ändert die Nordwind-Projektbasis?** Nein – der Agent legt nur eine Testdatei im eigenen Arbeitsbereich an.

## Vorbereitung

- Terminal aus Lab 1.1 ist offen und steht im Kursordner.
- Dateien: [`antwort_a.py`](../../project/examples/m01-ai-analysis-basics/l02-four-ways/antwort_a.py), [`antwort_b.py`](../../project/examples/m01-ai-analysis-basics/l02-four-ways/antwort_b.py), [`kpi_reference.py`](../../project/examples/m01-ai-analysis-basics/l02-four-ways/kpi_reference.py) in `project/examples/m01-ai-analysis-basics/l02-four-ways/`
- Ergebnisdatei: `project/playground/antwort_a_korrigiert.py` (legt der Agent in Aufgabe 2 an)

## Aufgaben

1. Führe die drei Skripte nacheinander im Terminal aus und vergleiche die drei Prozentwerte:

   ```bash
   python project/examples/m01-ai-analysis-basics/l02-four-ways/antwort_a.py
   python project/examples/m01-ai-analysis-basics/l02-four-ways/antwort_b.py
   python project/examples/m01-ai-analysis-basics/l02-four-ways/kpi_reference.py
   ```

2. Öffne den Chat mit **Strg+Alt+I**, beginne mit **+** einen neuen Chat, wähle im Auswahlfeld **Agent** und sende diesen Prompt (die beiden `#file:`-Angaben über `#` aus der Liste wählen):

   > Die Skripte #file:antwort_a.py und #file:kpi_reference.py beantworten dieselbe Frage „Welche Region wuchs 2025 am stärksten?" mit unterschiedlichen Zahlen (+3,6 % und +13,4 %). Erkläre in höchstens fünf Stichpunkten, was antwort_a.py anders rechnet. Lege danach project/playground/antwort_a_korrigiert.py an: wie antwort_a.py, aber vor der Rechnung doppelte Zeilen entfernen und die Regionsnamen wie in kpi_reference.py vereinheitlichen. Führe die neue Datei mit python aus. Ändere keine anderen Dateien.

   Lies im Bestätigungsdialog den Befehl: Er muss `python project/playground/antwort_a_korrigiert.py` lauten. Wähle dann **Allow**. Prüfe in der Liste der geänderten Dateien, dass nur `antwort_a_korrigiert.py` neu ist, und wähle **Keep**.

3. Technik-Test für Tag 2: Beginne einen neuen Chat im Modus **Agent** und sende den Satz:

   > Führe den KPI-Kurzcheck für die Nordwind-Daten aus.

   Lies im Bestätigungsdialog den angezeigten Befehl, erlaube ihn mit **Allow** und prüfe die Zahlen in der Antwort.

**Claude Code:** Prompt im Claude-Code-Panel senden, Dateien mit `@` statt `#file:` nennen; Datei-Änderung und Befehl im Dialog genauso prüfen und erlauben.

## Checkpoint

- Das Terminal zeigt drei Antworten: `+3.6 %`, `+2.9 %`, `+13.4 %`, jedes Mal West.
- Die Erklärung des Agenten nennt mindestens Dubletten und Regionsschreibweisen.
- `antwort_a_korrigiert.py` meldet West mit `+13.4 %`.
- Der Technik-Test zeigt einen Befehl mit `kpi_kurzcheck.py` und in der Antwort `33554` Zeilen.

## Abschlusskriterien

- Drei verschiedene Zahlen zur selben Frage liegen vor, dazu die Erklärung der Abweichung.
- Der Agent hat eine Datei angelegt und ausgeführt, der Skill-Test hat ein Skript ausgeführt.

## Erweiterung

Beginne zweimal hintereinander einen neuen Chat im Modus **Agent** und stelle jeweils die Frage „Welche Region wuchs 2025 am stärksten? Die Daten liegen in data/nordwind_umsatz.csv." Erlaube nur Befehle, die `python` ausführen. Vergleiche die beiden Prozentwerte mit den drei Zahlen aus Aufgabe 1.

## Fallback

- Kein Chat verfügbar: Die Erklärung und das korrigierte Skript stehen in der Lösung; das Skript dort nach `project/playground/antwort_a_korrigiert.py` kopieren und ausführen.
- Agent zeigt einen anderen Befehl oder ändert weitere Dateien: **Skip** bzw. **Undo** wählen, neuen Chat beginnen und den Prompt erneut senden.
- Skill-Test klappt nicht: neuen Chat beginnen und „Nutze den Skill kpi-kurzcheck." senden. Klappt es weiter nicht, den Befehl selbst ausführen (`python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py`) und den Trainer informieren; bis Tag 2 wird es geklärt.
