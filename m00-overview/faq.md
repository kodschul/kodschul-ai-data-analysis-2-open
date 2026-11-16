# FAQ

## Sind pandas- oder ML-Vorkenntnisse nötig?

- Nein. Python-Grundlagen reichen.
- pandas startet in Lab 2.1, Machine Learning in Lab 5.1.

## Was tun, wenn eine markierte Stelle nicht gelingt?

- Nach dem zweiten Versuch das Lösungs-Snippet aus der Lösungsseite einsetzen.
- Das nächste Lab startet ohnehin aus dem fertigen Beispiel.

## Warum rechnet der KI-Chat nicht einfach den Bericht?

- Ein Sprachmodell wählt bei jeder Frage einen neuen Rechenweg.
- Ein Skript liefert bei gleicher Datei immer dieselbe Zahl.
- Details: [Lab 1.2](../m01-ai-analysis-basics/l02-four-ways/l02-four-ways-thx.md)

## Welche Daten gehen an den KI-Dienst?

- Copilot und Claude Code: der Chat und die angehängten Dateien.
- PandasAI: Spaltennamen, Spaltentypen und die ersten Zeilen.
- `classify()`: jeder einzelne Kommentar.

## Was ist der Unterschied zwischen PandasAI und einem Skript?

- PandasAI erzeugt für jede Frage neuen Code: gut zum Erkunden.
- Das Skript bleibt gleich: gut für den wiederkehrenden Bericht.

## Woher kommen die Sollwerte in `kontrollsummen.csv`?

- Im Kurs aus dem Datengenerator, unabhängig vom eigenen Code.
- Im Unternehmen aus dem Vorsystem, z. B. ERP oder Hauptbuch.

## Der Skill löst nicht aus. Was nun?

- Ausdrücklich: „Nutze den Skill monatsbericht und …".
- Sonst den Befehl aus `SKILL.md` im Terminal ausführen.
- Details: [Lab 7.1](../m07-analysis-skill/l01-skill-anatomy/l01-skill-anatomy-thx.md)

## Woran ist erkennbar, dass der Agent selbst gerechnet hat?

- In der Antwort fehlen „Summenkontrolle" und „Sollwert-Prüfung".
- Dann neuen Chat starten und den Skill ausdrücklich nennen.

## Ist eine markierte Auffälligkeit ein Fehler?

- Nicht unbedingt: der 27.11.2025 ist ein echter Großauftrag.
- Der 10.02.2026 dagegen ist ein Kommafehler.

## Funktioniert das mit eigenen Daten?

- Ja, bei einer CSV im Langformat mit Datum und Betrag.
- Anpassen: Spaltenrollen und Datenordner in den Einstellungen.
- Details: [Lab 9.1](../m09-final-project/l01-cost-report/l01-cost-report-thx.md)

## Was gilt rechtlich für KI-Analysen?

- Die EU-KI-Verordnung gilt seit 01.08.2024, Pflichten greifen gestaffelt.
- Datenschutz und interne Freigaben gelten unabhängig davon.
- Details: [Lab 8.1](../m08-validation/l01-fact-check/l01-fact-check-thx.md)

## Lässt sich alles nach dem Kurs wiederholen?

- Ja: Starter, Beispiele und Daten liegen vollständig im Kursordner.
- Daten zurücksetzen: `python project/data/generate_data.py`.
