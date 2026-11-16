# Lab 6.1 – Übung: Umsatz prognostizieren

**Dauer:** ca. 25 Minuten (inkl. 5 Minuten Abschlussrunde)
**Ändert die Nordwind-Projektbasis?** Ja — es entsteht `prognose_einfach`; der Bericht v2 (Lab 6.2) rechnet dieselbe Prognose ohne Backtest.
**Arbeitsdatei:** `project/playground/m06-l01-prognose.ipynb`
**Starter:** `project/starters/m06-l01-prognose.ipynb` · **Beispiel:** `project/examples/m06-forecast-report/l01-forecast/prognose.ipynb`

## Vorbereitung

- Das Notebook liest `umsatz_features.csv` aus dem Beispiel von Lab 2.3 und bildet daraus den Monatsumsatz.
- Die naive Prognose, Backtest und Diagramme sind fertig; offen ist die einfache Prognose mit Trendfaktor.

## Aufgaben

1. Kopiere `project/starters/m06-l01-prognose.ipynb` nach `project/playground/`, öffne die Kopie und führe die Zellen bis einschließlich Schritt 1 aus. Das Liniendiagramm zeigt 33 Monate; die naive Prognose für 2026-10 lautet 327.549.
2. Fülle die Zelle mit `AUFGABE 1` mit Copilot (Chat, Modus Ask, Notebook mit `#file` anhängen) und diesem Prompt, übernimm den Code zwischen die Markierungen und führe die Zelle und die Prüfzelle aus:

   > Im Notebook gibt es die pandas-Series `umsatz` (Index = Monat als Text "JJJJ-MM", Werte = Monatsumsatz, aufsteigend sortiert) und die Funktion `vorjahresmonat(monat)`, die zum Beispiel aus "2026-04" den Text "2025-04" macht. Schreibe eine Funktion `prognose_einfach(umsatz, monat, stand)`: Nimm nur die Monate bis einschließlich `stand`. Trendfaktor = Summe der letzten 12 dieser Monate geteilt durch die Summe der 12 Monate davor. Ergebnis = Umsatz im Vorjahresmonat von `monat` × Trendfaktor. Gib nur die Funktion für eine Notebook-Zelle aus, ohne Aufruf.

   **Claude Code:** Prompt im Claude-Code-Panel senden, das Notebook mit `@` nennen, Code aus der Antwort zwischen die Markierungen kopieren.
3. Meldet die Prüfzelle `nicht OK`, lies den Hinweis und versuche es ein zweites Mal; sonst setze das Lösungs-Snippet aus der Lösung ein.
4. Führe Schritt 3 (Backtest) mit Tabelle und Diagramm aus.
5. Führe Schritt 4 aus und öffne `project/playground/prognose_2026.html` im Browser. Der Diagrammtitel nennt die Summe für das vierte Quartal 2026 und den Backtest-MAPE.

## Checkpoint

- Nach Aufgabe 2: Die Prüfzelle meldet `OK – 2026-04: 288.113 € (Vorjahr 272.033 € × Trendfaktor 1,059); 2026-10: 354.164 €`.
- Nach Aufgabe 4: `MAPE naiv: 7.7 %` und `MAPE einfach: 4.8 %`, gleich wie im Beispiel.

## Abschlusskriterien

- `prognose_2026.csv` enthält die Monate 2026-10 bis 2026-12 mit naiver und einfacher Prognose.
- Das Prognosediagramm zeigt Ist bis September 2026 und die einfache Prognose bis Dezember 2026; der Titel nennt den Backtest-MAPE.

## Erweiterung

Eine der beiden Varianten in die leere Zelle unter **Erweiterung**, mit eigenem Prompt nach dem Muster Kontext + Spalten + Regel + Ausgabe:

- **Spanne:** Zeichne um die einfache Prognose eine graue Fläche von Prognose × (1 − MAPE/100) bis Prognose × (1 + MAPE/100) in das bestehende Diagramm `fig` (Tabelle `vorschau`, Spalten `monat` und `umsatz`, Variable `mape_einfach`).
- **Backtest je Region:** Wiederhole den Backtest (Stand 2026-03, Monate 2026-04 bis 2026-09) für jede Region einzeln und gib je Region den MAPE beider Prognosen aus; die Monatsumsätze je Region kommen aus `df.groupby(["region", "monat"])["umsatz"].sum()`.

## Fallback

Läuft die eigene Kopie nicht: Starter erneut kopieren oder im Beispiel `prognose.ipynb` weiterarbeiten.
