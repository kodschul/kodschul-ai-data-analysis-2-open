# Cheatsheet: Skills

Schnellreferenz für Modul 7: Aufbau eines Agent Skills, Auslösen, Skill-Regeln und die Befehle des Skills `monatsbericht`. Alle Befehle laufen im Terminal im Kursordner.

## Ordner und Dateien

| Pfad | Inhalt |
| --- | --- |
| `.github/skills/<name>/SKILL.md` | Anleitung: Frontmatter + Vorgehen (Wurzelordner des Arbeitsbereichs) |
| `.github/skills/<name>/scripts/` | Skripte, die der Skill ausführt |
| `.claude/skills/<name>/` | Ort für Claude Code (Kopie von `.github/skills/`; Stand 11/2026 prüfen) |
| `.github/skills/kpi-kurzcheck/` | Beispiel-Skill (Lab 1.2, 7.1) |
| `.github/skills/monatsbericht/` | Skill aus Lab 7.2: `SKILL.md` + `scripts/monatsbericht.py` (Kopie von v2) |
| `lieferungen/` → `data/` | neue Lieferung erst nach dem Verschieben auswerten (Lab 7.3) |

## Aufbau von `SKILL.md`

| Teil | Regel | Beispiel |
| --- | --- | --- |
| `name:` | Kleinbuchstaben, Ziffern, Bindestriche; = Ordnername; ≤ 64 Zeichen | `monatsbericht` |
| `description:` | was der Skill liefert + wann er gilt + Wörter aus echten Fragen; ≤ 1024 Zeichen | „Erstellt den Nordwind-Monatsbericht … Verwenden bei Fragen nach Monatsbericht, Umsatzbericht …“ |
| `## Wann verwenden` | Beispielfragen; wofür nicht | „Nicht verwenden für Kosten je Kostenstelle“ |
| `## Vorgehen` | nummerierte Schritte, vollständige Befehle in `bash`-Codeblöcken | Monat bestimmen → Befehl → bei `STOPP:` aufhören |
| `## Antwortformat` | was in die Antwort gehört, was wörtlich bleibt | Kurzfazit, Kennzahlentabelle, Prüfzeilen wörtlich, Dateipfade |
| `## Regeln` | was nie passieren darf | keine eigene Zahl, keine Dateien ändern |

Gerüst:

```markdown
---
name: monatsbericht
description: Erstellt … Verwenden bei Fragen nach …
---

# Titel

## Wann verwenden
## Vorgehen
## Antwortformat
## Regeln
```

## Schrittweises Laden

| Stufe | Agent liest | wann |
| --- | --- | --- |
| 1 | `name` + `description` aller Skills | immer |
| 2 | übrige `SKILL.md` | Frage passt oder Aufruf per `/` |
| 3 | Skripte und Dateien | nur wenn die Anleitung sie nennt |

## Auslösen

| Weg | Beispiel |
| --- | --- |
| natürlicher Satz (Agent-Modus) | „Erstelle den Monatsbericht für September 2026.“ |
| ausdrücklicher Satz | „Nutze den Skill monatsbericht und erstelle den Bericht für Oktober 2026.“ |
| Slash-Befehl | `/monatsbericht` im Chat-Eingabefeld, dann Monat nennen |
| Skills anzeigen (VS Code) | Befehlspalette → **Chat: Open Customizations** → **Skills** → Workspace |
| Skills anzeigen (Claude Code) | `/` im Claude-Code-Panel |

## Die fünf Skill-Regeln

| Nr. | Regel |
| --- | --- |
| 1 | ein Modell wählen und für alle Skill-Läufe beibehalten |
| 2 | natürlicher Satz; löst nichts aus: neuer Chat, „Nutze den Skill … und …“ oder `/name` |
| 3 | fehlen `Summenkontrolle:` und `Sollwert-Prüfung:` in der Antwort, hat der Agent selbst gerechnet: neuer Chat, ausdrücklicher Satz |
| 4 | letzter Rückfall: Befehl aus `SKILL.md` im Terminal |
| 5 | im Bestätigungsdialog nur Befehle aus `SKILL.md` erlauben: **Allow**, nicht **Always Allow** |

## Befehle des Skills `monatsbericht`

| Befehl | Ergebnis |
| --- | --- |
| `python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat 2026-09 --excel` | `berichte/bericht_2026_09_v2.html` + `berichte/kpi_2026_09.xlsx` |
| `python .github/skills/monatsbericht/scripts/monatsbericht.py auffaelligkeiten --daten data --monat 2026-09` | auffällige Tage im Terminal |
| `python .github/skills/monatsbericht/scripts/monatsbericht.py prognose --daten data --monat 2026-09` | Prognose der drei Folgemonate |
| `python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py` | Zeilen, Monate, Gesamtumsatz der Rohdatei |

## Meldungen des Skripts

| Ausgabe | Bedeutung | Antwort des Agenten |
| --- | --- | --- |
| `Sollwert-Prüfung: bestanden (12 Werte …)` | alle Werte des Monats stimmen mit `kontrollsummen.csv` | Prüfzeilen wörtlich melden |
| `Sollwert-Prüfung: n Abweichungen …` | Zahlen weichen von den Sollwerten ab | melden, nicht beschönigen |
| `STOPP: Pflichtspalte umsatz fehlt in <datei>` | Lieferung unbrauchbar, Exit-Code 2, kein Bericht | Zeile wörtlich melden, nichts weiter tun |
| `STOPP: keine Daten für den Monat 2026-10 in data/` | Lieferung noch nicht in `data/` | Datei von `lieferungen/` nach `data/` verschieben |

## Kennzahlen zum Abgleich

| Monat | Summenkontrolle | Sollwert-Prüfung |
| --- | --- | --- |
| 2026-09 | 1.144 Zeilen, Summe Umsatz 343.381,74 | bestanden (12 Werte) |
| 2026-10 | 1.111 Zeilen, Summe Umsatz 337.139,00 | bestanden (12 Werte) |
