# Lab 7.3 – Übung: Neue Daten, gleicher Bericht

**Dauer:** ca. 20 Minuten
**Ändert die Nordwind-Projektbasis?** Ja — `data/` enthält danach die Oktober-Lieferung; Lab 8.1 prüft einen Kommentar zum Oktober-Bericht.
**Arbeitsdatei:** keine (Skill `.github/skills/monatsbericht/` aus Lab 7.2)
**Starter:** keiner · **Beispiel:** `project/examples/m07-analysis-skill/l03-new-delivery/` (Oktober-Bericht, Excel, `stopp_meldung.txt`)

## Vorbereitung

- Der Skill `monatsbericht` aus Lab 7.2 läuft. Fehlt er: Lab 7.2, Aufgabe 1, mit `SKILL.md` aus `project/examples/m07-analysis-skill/l02-report-skill/monatsbericht/` ausführen.
- In `lieferungen/` liegen `nordwind_umsatz_2026_10.csv`, `nordwind_umsatz_2026_10_defekt.csv` und `kostenstellen.csv`.
- Dateien verschieben: im Explorer mit der Maus auf den Zielordner ziehen und **Move** bestätigen.

## Aufgaben

1. Verschiebe `lieferungen/nordwind_umsatz_2026_10.csv` nach `data/`.
2. Beginne einen neuen Chat im Modus **Agent** und sende „Erstelle den Monatsbericht für Oktober 2026.“ Erlaube nur den Befehl aus `SKILL.md`. Lies in der Antwort die Zeilen `Summenkontrolle` und `Sollwert-Prüfung` und öffne `berichte/bericht_2026_10_v2.html` im Browser.
3. Tausche die Lieferung aus: Verschiebe `data/nordwind_umsatz_2026_10.csv` zurück nach `lieferungen/` und danach `lieferungen/nordwind_umsatz_2026_10_defekt.csv` nach `data/`.
4. Beginne einen neuen Chat und sende denselben Satz wie in Aufgabe 2. Erlaube den Befehl. Die Antwort meldet den Stopp des Skripts statt eines Berichts.
5. Lege die richtige Datei zurück: `data/nordwind_umsatz_2026_10_defekt.csv` nach `lieferungen/`, `lieferungen/nordwind_umsatz_2026_10.csv` nach `data/`. Bestätige im Terminal (Skill-Regel 4), dass der Oktober-Bericht wieder entsteht:

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat 2026-10 --excel
   ```

## Checkpoint

- Aufgabe 2 und 5 enden mit:

  ```text
  Summenkontrolle: 2026-10 – 1.111 Zeilen, Summe Umsatz 337.139,00 – stimmt mit der Kennzahlentabelle überein
  Sollwert-Prüfung: bestanden (12 Werte für 2026-10 gegen kontrollsummen.csv)
  ```

- Aufgabe 4: Die Antwort enthält `STOPP: Pflichtspalte umsatz fehlt in nordwind_umsatz_2026_10_defekt.csv`, keine Kennzahlentabelle und keine Oktober-Zahlen.

## Abschlusskriterien

- `berichte/bericht_2026_10_v2.html` und `berichte/kpi_2026_10.xlsx` mit bestandener Sollwert-Prüfung.
- Eine Stopp-Meldung im Chat, die Spalte und Datei nennt.
- `data/` enthält am Ende `nordwind_umsatz_2026_10.csv`, `lieferungen/` die defekte Datei.

## Erweiterung

Ergänze in `.github/skills/monatsbericht/SKILL.md`, Vorgehen Schritt 3, eine Rückfrage, die der Agent nach einem Stopp stellt (z. B. ob eine korrigierte Lieferung angefordert werden soll). Wiederhole Aufgabe 3 bis 5 und vergleiche die Antwort mit dem Beispiel in der Lösung.

## Fallback

- KI-Assistent nicht verfügbar: Befehl aus Aufgabe 5 nach Aufgabe 1 und nach Aufgabe 3 im Terminal ausführen; die Ausgaben stehen in der Lösung und in `project/examples/m07-analysis-skill/l03-new-delivery/stopp_meldung.txt`.
- Dateien durcheinander: Ziel ist `data/` mit `nordwind_umsatz.csv`, `nordwind_umsatz_2026_10.csv`, `kontrollsummen.csv`, `nordwind_plan_2026.csv`, `nordwind_feedback.csv` und `lieferungen/` mit `nordwind_umsatz_2026_10_defekt.csv` und `kostenstellen.csv`.
