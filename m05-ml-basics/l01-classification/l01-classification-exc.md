# Lab 5.1 – Übung: Wie eine Maschine aus Daten lernt

**Dauer:** ca. 15 Minuten (nach der Vorführung)
**Ändert die Nordwind-Projektbasis?** Nein — das Notebook dient dem Verständnis; Lab 5.2 liest `kunden_rfm.csv` aus dem Beispiel von Lab 2.3.
**Arbeitsdatei:** `project/playground/m05-l01-wiederkauf.ipynb`
**Starter:** `project/starters/m05-l01-wiederkauf.ipynb` · **Beispiel:** `project/examples/m05-ml-basics/l01-classification/wiederkauf.ipynb`

## Vorbereitung

- VS Code mit dem Kursordner ist offen, das Notebook-Kernel Python 3.11 ist vorausgewählt (wie seit Lab 1.1).
- Das Notebook liest `umsatz_features.csv` aus dem Beispiel von Lab 2.3; eigene Dateien werden nicht gebraucht.

## Aufgaben

1. Kopiere `project/starters/m05-l01-wiederkauf.ipynb` im Explorer nach `project/playground/` (Rechtsklick **Copy**, auf `playground` Rechtsklick **Paste**) und öffne die Kopie.
2. Führe die Zellen von oben bis einschließlich Schritt 1 mit **Umschalt+Enter** aus. Die Ausgabe nennt die Zahl der Kunden und wie viele davon wieder kaufen.
3. Führe Schritt 2, Schritt 3 und die Prüfzelle aus. Ändere danach in der Zelle mit `AUFGABE 1` den Wert `TESTANTEIL = 0.2` auf `0.3`, klicke in diese Zelle und wähle im Zellmenü **Execute Cell and Below** (Zelle und alle darunter ausführen). Wiederhole das mit `0.5`.
4. Führe Schritt 4 aus: Die Tabelle zeigt die Grenzfälle, bei denen das Modell eine Wiederkauf-Wahrscheinlichkeit zwischen 0,2 und 0,8 schätzt.
5. Öffne das Beispiel `project/examples/m05-ml-basics/l01-classification/wiederkauf.ipynb` und vergleiche die Ausgabe von Schritt 3 bei Testanteil 20 % mit dem eigenen ersten Lauf.

## Checkpoint

- Schritt 1 meldet `400 Kunden, davon kaufen wieder: 329`.
- Die Prüfzelle meldet bei jedem Testanteil `OK – … liegt über der Messlatte …`.
- Bei Testanteil 20 % stehen Modell und Messlatte genau wie im Beispiel.

## Abschlusskriterien

- Das Notebook läuft von oben bis unten ohne Fehler.
- Für die Testanteile 20 %, 30 % und 50 % liegt die Genauigkeit des Modells über der Messlatte „alle kaufen wieder“.

## Erweiterung

Lass Copilot eine Verwechslungsmatrix in die leere Zelle unter **Erweiterung** schreiben (Copilot Chat, Modus Ask, Notebook mit `#file` anhängen) und führe sie aus:

> Im Notebook gibt es die Testdaten `y_test` (0 = kauft nicht wieder, 1 = kauft wieder) und die Vorhersagen `vorhersage` eines Klassifikationsmodells. Schreibe eine Zelle, die mit `confusion_matrix` aus scikit-learn eine Verwechslungsmatrix berechnet und als pandas-Tabelle mit den Zeilen „tatsächlich 0 (kauft nicht)“, „tatsächlich 1 (kauft wieder)“ und den Spalten „vorhergesagt 0“, „vorhergesagt 1“ ausgibt.

Die Matrix zeigt, welche der beiden Fehlerarten häufiger vorkommt: Kunden, die abspringen, obwohl das Modell „kauft wieder“ sagt, oder umgekehrt.

**Claude Code:** Prompt im Claude-Code-Panel senden, das Notebook mit `@` nennen und den Code aus der Antwort in die leere Zelle kopieren.

## Fallback

Läuft die eigene Kopie nicht: Starter erneut nach `project/playground/` kopieren oder im Beispiel `wiederkauf.ipynb` weiterarbeiten (dort zuerst **Alle ausführen**).
