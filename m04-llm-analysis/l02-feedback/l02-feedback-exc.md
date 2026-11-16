# Lab 4.2 – Übung: Kundenfeedback auswerten

**Dauer:** ca. 20 Minuten
**Ändert die Nordwind-Projektbasis?** Ja – `feedback_klassifiziert.csv` und ein Themendiagramm entstehen; der Monatsbericht bleibt unverändert.

## Vorbereitung

- Starter: [`project/starters/m04-l02-feedback.ipynb`](../../project/starters/m04-l02-feedback.ipynb)
- Arbeitsdatei: `project/playground/m04-l02-feedback.ipynb`
- Eingabe: `data/nordwind_feedback.csv`; Schlüssel wie in Lab 4.1

## Aufgaben

1. Kopiere den Starter nach `project/playground/`, öffne die Kopie und führe die Zellen bis einschließlich **Grenze der Stichwortregeln** aus. Die erste Zelle meldet, ob das Sprachmodell oder die Stichwortregeln einordnen.
2. Führe die Zelle **50 Kommentare einordnen** aus und prüfe in der Ausgabe die Spalte `methode`.
3. Führe die Zelle mit `gelabelt` aus. Sende dann im Chat (**Ask**) diesen Prompt, ersetze die zwei `None`-Zeilen zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` durch den Code aus der Antwort, führe die Zelle und danach die Prüfzelle aus:

   > Kontext: In einem Jupyter-Notebook ist `gelabelt` eine pandas-Tabelle mit 20 Kundenkommentaren, die ein Mensch eingeordnet hat; daneben steht die Einordnung durch die Funktion `classify()`.
   > Spalten: `thema` und `stimmung` (von `classify()`), `thema_label` und `stimmung_label` (von Hand).
   > Regel: Trefferquote = Anteil der Zeilen, in denen `thema` gleich `thema_label` ist, als Zahl zwischen 0 und 1; genauso für `stimmung` und `stimmung_label`.
   > Ausgabe: Nur Python-Code für eine Notebook-Zelle, der die Variablen `treffer_thema` und `treffer_stimmung` setzt und beide in Prozent ausgibt. Keine Erklärung.

4. Führe die Zellen **Themen zählen und zeigen** und **Ergebnis speichern** aus.
5. Lege am Ende eine neue Zelle an und zeige die Kommentare, die keinem Thema zugeordnet wurden: `kommentare[kommentare["thema"] == "unklar"]`. Den Wert `unklar` vergeben nur die Stichwortregeln; mit Sprachmodell bleibt die Tabelle leer, solange das Modell nur die erlaubten Werte verwendet.

## Checkpoint

- Die Ausgabe von Aufgabe 2 zeigt `Sprachmodell 50` (mit Schlüssel) oder `Stichwortregeln 50` (ohne).
- Die Prüfzelle meldet für beide Quoten `OK – … von 20 gleich`.
- Der Titel des Themendiagramms nennt die Methode der Einordnung.

## Abschlusskriterien

- `project/playground/` enthält `feedback_klassifiziert.csv` (50 Zeilen, Spalten `stimmung`, `thema`, `methode`) und `diagramm_themen.html`.
- Die Trefferquoten für Thema und Stimmung stehen im Notebook.

## Erweiterung

Lege in einer neuen Zelle `PROMPT2` an: derselbe Text plus zwei Regeln, z. B. „Bei Wartezeit, auch mit ‚endlich', ist die Stimmung negativ." und „Produktmängel (kaputt, schreibt nicht) gehören zu Qualität." Ordne die 50 Kommentare mit `classify(text, prompt=PROMPT2)` erneut ein und miss die Trefferquote noch einmal. Ohne Schlüssel bleibt das Ergebnis gleich, weil die Stichwortregeln den Prompt nicht verwenden.

## Fallback

- Ohne Schlüssel oder bei Störung ordnen die Stichwortregeln ein; alle Aufgaben außer der Erweiterung laufen genauso. Ergebnisse dann immer als „per Stichwortregeln" bezeichnen, nie als KI-Ergebnis.
- Notebook verloren: Starter neu kopieren oder das Beispiel [`feedback.ipynb`](../../project/examples/m04-llm-analysis/l02-feedback/feedback.ipynb) öffnen.
