# Lab 3.2 – Übung: Diagramme, die eine Aussage haben

**Dauer:** ca. 20 Minuten
**Ändert die Nordwind-Projektbasis?** Ja – drei Diagramme als HTML; Lab 3.3 übernimmt die Diagramm-Funktionen in `monatsbericht.py`.

## Vorbereitung

- Starter: [`project/starters/m03-l02-diagramme.ipynb`](../../project/starters/m03-l02-diagramme.ipynb)
- Arbeitsdatei: `project/playground/m03-l02-diagramme.ipynb`
- Eingabe: die drei Tabellen aus dem Beispiel von Lab 3.1 (`project/examples/m03-exploration/l01-eda/`), der Starter liest sie von dort

## Aufgaben

1. Kopiere `project/starters/m03-l02-diagramme.ipynb` nach `project/playground/`, öffne die Kopie und führe die Zellen bis einschließlich **Diagramm 1** aus. Fahre mit der Maus über die Linien und blende per Klick auf die Legende einen Kanal aus.
2. Sende im Chat (**Ask**) diesen Prompt, ersetze `fig2 = None` zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` durch den Code aus der Antwort, führe die Zelle und danach die Prüfzelle aus:

   > Kontext: In einem Jupyter-Notebook ist `marge` eine pandas-Tabelle mit der Marge je Produktgruppe; plotly express ist als `px` importiert.
   > Spalten: `produktgruppe` (Text), `marge_prozent` (Zahl, bereits in Prozent).
   > Regel: Balkendiagramm mit `px.bar`, ein Balken je Produktgruppe, der Wert als Beschriftung auf dem Balken, deutsche Achsentitel. Der Titel nennt den Befund in einem Satz: welche Produktgruppe die höchste und welche die niedrigste Marge hat, jeweils mit Wert.
   > Ausgabe: Nur Python-Code für eine Notebook-Zelle, Ergebnis in der Variable `fig2`. Nichts speichern, keine Erklärung.

3. Schreibe im Chat (**Ask**) einen eigenen Prompt nach dem Muster **Kontext + Spalten + Regel + Ausgabe** für ein Balkendiagramm der Tabelle `wachstum` (Ausgabe der ersten Code-Zelle; Spalten `region` und `wachstum_prozent` = Veränderung Januar–September 2026 zum Vorjahr in %). Der Titel soll den Befund mit Werten nennen, das Ergebnis in der Variable `fig3` landen. Setze den Code zwischen `# >>> AUFGABE 2` und `# <<< ENDE AUFGABE 2` ein und führe die Prüfzelle aus.
4. Führe die Zelle **Als HTML speichern** aus und öffne `project/playground/diagramm_wachstum.html` im Browser (Rechtsklick auf die Datei → **Reveal in File Explorer** bzw. **Reveal in Finder**, dann Doppelklick).

## Checkpoint

- Beide Prüfzellen melden `OK` mit den Spalten des Diagramms und dem Titel.
- Der Titel von `fig3` nennt Regionen und Prozentwerte, nicht nur „Wachstum je Region".

## Abschlusskriterien

- `project/playground/` enthält `diagramm_kanal.html`, `diagramm_marge.html` und `diagramm_wachstum.html`; jede Datei zeigt im Browser ein interaktives Diagramm.

## Erweiterung

Erzeuge mit eigenem Prompt in einer neuen Zelle ein Abweichungsdiagramm **Ist gegen Plan** je Region für Januar bis September 2026. Ist: `umsatz` aus `project/examples/m02-data-preparation/l03-features/umsatz_features.csv` (Spalten `monat`, `region`), Plan: `plan_umsatz` aus `data/nordwind_plan_2026.csv` (Spalten `monat`, `region`). Abweichung in % = (Ist − Plan) / Plan × 100. Vergleiche mit der Erweiterung im Beispiel [`diagramme.ipynb`](../../project/examples/m03-exploration/l02-charts/diagramme.ipynb).

## Fallback

- Kein Chat verfügbar: Lösungs-Snippets aus der Lösung einsetzen; den Beispiel-Prompt für `fig3` später im Chat ausprobieren.
- Browser zeigt eine leere Seite: Internet fehlt (plotly kommt per `cdn`); das Diagramm im Notebook genügt, oder in der Speicherzelle `include_plotlyjs=True` setzen.
