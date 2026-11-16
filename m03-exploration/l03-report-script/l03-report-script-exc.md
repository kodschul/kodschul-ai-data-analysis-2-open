# Lab 3.3 – Übung: Der Monatsbericht als Skript

**Dauer:** ca. 25 Minuten
**Ändert die Nordwind-Projektbasis?** Ja – `monatsbericht.py` v1 entsteht; in Lab 6.2 folgt v2.

## Vorbereitung

- Starter: [`project/starters/m03-l03-monatsbericht.py`](../../project/starters/m03-l03-monatsbericht.py)
- Arbeitsdatei: `project/playground/monatsbericht.py` (beim Kopieren umbenennen)
- Eingabe: `data/nordwind_umsatz.csv` (Rohdaten) und `data/nordwind_plan_2026.csv`
- Terminal im Kursordner (Lab 1.1)

## Aufgaben

1. Kopiere `project/starters/m03-l03-monatsbericht.py` nach `project/playground/` und benenne die Kopie in `monatsbericht.py` um (Rechtsklick → **Rename**). Führe sie einmal aus und lies die Meldung der eingebauten Prüfung:

   ```bash
   python project/playground/monatsbericht.py data/nordwind_umsatz.csv --monat 2026-09
   ```

2. Öffne `project/playground/monatsbericht.py`, suche in `main()` die Stelle `# >>> AUFGABE 1` und sende im Chat (**Ask**) diesen Prompt (`#file:` über `#` aus der Liste wählen). Füge die drei Zeilen aus der Antwort zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` ein und speichere:

   > Kontext: In #file:monatsbericht.py fehlen in `main()` zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` drei Zeilen. Alle Funktionen stehen schon in der Datei.
   > Variablen: `roh` = Rohdaten aus der CSV, `plan` = Plantabelle, `args.monat` = Berichtsmonat als Text JJJJ-MM.
   > Regel: Rufe nacheinander auf: `clean_umsatz(roh)` ergibt `sauber`, `add_features(sauber)` ergibt `df`, `kpi_tabelle(df, args.monat, plan)` ergibt `kpi`. Ändere keine andere Zeile.
   > Ausgabe: Nur die drei Zeilen Python-Code mit vier Leerzeichen Einrückung, keine Erklärung.

   **Claude Code:** Prompt mit `@project/playground/monatsbericht.py` statt `#file:` senden; eine vorgeschlagene Änderung an der Datei nur annehmen, wenn sie genau diese drei Zeilen betrifft.
3. Führe den Befehl aus Aufgabe 1 erneut aus. Die eingebaute Prüfung meldet `OK`. Bei „nicht OK" den Hinweis lesen, einmal nachbessern, danach das Lösungs-Snippet aus der Lösung einsetzen.
4. Öffne `project/playground/bericht_2026_09.html` im Browser und prüfe die KPI-Tabelle dann gegen die Sollwerte:

   ```bash
   python check_zahlen.py project/playground/kpi_2026_09.csv
   ```

5. Erzeuge mit demselben Skript den Bericht für August 2026 (`--monat 2026-08`) und prüfe auch diese KPI-Tabelle mit `check_zahlen.py`.

## Checkpoint

- Nach Aufgabe 1: `nicht OK – sauber fehlt …`, keine Dateien entstehen.
- Nach Aufgabe 3: `OK – 4 Regionen, Summe der Regionen = Umsatz aller Buchungen im Monat (343.382 €)` und zwei `Gespeichert:`-Zeilen.
- `check_zahlen.py` meldet `0 Abweichungen – Prüfung bestanden`.

## Abschlusskriterien

- `project/playground/` enthält `bericht_2026_09.html`, `kpi_2026_09.csv`, `bericht_2026_08.html` und `kpi_2026_08.csv`.
- Beide KPI-Tabellen bestehen die Prüfung.

## Erweiterung

Ergänze mit eigenem Prompt in `kpi_tabelle` die Spalte `plan_abweichung_prozent` = (umsatz − plan) / plan × 100, gerundet auf eine Nachkommastelle, und zeige sie im HTML als zusätzliche Spalte **Abw. Plan**. Führe danach `check_zahlen.py` erneut aus: Die Prüfung muss weiterhin bestehen.

## Fallback

- Kein Chat verfügbar: Lösungs-Snippet aus der Lösung einsetzen.
- Skript verloren oder unrettbar: das Beispiel ausführen, es erzeugt dieselben Dateien im Beispielordner:

  ```bash
  python project/examples/m03-exploration/l03-report-script/monatsbericht.py data/nordwind_umsatz.csv --monat 2026-09
  ```
