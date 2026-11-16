---
name: kostenbericht
description: Erstellt den Monatsbericht Kosten je Kostenstelle (Vertrieb, Marketing, IT, Fuhrpark, Gebäude, Personalentwicklung) mit Vormonat, Vorjahr, auffälligen Tagen und Prognose aus data_kosten/kostenstellen.csv mit dem Skript scripts/monatsbericht.py und meldet Summenkontrolle und Sollwert-Prüfung. Verwenden bei Fragen nach Kosten, Kostenbericht, Kostenstelle oder Kosten je Kostenstelle eines Monats.
---

# Kosten je Kostenstelle

Das Skript rechnet, die KI erklärt. Alle Zahlen kommen aus der Ausgabe von `scripts/monatsbericht.py`; nie selbst rechnen, schätzen oder runden.

## Wann verwenden

- Kostenbericht oder Kosten je Kostenstelle eines Monats, z. B. „Erstelle den Kostenbericht je Kostenstelle für September 2026.“
- auffällige Buchungstage einer Kostenstelle, z. B. „Welche Kosten waren im September 2026 auffällig?“
- Kostenprognose für die nächsten Monate

Nicht verwenden für Umsatz, Umsatzbericht oder die Nordwind-Umsatzdateien in `data/`.

## Vorgehen

1. Berichtsmonat als JJJJ-MM bestimmen (September 2026 = `2026-09`). Nennt die Frage keinen eindeutigen Monat, zuerst nachfragen („Für welchen Monat, z. B. 2026-09?“) und nicht raten.
2. Im Wurzelordner des Arbeitsbereichs genau einen dieser Befehle ausführen, `JJJJ-MM` durch den Monat ersetzen:

   Kostenbericht (HTML und Excel):

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py bericht --daten data_kosten --monat JJJJ-MM --excel
   ```

   Nur die auffälligen Tage:

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py auffaelligkeiten --daten data_kosten --monat JJJJ-MM
   ```

   Nur die Prognose der drei Folgemonate:

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py prognose --daten data_kosten --monat JJJJ-MM
   ```

3. Beginnt eine Zeile der Ausgabe mit `STOPP:`, diese Zeile wörtlich melden, sagen, dass kein Bericht entstanden ist, und nichts weiter rechnen oder ausführen.

## Antwortformat

1. **Kurzfazit:** 2–3 Sätze zu den Gesamtkosten und der Abweichung zu Vormonat und Vorjahr; nur Zahlen aus der Ausgabe.
2. **Kennzahlentabelle:** die Tabelle aus der Ausgabe als Markdown-Tabelle (Kostenstelle, Kosten, Δ Vormonat %, Δ Vorjahr %). Bei `auffaelligkeiten` oder `prognose` stattdessen deren Tabelle.
3. **Prüfung:** die Zeilen `Summenkontrolle: …` und `Sollwert-Prüfung: …` wörtlich aus der Ausgabe.
4. **Dateien:** Pfade zu `berichte/kosten/bericht_JJJJ_MM_v2.html` und `berichte/kosten/kpi_JJJJ_MM.xlsx` (nur beim Befehl `bericht`).

## Regeln

- Nur die Befehle aus dem Abschnitt Vorgehen ausführen; keine Dateien ändern, verschieben oder löschen.
- Keine Zahl selbst berechnen; fehlt eine Zahl in der Ausgabe, sagen, dass sie fehlt.
