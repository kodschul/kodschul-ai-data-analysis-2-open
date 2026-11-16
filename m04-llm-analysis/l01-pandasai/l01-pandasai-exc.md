# Lab 4.1 – Übung: PandasAI: fragen, prüfen, verbessern

**Dauer:** ca. 45 Minuten (Einstieg 5, Arbeitsphase 1: 15, Arbeitsphase 2: 20, Debrief 5)
**Ändert die Nordwind-Projektbasis?** Nein – PandasAI ist ein Werkzeug für Einmalfragen; der Bericht bleibt das Skript aus Lab 3.3.

## Vorbereitung

- Starter: [`project/starters/m04-l01-pandasai.ipynb`](../../project/starters/m04-l01-pandasai.ipynb)
- Arbeitsdatei: `project/playground/m04-l01-pandasai.ipynb`
- Eingabe: `umsatz_features.csv` aus dem Beispiel von Lab 2.3, Sollwerte aus `data/kontrollsummen.csv`
- Umgebungsvariable `OPENAI_API_KEY` ist gesetzt (`python check_setup.py --llm` meldet `OK` beim Sprachmodell)

## Aufgaben

1. Kopiere den Starter nach `project/playground/`, öffne die Kopie und führe die Zellen bis einschließlich **Testfrage** aus. Lies unter `Erzeugter Code` die SQL-Abfrage.
2. Arbeitsphase 1: Führe die vier Fragezellen aus (`a1` bis `a4`, `a4` ist die Diagrammfrage). Prüfe bei jeder Antwort den Code mit den drei Lesefragen und vergleiche die Zahlen mit der Zelle **Gegenprobe mit pandas**.
3. Arbeitsphase 2, Vorher: Führe die Zelle **Prüfhilfe**, die Zelle **Vorher** und deren **Prüfzelle** aus. Die Vergleichstabelle zeigt Sollwert und Vorher-Zeile.
4. Arbeitsphase 2, Nachher: Führe die Zelle **Spaltenbeschreibungen einsetzen** aus, dann die Zelle **Nachher** und deren **Prüfzelle**. Vergleiche in der Tabelle Vorher- und Nachher-Zeile mit dem Sollwert und suche im Code von Vorher und Nachher nach `AVG` und `SUM`.

## Checkpoint

- Nach Arbeitsphase 1: vier Antworten mit Code, darunter ein Diagramm; die Zahlen von `a1` bis `a3` stimmen mit der Gegenprobe überein oder die Abweichung ist im Code gefunden (Filter, Spalte, Rechenart).
- Nach Arbeitsphase 2: Die Vergleichstabelle hat die Zeilen Sollwert, Vorher und Nachher. Meldet auch Nachher `nicht OK`, zeigt der Code die Ursache (meist `AVG` oder ein fehlender Monatsfilter).

## Abschlusskriterien

- Das Notebook enthält vier Antworten und eine Vorher/Nachher-Vergleichstabelle gegen den Sollwert. Die Tabelle ist das Ergebnis, auch wenn schon Vorher `OK` war.

## Erweiterung

Stelle in der Zelle **Erweiterung** eine eigene Frage, z. B. `eigene = frage("Welche drei Kunden hatten 2026 den höchsten Umsatz im Onlineshop?")`, und prüfe den erzeugten Code mit den drei Lesefragen. Rechne die Antwort mit pandas nach.

## Fallback

- Fragezellen melden `Ohne Dienst` oder `Dienst nicht erreichbar`: Führe die Zelle **Ohne Dienst** aus. Sie rechnet mit pandas (keine PandasAI-Antwort) die Marge je Region zweimal: als Mittelwert der Zeilenmargen (typischer Fehler) und als Summe Deckungsbeitrag / Summe Umsatz. Die Vergleichstabelle zeigt danach, welche Rechnung den Sollwert trifft. Den Code-Teil üben die zwei SQL-Abfragen in der Theorie.
- Das Beispiel-Notebook [`pandasai_fragen.ipynb`](../../project/examples/m04-llm-analysis/l01-pandasai/pandasai_fragen.ipynb) zeigt genau diesen Ablauf ohne Dienst.
