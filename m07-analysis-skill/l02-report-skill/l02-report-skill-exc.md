# Lab 7.2 – Übung: Den Monatsbericht-Skill bauen

**Dauer:** ca. 25 Minuten (inkl. 5 Minuten Abschlussrunde)
**Ändert die Nordwind-Projektbasis?** Ja — es entsteht der Skill `.github/skills/monatsbericht/`; Lab 7.3 nutzt ihn für die Oktober-Lieferung, Lab 9.1 kopiert ihn.
**Arbeitsdatei:** `.github/skills/monatsbericht/SKILL.md`
**Starter:** `project/starters/m07-l02-SKILL.md` · **Beispiel:** `project/examples/m07-analysis-skill/l02-report-skill/monatsbericht/`

## Vorbereitung

- Terminal im Kursordner, Chat im Modus **Agent** mit dem Modell nach Skill-Regel 1.
- `data/` enthält den Startbestand (`nordwind_umsatz.csv`, `kontrollsummen.csv`, `nordwind_plan_2026.csv`); `lieferungen/` bleibt unverändert.

## Aufgaben

1. Lege im Explorer den Skill-Ordner an: Rechtsklick auf `.github/skills` → **New Folder…** → `monatsbericht/scripts`. Kopiere `project/examples/m06-forecast-report/l02-report-v2/monatsbericht.py` nach `.github/skills/monatsbericht/scripts/` und `project/starters/m07-l02-SKILL.md` nach `.github/skills/monatsbericht/`; benenne die Kopie des Starters mit **F2** in `SKILL.md` um.
2. Teste das Skript am neuen Ort im Terminal (Stufe 1):

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat 2026-09 --excel
   ```

3. Öffne `.github/skills/monatsbericht/SKILL.md`, beginne einen neuen Chat im Modus **Agent** und lass Copilot beide Lücken füllen. Prüfe die Änderung und wähle **Keep**:

   > Die Datei `#file:.github/skills/monatsbericht/SKILL.md` ist das Gerüst eines Agent Skills. Das Skript `.github/skills/monatsbericht/scripts/monatsbericht.py` erzeugt den Nordwind-Monatsbericht zum Umsatz; Befehle `bericht`, `auffaelligkeiten`, `prognose`; Optionen `--daten <ordner>`, `--monat JJJJ-MM`, `--excel`; jede Ausgabe endet mit den Zeilen `Summenkontrolle: …` und `Sollwert-Prüfung: …`, bei unbrauchbarer Lieferung erscheint stattdessen eine Zeile `STOPP: …`. Fülle nur die Stellen zwischen `>>> AUFGABE` und `<<< ENDE`, lass die Markierungen stehen. AUFGABE 1: `description` in einer Zeile, was der Skill liefert (Kennzahlen je Region mit Vormonat, Vorjahr, Plan und Marge, Segmente, auffällige Tage, Prognose, HTML und Excel) und wann er gilt, mit den Wörtern Monatsbericht, Umsatzbericht, Umsatz eines Monats, Auffälligkeiten, Prognose, neue Nordwind-Umsatzlieferung. AUFGABE 2: Abschnitt `## Vorgehen` mit drei nummerierten Schritten: (1) Monat als JJJJ-MM bestimmen, fehlt er, nachfragen statt raten; (2) genau einen der drei Befehle in je einem `bash`-Codeblock ausführen, Form `python .github/skills/monatsbericht/scripts/monatsbericht.py <befehl> --daten data --monat JJJJ-MM`, beim Befehl `bericht` zusätzlich `--excel`; (3) bei einer Zeile `STOPP:` diese wörtlich melden, sagen, dass kein Bericht entstanden ist, und nichts weiter tun. Danach Abschnitt `## Antwortformat` mit vier Punkten: Kurzfazit in 2–3 Sätzen nur mit Zahlen aus der Ausgabe; Kennzahlentabelle aus der Ausgabe als Markdown-Tabelle; die Zeilen Summenkontrolle und Sollwert-Prüfung wörtlich; Pfade zu `berichte/bericht_JJJJ_MM_v2.html` und `berichte/kpi_JJJJ_MM.xlsx`. Ändere nichts außerhalb der Markierungen und führe keine Befehle aus.

   **Claude Code:** Prompt im Claude-Code-Panel senden, die Datei mit `@` nennen; die vorgeschlagene Änderung annehmen.
4. Beginne einen neuen Chat im Modus **Agent** und sende „Erstelle den Monatsbericht für September 2026.“ Erlaube nur den Befehl aus `SKILL.md` (Skill-Regel 5). Löst der Skill nicht aus oder fehlen die Prüfzeilen, wende Skill-Regel 2 und 3 an; als letzter Rückfall gilt Aufgabe 2 (Skill-Regel 4).
5. Beginne einen neuen Chat und sende „Erstelle den Monatsbericht.“ ohne Monat. Der Agent fragt nach dem Monat, statt zu raten; antworte mit „September 2026“.

## Checkpoint

- Nach Aufgabe 2 enden Terminal-Ausgabe und Bericht mit:

  ```text
  Summenkontrolle: 2026-09 – 1.144 Zeilen, Summe Umsatz 343.381,74 – stimmt mit der Kennzahlentabelle überein
  Sollwert-Prüfung: bestanden (12 Werte für 2026-09 gegen kontrollsummen.csv)
  ```

- Nach Aufgabe 3 enthält `SKILL.md`: eine ausgefüllte `description`, drei Codeblöcke mit `--daten data`, die Wörter `STOPP`, `Summenkontrolle` und `Sollwert-Prüfung`.
- Nach Aufgabe 4 zeigt die Antwort Kurzfazit, Kennzahlentabelle, beide Prüfzeilen wie oben und die Pfade zu HTML und Excel.

## Abschlusskriterien

- `.github/skills/monatsbericht/SKILL.md` und `scripts/monatsbericht.py` liegen im Skill-Ordner.
- Ein Satz im Chat erzeugt `berichte/bericht_2026_09_v2.html` und `berichte/kpi_2026_09.xlsx`; die Antwort meldet „Sollwert-Prüfung: bestanden“.

## Erweiterung

Sende in einem neuen Chat „Was ist im September 2026 auffällig?“. Der Agent wählt den Befehl `auffaelligkeiten`; die Antwort nennt die auffälligen Tage und beide Prüfzeilen.

## Fallback

- Copilot füllt die Lücken nicht oder falsch: **Undo**, dann `SKILL.md` aus dem Beispiel `project/examples/m07-analysis-skill/l02-report-skill/monatsbericht/SKILL.md` in den Skill-Ordner kopieren (vorhandene Datei ersetzen).
- KI-Assistent nicht verfügbar: Befehl aus Aufgabe 2 im Terminal (Skill-Regel 4); er erzeugt denselben Bericht.
