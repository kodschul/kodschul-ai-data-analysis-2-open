# Lab 3.1 – Übung: Muster finden: explorative Analyse

**Dauer:** ca. 15 Minuten
**Ändert die Nordwind-Projektbasis?** Ja – drei Ergebnistabellen; Lab 3.2 zeigt sie als Diagramme (aus dem Beispielordner).

## Vorbereitung

- Starter: [`project/starters/m03-l01-eda.ipynb`](../../project/starters/m03-l01-eda.ipynb)
- Arbeitsdatei: `project/playground/m03-l01-eda.ipynb`
- Eingabe: `umsatz_features.csv` aus dem Beispiel von Lab 2.3 (der Starter liest sie von dort)

## Aufgaben

1. Kopiere im Explorer `project/starters/m03-l01-eda.ipynb` nach `project/playground/` (Rechtsklick → **Copy**, Rechtsklick auf `playground` → **Paste**) und öffne die Kopie.
2. Führe die Zellen bis einschließlich **Frage 2** mit **Umschalt+Enter** aus. Öffne über **Variables** in der Notebook-Leiste die Tabelle `wachstum` im Data Viewer und sortiere nach `wachstum_prozent`.
3. Öffne den Chat (**Strg+Alt+I**), wähle **Ask** und sende diesen Prompt. Ersetze in der Zelle unter **Frage 3** die Zeile `kanal_monat = None` durch den Code aus der Antwort (zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1`) und führe die Zelle aus:

   > Kontext: In einem Jupyter-Notebook ist `df` eine pandas-Tabelle mit Umsatzbuchungen eines Großhändlers; pandas ist als `pd` importiert.
   > Spalten: `monat` (Text im Format JJJJ-MM), `kanal` (Außendienst oder Onlineshop), `umsatz` (Euro).
   > Regel: Summiere `umsatz` je Monat und Kanal mit `pivot_table`: Monate als Zeilen, Kanäle als Spalten. Ergänze die Spalte `anteil_online_prozent` = Onlineshop / (Außendienst + Onlineshop) * 100 und runde auf eine Nachkommastelle.
   > Ausgabe: Nur Python-Code für eine Notebook-Zelle, der das Ergebnis in der Variable `kanal_monat` ablegt. Keine Datei lesen oder schreiben, keine Erklärung.

   **Claude Code:** Prompt im Claude-Code-Fenster senden und nur den Code aus der Antwort in die Zelle kopieren.
4. Prüfe den Code mit den drei Lesefragen aus Lab 2.1 und führe dann die **Prüfzelle** aus. Bei „nicht OK" den Hinweis lesen und einmal nachbessern; danach das Lösungs-Snippet aus der Lösung einsetzen.
5. Führe die Zelle **Ergebnisse speichern** aus.

## Checkpoint

- `wachstum` zeigt vier Regionen; West steht oben mit `9.8`.
- `marge` zeigt sechs Produktgruppen, Schreibwaren oben mit `34.8`.
- Die Prüfzelle meldet `OK – 33 Monate, Onlineshop-Anteil im September 2026: 30,1 %`.

## Abschlusskriterien

- Das Notebook läuft ohne Fehler bis zum Ende.
- `project/playground/` enthält `wachstum_region.csv`, `marge_produktgruppe.csv` und `kanal_monat.csv`.

## Erweiterung

Frage Copilot (Ask) nach fünf weiteren Analysefragen an `df` und nenne dabei die Spalten `datum, jahr, kunde_id, region, produktgruppe, kanal, menge, umsatz, deckungsbeitrag, monat`. Beantworte eine der Fragen in einer neuen Zelle am Ende des Notebooks und vergleiche mit der Erweiterung im Beispiel-Notebook [`eda.ipynb`](../../project/examples/m03-exploration/l01-eda/eda.ipynb).

## Fallback

- Kein Chat verfügbar: Lösungs-Snippet aus der Lösung einsetzen.
- Notebook verloren: Starter erneut kopieren oder mit dem Beispiel [`eda.ipynb`](../../project/examples/m03-exploration/l01-eda/eda.ipynb) weiterarbeiten; Lab 3.2 liest ohnehin die Tabellen aus dem Beispielordner.
