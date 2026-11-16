---
name: monatsbericht
description: Erstellt den Nordwind-Monatsbericht zum Umsatz (Kennzahlen je Region mit Vormonat, Vorjahr, Plan und Marge, Kundensegmente, auffällige Tage, Prognose) als HTML und Excel mit dem Skript scripts/monatsbericht.py und meldet Summenkontrolle und Sollwert-Prüfung. Verwenden bei Fragen nach Monatsbericht, Umsatzbericht, Umsatz oder Kennzahlen eines Monats, Auffälligkeiten, Umsatzprognose oder einer neuen Nordwind-Umsatzlieferung.
---

# Monatsbericht Umsatz (Nordwind)

Das Skript rechnet, die KI erklärt. Alle Zahlen kommen aus der Ausgabe von `scripts/monatsbericht.py`; nie selbst rechnen, schätzen oder runden.

## Wann verwenden

- Monatsbericht, Umsatzbericht oder Kennzahlen eines Monats, z. B. „Erstelle den Monatsbericht für September 2026.“
- auffällige Tage eines Monats, z. B. „Was ist im September 2026 auffällig?“
- Umsatzprognose für die nächsten Monate
- eine neue Umsatzlieferung in `data/` soll ausgewertet werden

Nicht verwenden für Kosten je Kostenstelle oder für andere Dateien als `data/nordwind_umsatz*.csv`.

## Vorgehen

1. Berichtsmonat als JJJJ-MM bestimmen (September 2026 = `2026-09`). Nennt die Frage keinen eindeutigen Monat, zuerst nachfragen („Für welchen Monat, z. B. 2026-09?“) und nicht raten.
2. Im Wurzelordner des Arbeitsbereichs genau einen dieser Befehle ausführen, `JJJJ-MM` durch den Monat ersetzen:

   Monatsbericht (HTML und Excel):

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat JJJJ-MM --excel
   ```

   Nur die auffälligen Tage:

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py auffaelligkeiten --daten data --monat JJJJ-MM
   ```

   Nur die Prognose der drei Folgemonate:

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py prognose --daten data --monat JJJJ-MM
   ```

3. Beginnt eine Zeile der Ausgabe mit `STOPP:`, diese Zeile wörtlich melden, sagen, dass kein Bericht entstanden ist, und nichts weiter rechnen oder ausführen.

## Antwortformat

1. **Kurzfazit:** 2–3 Sätze zu Gesamtumsatz und Abweichung zu Vormonat, Vorjahr und Plan; nur Zahlen aus der Ausgabe.
2. **Kennzahlentabelle:** die Tabelle aus der Ausgabe als Markdown-Tabelle (Region, Umsatz, Δ Vormonat %, Δ Vorjahr %, Δ Plan %, Marge %). Bei `auffaelligkeiten` oder `prognose` stattdessen deren Tabelle.
3. **Prüfung:** die Zeilen `Summenkontrolle: …` und `Sollwert-Prüfung: …` wörtlich aus der Ausgabe.
4. **Dateien:** Pfade zu `berichte/bericht_JJJJ_MM_v2.html` und `berichte/kpi_JJJJ_MM.xlsx` (nur beim Befehl `bericht`).

## Regeln

- Nur die Befehle aus dem Abschnitt Vorgehen ausführen; keine Dateien ändern, verschieben oder löschen.
- Keine Zahl selbst berechnen; fehlt eine Zahl in der Ausgabe, sagen, dass sie fehlt.
