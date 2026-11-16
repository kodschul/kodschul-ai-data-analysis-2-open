# Lab 6.2 – Übung: Der Bericht v2 mit Excel-Export

**Dauer:** ca. 35 Minuten (inkl. 5 Minuten Abschlussrunde)
**Ändert die Nordwind-Projektbasis?** Ja — v2 ist der Stand, den Lab 7.2 als Skill verpackt; dort wird die Beispiel-Fassung kopiert, nicht die eigene.
**Arbeitsdatei:** `project/playground/m06-l02-monatsbericht.py`
**Starter:** `project/starters/m06-l02-monatsbericht.py` · **Beispiel:** `project/examples/m06-forecast-report/l02-report-v2/monatsbericht.py`

## Vorbereitung

- Terminal in VS Code (**Terminal → New Terminal**) im Kursordner; die Befehle unten werden dort eingegeben.
- `data/` enthält `nordwind_umsatz.csv`, `kontrollsummen.csv` und `nordwind_plan_2026.csv` (Startbestand). `lieferungen/` bleibt unverändert.
- Der Starter ist das vollständige v2 mit einer Lücke: Die Funktion `export_excel` ist leer.

## Aufgaben

1. Kopiere `project/starters/m06-l02-monatsbericht.py` nach `project/playground/` (Name bleibt). Führe im Terminal aus und lies die Liste der Befehle und Optionen:

   ```bash
   python project/playground/m06-l02-monatsbericht.py --help
   python project/playground/m06-l02-monatsbericht.py bericht --help
   ```

2. Erzeuge den Bericht für September 2026 und öffne `berichte/bericht_2026_09_v2.html` im Browser (im Explorer Rechtsklick auf die Datei → **Reveal in Finder** bzw. **Reveal in File Explorer**, dann Doppelklick). Suche die Prüfzeilen oben und die neuen Abschnitte Kundensegmente, Auffälligkeiten und Prognose.

   ```bash
   python project/playground/m06-l02-monatsbericht.py bericht --daten data --monat 2026-09
   ```

3. Führe denselben Befehl mit `--excel` am Ende aus. Die eingebaute Prüfung meldet `nicht OK`, weil `export_excel` noch keine Datei schreibt.
4. Öffne `project/playground/m06-l02-monatsbericht.py`, suche `AUFGABE 1` in der Funktion `export_excel` und lass Copilot (Chat, Modus Ask, Datei mit `#file` anhängen) den Rumpf mit diesem Prompt schreiben. Übernimm die Zeilen zwischen die Markierungen (Einrückung: vier Leerzeichen wie die Kommentarzeilen), speichere und führe den Befehl aus Aufgabe 3 erneut aus:

   > In der Datei `m06-l02-monatsbericht.py` ist die Funktion `export_excel(kpi, auffaellige, pfad)` leer. `kpi` ist eine pandas-Tabelle mit den Kennzahlen je Region (Index = Region, Spalten wie Umsatz, Vormonat, Marge %), `pfad` ist der Dateiname der Excel-Datei. Schreibe den Rumpf der Funktion: Speichere `kpi` mit pandas als Blatt „Kennzahlen“ in die Datei `pfad`, mit Index, damit die Region als erste Spalte erscheint. `auffaellige` wird hier nicht gebraucht. Gib nur die Zeilen des Funktionsrumpfs aus und ändere nichts anderes in der Datei.

   **Claude Code:** Prompt im Claude-Code-Panel senden und die Datei mit `@` nennen; schlägt Claude Code eine Änderung direkt in der Datei vor, nur die Zeilen in `export_excel` übernehmen.
5. Meldet die Prüfung `nicht OK`, lies den Hinweis und versuche es ein zweites Mal; sonst setze das Lösungs-Snippet aus der Lösung ein. Öffne danach `berichte/kpi_2026_09.xlsx` in Excel oder LibreOffice Calc (nur ansehen, vor dem nächsten Lauf wieder schließen).

## Checkpoint

- Nach Aufgabe 2 enden die Ausgabe im Terminal und der Kasten „Prüfung“ im HTML mit:

  ```text
  Summenkontrolle: 2026-09 – 1.144 Zeilen, Summe Umsatz 343.381,74 – stimmt mit der Kennzahlentabelle überein
  Sollwert-Prüfung: bestanden (12 Werte für 2026-09 gegen kontrollsummen.csv)
  ```

- Nach Aufgabe 5 meldet die Prüfung `OK – berichte/kpi_2026_09.xlsx mit 5 Zeilen im Blatt 'Kennzahlen' …`.

## Abschlusskriterien

- `berichte/bericht_2026_09_v2.html` mit bestandener Sollwert-Prüfung.
- `berichte/kpi_2026_09.xlsx` mit dem Blatt „Kennzahlen“: Nord, Ost, Süd, West und Gesamt.

## Erweiterung

1. Rufe nur die Auffälligkeiten mit einer niedrigeren Schwelle auf und vergleiche mit Schwelle 3:

   ```bash
   python project/playground/m06-l02-monatsbericht.py auffaelligkeiten --daten data --monat 2026-09 --schwelle 2
   ```

2. Erweitere `export_excel` mit eigenem Prompt so, dass die Tabelle `auffaellige` als zweites Blatt „Auffaelligkeiten“ (ohne Index) in dieselbe Datei geschrieben wird, und vergleiche mit dem Beispiel.

## Fallback

- Copilot nicht verfügbar: Lösungs-Snippet aus der Lösung einsetzen.
- Eigene Datei kaputt: Starter erneut kopieren oder das Beispiel ausführen (`python project/examples/m06-forecast-report/l02-report-v2/monatsbericht.py bericht --daten data --monat 2026-09 --excel`); fertige Ausgaben liegen in `project/examples/m06-forecast-report/l02-report-v2/berichte/`.
- Weder Excel noch LibreOffice vorhanden: Die eingebaute Prüfung bestätigt Blatt und Zeilenzahl; der Inhalt entspricht der Kennzahlentabelle im HTML.
