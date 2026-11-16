# Lab 7.1 – Übung: Was ist ein Skill?

**Dauer:** ca. 10 Minuten
**Ändert die Nordwind-Projektbasis?** Nein — der Beispiel-Skill `kpi-kurzcheck` wird nur gelesen und ausgeführt.
**Arbeitsdatei:** keine · **Beispiel:** `.github/skills/kpi-kurzcheck/` (liegt von Anfang an im Kursordner)

## Vorbereitung

- Kursordner als Arbeitsbereich in VS Code geöffnet, Terminal im Kursordner (**Terminal → New Terminal**).
- Chat geöffnet (**Strg+Alt+I**, macOS: Ctrl+Cmd+I), Modus **Agent**, Modell nach Skill-Regel 1 gewählt.

## Aufgaben

1. Öffne `.github/skills/kpi-kurzcheck/SKILL.md` im Explorer (Ordner `.github` → `skills` → `kpi-kurzcheck`). Kopiere den Befehl aus Schritt 1 des Vorgehens ins Terminal und führe ihn aus (Skill-Regel 4 als Probe):

   ```bash
   python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py
   ```

2. Öffne die Befehlspalette (**Strg+Umschalt+P**, macOS: Cmd+Umschalt+P), wähle **Chat: Open Customizations** → **Skills** und suche `kpi-kurzcheck` im Abschnitt **Workspace**.
3. Beginne einen neuen Chat (**+**) im Modus **Agent** und sende:

   > Führe den KPI-Kurzcheck für die Nordwind-Daten aus.

   Vergleiche den Befehl im Bestätigungsdialog mit `SKILL.md` und wähle **Allow** (Skill-Regel 5). Stimmt der Befehl nicht überein, wähle **Skip** und wende Skill-Regel 2 an.
4. Klappe in der Antwort die Zeile mit dem ausgeführten Befehl auf und vergleiche die vier Ausgabezeilen mit dem Terminal aus Aufgabe 1.
5. Beginne einen neuen Chat, tippe `/` ins Eingabefeld, wähle `kpi-kurzcheck` aus der Liste und sende die Nachricht. Erlaube den Befehl wie in Aufgabe 3.

**Claude Code:** Aufgabe 2 entfällt; `/kpi-kurzcheck` im Claude-Code-Panel listet den Skill und ruft ihn auf.

## Checkpoint

- Aufgabe 1: vier Zeilen, beginnend mit `KPI-Kurzcheck data/nordwind_umsatz.csv (Rohdaten, vor Bereinigung)`.
- Aufgabe 3 und 5: Der Dialog zeigt `python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py`; die Antwort enthält dieselben vier Zeilen wie das Terminal.

## Abschlusskriterien

- Ein Skill-Lauf per Satz und einer per `/` mit erlaubtem Befehl aus `SKILL.md`.

## Erweiterung

Finde einen zweiten Auslösesatz ohne das Wort „KPI-Kurzcheck“, der in einem neuen Chat denselben Skill trifft. Die Beschreibung in `SKILL.md` nennt die Wörter, auf die der Agent achtet.

## Fallback

- Skill fehlt in **Customizations → Skills**: prüfen, dass der Ordner `.github/skills/kpi-kurzcheck` im Wurzelordner liegt und `name` dem Ordnernamen entspricht; VS Code neu laden (**Developer: Reload Window**).
- KI-Assistent nicht verfügbar: Aufgabe 1 zeigt das Ergebnis des Skills; Agent-Lauf beim Trainer mitverfolgen.
