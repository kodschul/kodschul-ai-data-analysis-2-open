# Lab 2.2 – Übung: Bereinigen und transformieren

**Dauer:** ca. 20 Minuten
**Ändert die Nordwind-Projektbasis?** Ja – es entsteht `umsatz_clean.csv`. Lab 2.3 liest die Fassung aus dem Beispiel, damit eigene Abweichungen nicht weiterwandern.

## Vorbereitung

- Starter: [`project/starters/m02-l02-clean.py`](../../project/starters/m02-l02-clean.py) · Arbeitsdatei: `project/playground/m02-l02-clean.py`
- Ergebnis: `project/playground/umsatz_clean.csv`

## Aufgaben

1. Kopiere den Starter nach `project/playground/` und führe ihn im Terminal aus:

   ```bash
   python project/playground/m02-l02-clean.py
   ```

2. Öffne `project/playground/m02-l02-clean.py`, beginne einen neuen Chat im Modus **Ask** und sende diesen Prompt:

   > Kontext: In #file:m02-l02-clean.py bereinigt die Funktion `clean_umsatz(df)` die Nordwind-Umsätze mit pandas; Schritt 4 fehlt.
   > Spalten: `region` enthält „Nord", „Region Nord", „nord", „Nord " (mit Leerzeichen), „Sued", „süd" und ähnliche Schreibweisen.
   > Regel: Leerzeichen am Rand entfernen, die Vorsilbe „Region " entfernen, erster Buchstabe groß und Rest klein, danach „Sued" durch „Süd" ersetzen. Nur die Spalte `region` ändern, keine Zeile löschen.
   > Gewünschte Ausgabe: nur der Code für Schritt 4 innerhalb der Funktion (vier Leerzeichen eingerückt), der `df["region"]` überschreibt, mit kurzen Kommentaren. Danach gibt es genau Nord, Ost, Süd und West.

3. Prüfe den Vorschlag mit den drei Lesefragen aus Lab 2.1, füge ihn zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` ein, speichere und führe das Skript erneut aus.

## Checkpoint

- Aufgabe 1 meldet `nicht OK  genau 4 Regionen` und listet 14 Schreibweisen.
- Nach Aufgabe 3 meldet die Prüfung dreimal `OK`, `Zeilen nachher: 33156` und `Zeilen ohne Kosten: 648`, gleich dem Beispiel.
- Bei `nicht OK`: Prompt ein zweites Mal senden; danach das Lösungs-Snippet aus der Lösung einfügen.

## Abschlusskriterien

- `project/playground/umsatz_clean.csv` hat 33.156 Zeilen und in `region` nur Nord, Ost, Süd, West.

## Erweiterung

Ergänze in der Funktion `pruefen` mit eigenem Prompt eine Zeile, die den Umsatz der Zeilen ohne Kosten und seinen Anteil am Gesamtumsatz ausgibt, und halte die Regel für fehlende Kosten als Kommentar über Schritt 3 fest (Was passiert mit den Zeilen? Wofür zählen sie, wofür nicht?).

## Fallback

Ohne Copilot: Lösungs-Snippet aus der Lösung einfügen. Fertige Fassung: [`clean.py`](../../project/examples/m02-data-preparation/l02-cleaning/clean.py) mit Ergebnis `umsatz_clean.csv` im selben Ordner.
