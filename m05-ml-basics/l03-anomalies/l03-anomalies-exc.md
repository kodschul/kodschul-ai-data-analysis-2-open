# Lab 5.3 – Übung: Auffälligkeiten erkennen

**Dauer:** ca. 12 Minuten
**Ändert die Nordwind-Projektbasis?** Ja — es entsteht die Funktion `find_anomalies(df, schwelle=3)`; der Bericht v2 (Lab 6.2) enthält dieselbe Regel.
**Arbeitsdatei:** `project/playground/m05-l03-auffaelligkeiten.ipynb`
**Starter:** `project/starters/m05-l03-auffaelligkeiten.ipynb` · **Beispiel:** `project/examples/m05-ml-basics/l03-anomalies/auffaelligkeiten.ipynb`

## Vorbereitung

- Das Notebook liest `umsatz_features.csv` aus dem Beispiel von Lab 2.3.
- Tagesumsatz je Region, Mittelwert und Standardabweichung je Region und Monat sind fertig; offen ist die Funktion mit der Markierung „auffällig“.

## Aufgaben

1. Kopiere `project/starters/m05-l03-auffaelligkeiten.ipynb` nach `project/playground/` und öffne die Kopie.
2. Führe die Zellen bis einschließlich Schritt 1 aus. Die Tabelle zeigt Region West im November 2025: Am 27.11. liegt der Tagesumsatz bei 25.329 € bei einem Monatsmittel von 5.517 €.
3. Fülle die Zelle mit `AUFGABE 1` mit Copilot (Chat, Modus Ask, Notebook mit `#file` anhängen) und diesem Prompt, übernimm den Code zwischen die Markierungen und führe die Zelle und die Prüfzelle aus:

   > Im Notebook gibt es die pandas-Tabelle `tage` mit den Spalten `datum`, `region`, `umsatz` (Tagesumsatz), `mittel` (Ø Tagesumsatz der Region im selben Monat) und `streuung` (Standardabweichung dazu). Schreibe eine Funktion `find_anomalies(df, schwelle=3)`, die eine Kopie von `df` mit zwei neuen Spalten zurückgibt: `abstand` = (umsatz − mittel) / streuung und `auffaellig` = True, wenn der Betrag von `abstand` größer als `schwelle` ist, sonst False. Gib nur die Funktion für eine Notebook-Zelle aus, ohne Aufruf und ohne Beispieldaten.

   **Claude Code:** Prompt im Claude-Code-Panel senden, das Notebook mit `@` nennen, Code aus der Antwort zwischen die Markierungen kopieren.
4. Meldet die Prüfzelle `nicht OK`, lies den Hinweis und versuche es ein zweites Mal; sonst setze das Lösungs-Snippet aus der Lösung ein.
5. Führe Schritt 3 aus. Ziehe im Diagramm mit der Maus einen Rahmen um November 2025 bis Februar 2026, um hineinzuzoomen (Doppelklick zoomt zurück), und suche die beiden hohen Spitzen mit roten Kreisen. Die Liste darunter wird als `project/playground/auffaellige_tage.csv` gespeichert.

## Checkpoint

- Die Prüfzelle meldet `OK – 11 auffällige Tage bei Schwelle 3, darunter 27.11.2025 West und 10.02.2026 Ost`.
- Die Liste in Schritt 3 hat 11 Zeilen; oben stehen 10.02.2026 Ost (Abstand 4,2) und 27.11.2025 West (4,1).

## Abschlusskriterien

- `find_anomalies(tage, schwelle=3)` liefert die Spalten `abstand` und `auffaellig`.
- Diagramm mit roten Kreisen und `auffaellige_tage.csv` liegen vor.

## Erweiterung

Lass Copilot die leere Zelle unter **Erweiterung** füllen und vergleiche die Schwellen:

> Im Notebook gibt es die Tabelle `tage` und die Funktion `find_anomalies(df, schwelle)`, die eine Spalte `auffaellig` (True/False) ergänzt. Dokumentiert sind genau zwei echte Auffälligkeiten: 2025-11-27 Region West und 2026-02-10 Region Ost (Spalten `datum` und `region`). Schreibe eine Schleife über die Schwellen 2, 3 und 4, die je Schwelle ausgibt: Anzahl auffälliger Tage, davon dokumentiert, Anzahl Fehlalarme (= auffällig, aber nicht dokumentiert).

## Fallback

Läuft die eigene Kopie nicht: Starter erneut kopieren oder im Beispiel `auffaelligkeiten.ipynb` weiterarbeiten.
