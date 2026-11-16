# Lab 7.1 – Lösung: Was ist ein Skill?

Beispiel: der Skill [`.github/skills/kpi-kurzcheck/`](../../.github/skills/kpi-kurzcheck/SKILL.md), unverändert.

## Aufgabe 1: Befehl aus `SKILL.md` im Terminal

```text
KPI-Kurzcheck data/nordwind_umsatz.csv (Rohdaten, vor Bereinigung)
Zeilen:        33554
Monate:        2024-01 bis 2026-09 (33 Monate)
Umsatz gesamt: 9.917.522,56 €
```

Das ist das Ergebnis, das jeder Skill-Lauf liefern muss. Der Agent darf es nur weitergeben, nicht verändern.

## Aufgabe 2: Skill in Customizations

Unter **Skills → Workspace** steht `kpi-kurzcheck` mit dem Pfad `.github/skills/kpi-kurzcheck/SKILL.md` (Darstellung wie im Bild der Theorie, Stand 11/2026). Fehlt der Eintrag: Fallback der Übung.

## Aufgabe 3: Auslösen per Satz

Bestätigungsdialog (Befehl):

```text
python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py
```

| Prüfung nach Skill-Regel 5 | Ergebnis |
| --- | --- |
| steht so in `SKILL.md`, Vorgehen Schritt 1 | ja → **Allow** |
| ändert Dateien | nein |

Alternative: Der Agent schlägt `python3 …` statt `python …` vor. Gleiches Skript, gleicher Pfad – erlauben ist in Ordnung. Ein Befehl mit anderem Pfad oder mit `pandas`-Code direkt im Terminal (`python -c "…"`) heißt: Der Agent rechnet selbst → **Skip**, neuer Chat, „Nutze den Skill kpi-kurzcheck und zeige den Kurzcheck.“

## Aufgabe 4: Antwort gegen Terminal

Die Antwort folgt dem Vorgehen aus `SKILL.md`: die vier Zeilen aus Aufgabe 1 unverändert, danach ein Satz wie „Das sind Rohdaten vor der Bereinigung.“ Der aufgeklappte Eintrag im Chat zeigt den ausgeführten Befehl und die Terminal-Ausgabe. Eine abweichende Zahl (z. B. „rund 9,9 Mio. €“ statt `9.917.522,56 €`) verstößt gegen die Regel „keine Zahl runden“ → Skill-Regel 3.

## Aufgabe 5: Aufruf per `/`

Nach `/` listet VS Code Skills und gespeicherte Prompts; `/kpi-kurzcheck` lädt den Skill ohne Umweg über die Beschreibung (Stufe 2 direkt). Dialog und Ausgabe sind dieselben wie in Aufgabe 3.

## Erweiterung

Die Beschreibung nennt „Kurzcheck, Schnellcheck oder Überblick über die Nordwind-Daten“. Passende zweite Sätze:

- „Gib mir einen Schnellcheck der Nordwind-Daten.“
- „Wie viele Zeilen und welchen Gesamtumsatz hat die Nordwind-Rohdatei?“

Eine Frage wie „Welche Region wuchs 2025 am stärksten?“ passt nicht zur Beschreibung: Sie erwähnt weder Regionen noch Wachstum, und das Skript liefert diese Zahl auch nicht. Ob ein Satz auslöst, hängt auch vom Modell ab (Skill-Regel 1).
