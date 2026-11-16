# Lab 8.1 – Übung: Zahlen und Aussagen prüfen

**Dauer:** ca. 18 Minuten
**Ändert die Nordwind-Projektbasis?** Nein — es entsteht ein korrigierter Kommentar im Playground.
**Arbeitsdateien:** `project/playground/m08-l01-kommentar_oktober.md`, `project/playground/m08-l01-gegenproben.ipynb`
**Starter:** `project/starters/m08-l01-kommentar_oktober.md`, `project/starters/m08-l01-gegenproben.ipynb` · **Beispiel:** `project/examples/m08-validation/l01-fact-check/`

## Vorbereitung

- Das Notebook liest den Oktober-Bericht aus dem Beispiel von Lab 7.3 (`kpi_2026_10.xlsx`) und die Rohdaten `data/nordwind_umsatz.csv` + `nordwind_umsatz_2026_10.csv` (aus `data/`, sonst aus `lieferungen/`).
- Der Kommentar enthält genau drei Fehler: (a) eine falsche Zahl, (b) eine behauptete Ursache, (c) eine Verallgemeinerung.

## Aufgaben

1. Kopiere beide Starter nach `project/playground/` (Namen bleiben). Öffne den Kommentar in der Markdown-Vorschau (Rechtsklick → **Open Preview**) und das Notebook daneben. Führe die erste Zelle und die Prüfzelle am Ende aus: Sie meldet dreimal `nicht OK`.
2. Führe Gegenprobe 1 aus und vergleiche jede Zahl im Abschnitt „Umsatz“ des Kommentars mit der Zeile `Gesamt`. Korrigiere die falsche Zahl im Kommentar und speichere.
3. Führe Gegenprobe 2 aus. Ersetze den Satz im Abschnitt „Onlineshop“ durch eine Aussage, die nur nennt, was die Tabelle belegt: Wachstum je Kanal und gesamt, April–Oktober 2026 gegen 2025, ohne Ursache zu behaupten.
4. Führe Gegenprobe 3 aus. Ersetze „Alle Regionen …“ durch eine Aussage, die die Region mit Rückgang und ihre Abweichung zum Vorjahresmonat nennt.
5. Speichere den Kommentar und führe die Prüfzelle erneut aus. Bei `nicht OK` den Hinweis lesen, die Stelle anpassen und wiederholen.

**Claude Code:** Notebook und Markdown laufen gleich; nichts weicht ab.

## Checkpoint

- Gegenprobe 1 zeigt fünf Zeilen (Nord, Ost, Süd, West, Gesamt) wie die Kennzahlentabelle aus Lab 7.3.
- Gegenprobe 2 zeigt drei Zeilen (Außendienst, Onlineshop, Gesamt), Gegenprobe 3 vier Regionen.
- Die Prüfzelle meldet `OK – alle drei Korrekturen sind belegt.`

## Abschlusskriterien

- `project/playground/m08-l01-kommentar_oktober.md` ohne die drei Fehler; jede geänderte Aussage stützt sich auf eine der drei Gegenproben.

## Erweiterung

Lass den Skill einen eigenen Kommentar schreiben und prüfe ihn genauso. Neuer Chat im Modus **Agent**:

> Nutze den Skill monatsbericht und erstelle den Bericht für Oktober 2026. Schreibe danach einen Managementkommentar in vier kurzen Absätzen (Umsatz, Onlineshop, Regionen, Ausblick) und beantworte darin: Hat der Relaunch des Onlineshops im März 2026 den Umsatz gesteigert?

Speichere die Antwort als `project/playground/kommentar_skill.md` und prüfe jede Zahl und jede Aussage mit Gegenprobe 1 bis 3. Markiere, was der Bericht des Skills gar nicht enthält (z. B. Zahlen je Kanal).

## Fallback

- Notebook läuft nicht: im Beispiel `project/examples/m08-validation/l01-fact-check/gegenproben.ipynb` die Tabellen ablesen; der korrigierte Kommentar liegt daneben als `kommentar_oktober_korrigiert.md`.
- KI-Assistent nicht verfügbar: Die Erweiterung entfällt; die Basis braucht keinen KI-Assistenten.
