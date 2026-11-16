# Lab 5.2 – Übung: Kundensegmente mit Clustering

**Dauer:** ca. 20 Minuten
**Ändert die Nordwind-Projektbasis?** Ja — es entstehen `kunden_segmente.csv` und `segmente.html`; der Bericht v2 (Lab 6.2) rechnet die Segmente selbst nach derselben Methode.
**Arbeitsdatei:** `project/playground/m05-l02-segmente.ipynb`
**Starter:** `project/starters/m05-l02-segmente.ipynb` · **Beispiel:** `project/examples/m05-ml-basics/l02-clustering/segmente.ipynb`

## Vorbereitung

- Das Notebook liest `kunden_rfm.csv` aus dem Beispiel von Lab 2.3 (`project/examples/m02-data-preparation/l03-features/`).
- Skalieren, k-Means, Segmenttabelle und Streudiagramm sind fertig; offen ist nur die Spalte `segment_name`.

## Aufgaben

1. Kopiere `project/starters/m05-l02-segmente.ipynb` nach `project/playground/` und öffne die Kopie.
2. Führe die Zellen bis einschließlich Schritt 3 aus. Lies in der Segmenttabelle je Segment die Anzahl Kunden, Ø Tage seit Kauf, Ø Buchungen und Ø Umsatz ab und fahre im Streudiagramm mit der Maus über einzelne Punkte.
3. Fülle die Zelle mit `AUFGABE 1` mit Copilot (Chat, Modus Ask, Notebook mit `#file` anhängen) und diesem Prompt. Übernimm den Code zwischen die Markierungen `>>>` und `<<<`, führe die Zelle und danach die Prüfzelle aus:

   > Im Notebook gibt es die pandas-Tabelle `kunden` mit der Spalte `segment` (ganze Zahlen 1 bis 4). Laut Segmenttabelle: Segment 1 = wenige Kunden, sehr viele Buchungen, höchster Umsatz; Segment 2 = kaufen laufend, mittlerer Umsatz; Segment 3 = letzter Kauf im Schnitt vor rund 300 Tagen; Segment 4 = aktiv, aber wenige Buchungen und kleiner Umsatz. Ergänze eine Spalte `segment_name` mit je einem kurzen deutschen Namen pro Segment, zum Beispiel „Top-Kunden“, „Stammkunden“, „Abgesprungen“, „Gelegenheitskunden“. Nutze ein dict und `map`. Gib nur den Code für eine Notebook-Zelle aus, ohne die Tabelle neu zu laden.

   **Claude Code:** Prompt im Claude-Code-Panel senden, das Notebook mit `@` nennen, Code aus der Antwort zwischen die Markierungen kopieren.
4. Meldet die Prüfzelle `nicht OK`, lies den Hinweis und versuche es ein zweites Mal; sonst setze das Lösungs-Snippet aus der Lösung ein.
5. Führe die Zelle unter **Ergebnis speichern** aus. Öffne `project/playground/kunden_segmente.csv` im Editor und `project/playground/segmente.html` im Browser (Rechtsklick **Reveal in Finder** bzw. **Reveal in File Explorer**, dann Doppelklick).

## Checkpoint

- Schritt 2 zeigt die Segmentgrößen 14, 90, 55 und 241 (Segment 1 bis 4).
- Die Prüfzelle meldet `OK – 1 = …, 2 = …, 3 = …, 4 = …`.
- `kunden_segmente.csv` hat 400 Zeilen und die Spalten `kunde_id, tage_seit_kauf, haeufigkeit, umsatz, segment, segment_name`.

## Abschlusskriterien

- `kunden_segmente.csv` und `segmente.html` liegen in `project/playground/`.
- Die Segmenttabelle am Ende des Notebooks zeigt je Segment einen Namen.

## Erweiterung

Führe die Zelle unter **Erweiterung: Elbow-Diagramm** aus. Setze danach in Schritt 2 `ANZAHL_SEGMENTE = 3` (danach `5`), wähle in dieser Zelle **Execute Cell and Below** und vergleiche die Segmenttabelle mit der Lösung für 4 Segmente. Die Namen aus Aufgabe 3 passen dann nicht mehr zu den Segmenten (bei 5 Segmenten meldet die Prüfzelle `nicht OK`). Zum Schluss `ANZAHL_SEGMENTE = 4` zurücksetzen und erneut **Execute Cell and Below** wählen, damit `kunden_segmente.csv` wieder 4 Segmente enthält.

## Fallback

Läuft die eigene Kopie nicht: Starter erneut kopieren oder im Beispiel `segmente.ipynb` weiterarbeiten. Die nächsten Labs brauchen die eigene `kunden_segmente.csv` nicht.
