# Lab 7.2 – Lösung: Den Monatsbericht-Skill bauen

Fertiger Stand: [project/examples/m07-analysis-skill/l02-report-skill/monatsbericht/](../../project/examples/m07-analysis-skill/l02-report-skill/monatsbericht/SKILL.md) mit `SKILL.md` und `scripts/monatsbericht.py` (unveränderte Kopie von v2 aus Lab 6.2). Das Beispiel liegt bewusst nicht in `.github/skills/`, damit es nicht vorzeitig auslöst.

## Aufgabe 1: Skill-Ordner

```text
.github/skills/
├── kpi-kurzcheck/
│   ├── SKILL.md
│   └── scripts/kpi_kurzcheck.py
└── monatsbericht/
    ├── SKILL.md
    └── scripts/monatsbericht.py
```

## Aufgabe 2: Skript am neuen Ort

```text
Monatsbericht 2026-09 – Umsatz – Daten: data/nordwind_umsatz*.csv
  nordwind_umsatz.csv: 33.554 Zeilen gelesen
  Dubletten entfernt: 398
  Zeilen ohne Kosten (zählen für Umsatz, nicht für den Deckungsbeitrag): 648
  Schreibweisen Region: 14 -> 4
  Zeilen nach Bereinigung: 33.156, Monate 2024-01 bis 2026-09

           Umsatz   Vormonat  Δ Vormonat %    Vorjahr  Δ Vorjahr %      Plan  Δ Plan %  Deckungsbeitrag  Marge %
Region
Nord    103872.09  101046.86           2.8  103297.45          0.6  108000.0      -3.8         21085.71     20.3
Ost      58995.87   57563.11           2.5   61560.70         -4.2   63000.0      -6.4         12163.13     20.6
Süd      83138.94   79258.85           4.9   75062.71         10.8   80000.0       3.9         16967.93     20.4
West     97374.84   91920.21           5.9   87939.19         10.7   95000.0       2.5         20344.76     20.9
Gesamt  343381.74  329789.03           4.1  327860.05          4.7  346000.0      -0.8         70561.53     20.5

Segmente: [14, 90, 55, 241] Kunden je Segment 1–4
Auffällige Tage (Schwelle 3): 2
Prognose 2026-10 bis 2026-12: 354.164, 375.537, 319.110

Bericht: berichte/bericht_2026_09_v2.html
OK – berichte/kpi_2026_09.xlsx mit 5 Zeilen im Blatt 'Kennzahlen' (Blätter: Kennzahlen, Auffaelligkeiten)

Summenkontrolle: 2026-09 – 1.144 Zeilen, Summe Umsatz 343.381,74 – stimmt mit der Kennzahlentabelle überein
Sollwert-Prüfung: bestanden (12 Werte für 2026-09 gegen kontrollsummen.csv)
```

Gleiche Zahlen wie in Lab 6.2: Das Skript ist dasselbe, nur der Ort ist neu.

## Aufgabe 3: Lösungs-Snippets für `SKILL.md`

**AUFGABE 1** (Frontmatter):

```yaml
# >>> AUFGABE 1: description in einer Zeile – was der Skill tut und wann er verwendet wird – Prompt siehe Übung, Aufgabe 3
description: Erstellt den Nordwind-Monatsbericht zum Umsatz (Kennzahlen je Region mit Vormonat, Vorjahr, Plan und Marge, Kundensegmente, auffällige Tage, Prognose) als HTML und Excel mit dem Skript scripts/monatsbericht.py und meldet Summenkontrolle und Sollwert-Prüfung. Verwenden bei Fragen nach Monatsbericht, Umsatzbericht, Umsatz oder Kennzahlen eines Monats, Auffälligkeiten, Umsatzprognose oder einer neuen Nordwind-Umsatzlieferung.
# <<< ENDE AUFGABE 1
```

**AUFGABE 2** (zwischen den Markierungen):

````markdown
<!-- >>> AUFGABE 2: Abschnitte "## Vorgehen" und "## Antwortformat" – Prompt siehe Übung, Aufgabe 3 -->
## Vorgehen

1. Berichtsmonat als JJJJ-MM bestimmen (September 2026 = `2026-09`). Nennt die Frage keinen eindeutigen Monat, zuerst nachfragen („Für welchen Monat, z. B. 2026-09?“) und nicht raten.
2. Im Wurzelordner des Arbeitsbereichs genau einen dieser Befehle ausführen, `JJJJ-MM` durch den Monat ersetzen:

   Monatsbericht (HTML und Excel):

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat JJJJ-MM --excel
   ```

   Nur die auffälligen Tage:

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py auffaelligkeiten --daten data --monat JJJJ-MM
   ```

   Nur die Prognose der drei Folgemonate:

   ```bash
   python .github/skills/monatsbericht/scripts/monatsbericht.py prognose --daten data --monat JJJJ-MM
   ```

3. Beginnt eine Zeile der Ausgabe mit `STOPP:`, diese Zeile wörtlich melden, sagen, dass kein Bericht entstanden ist, und nichts weiter rechnen oder ausführen.

## Antwortformat

1. **Kurzfazit:** 2–3 Sätze zu Gesamtumsatz und Abweichung zu Vormonat, Vorjahr und Plan; nur Zahlen aus der Ausgabe.
2. **Kennzahlentabelle:** die Tabelle aus der Ausgabe als Markdown-Tabelle (Region, Umsatz, Δ Vormonat %, Δ Vorjahr %, Δ Plan %, Marge %). Bei `auffaelligkeiten` oder `prognose` stattdessen deren Tabelle.
3. **Prüfung:** die Zeilen `Summenkontrolle: …` und `Sollwert-Prüfung: …` wörtlich aus der Ausgabe.
4. **Dateien:** Pfade zu `berichte/bericht_JJJJ_MM_v2.html` und `berichte/kpi_JJJJ_MM.xlsx` (nur beim Befehl `bericht`).
<!-- <<< ENDE AUFGABE 2 -->
````

Die Befehle wurden aus dieser `SKILL.md` kopiert und im Kursordner mit `2026-09` ausgeführt: alle drei laufen fehlerfrei und enden mit denselben zwei Prüfzeilen.

| Häufige Abweichung im KI-Entwurf | Folge | Korrektur |
| --- | --- | --- |
| Pfad `scripts/monatsbericht.py` ohne `.github/skills/monatsbericht/` | Befehl findet die Datei im Kursordner nicht | vollständigen Pfad einsetzen |
| `--daten data` fehlt oder `--daten data/nordwind_umsatz.csv` | falscher Ordner bzw. `STOPP: keine Datei …` | genau `--daten data` |
| Antwortformat „Prüfergebnis zusammenfassen“ | Agent formuliert die Prüfzeilen um, Skill-Regel 3 greift nicht mehr | „wörtlich“ verlangen |
| `--monat` fehlt im Befehl | Skript nimmt still den letzten Monat | `--monat JJJJ-MM` und „nachfragen statt raten“ |

## Aufgabe 4: Skill per Satz

Bestätigungsdialog:

```text
python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat 2026-09 --excel
```

Die Terminal-Ausgabe im Chat ist identisch mit Aufgabe 2. **Antwortformat, wie `SKILL.md` es verlangt** (Musterantwort aus der Ausgabe oben, keine aufgezeichnete Agent-Antwort):

> **Kurzfazit:** Der Umsatz im September 2026 beträgt 343.381,74 €. Das sind +4,1 % zum Vormonat und +4,7 % zum Vorjahresmonat; der Plan wird um 0,8 % verfehlt.
>
> | Region | Umsatz | Δ Vormonat % | Δ Vorjahr % | Δ Plan % | Marge % |
> | --- | ---: | ---: | ---: | ---: | ---: |
> | Nord | 103872.09 | 2.8 | 0.6 | -3.8 | 20.3 |
> | Ost | 58995.87 | 2.5 | -4.2 | -6.4 | 20.6 |
> | Süd | 83138.94 | 4.9 | 10.8 | 3.9 | 20.4 |
> | West | 97374.84 | 5.9 | 10.7 | 2.5 | 20.9 |
> | Gesamt | 343381.74 | 4.1 | 4.7 | -0.8 | 20.5 |
>
> Summenkontrolle: 2026-09 – 1.144 Zeilen, Summe Umsatz 343.381,74 – stimmt mit der Kennzahlentabelle überein
> Sollwert-Prüfung: bestanden (12 Werte für 2026-09 gegen kontrollsummen.csv)
>
> Dateien: `berichte/bericht_2026_09_v2.html`, `berichte/kpi_2026_09.xlsx`

Prüfen: Jede Zahl der Antwort steht in der Ausgabe von Aufgabe 2; beide Prüfzeilen sind Zeichen für Zeichen gleich.

## Aufgabe 5: Frage ohne Monat

Laut Vorgehen Schritt 1 führt der Agent noch keinen Befehl aus, sondern fragt nach dem Monat, z. B. „Für welchen Monat, z. B. 2026-09?“. Nach „September 2026“ folgt derselbe Dialog wie in Aufgabe 4. Führt der Agent stattdessen sofort `bericht` ohne `--monat` aus: **Skip**; in `SKILL.md` prüfen, ob Schritt 1 „nachfragen statt raten“ enthält.

## Erweiterung: „Was ist im September 2026 auffällig?“

Befehl im Dialog und Ausgabe (im Kursordner ausgeführt):

```text
$ python .github/skills/monatsbericht/scripts/monatsbericht.py auffaelligkeiten --daten data --monat 2026-09
…
Auffällige Tage 2026-09 (Schwelle 3): 2
     Datum Region  Umsatz  Monatsmittel  Abstand (Std.-Abw.)
01.09.2026    Süd 7185.31       3779.04                  3.1
24.09.2026    Ost 6640.98       2681.63                  3.2

Summenkontrolle: 2026-09 – 1.144 Zeilen, Summe Umsatz 343.381,74 – stimmt mit der Kennzahlentabelle überein
Sollwert-Prüfung: bestanden (12 Werte für 2026-09 gegen kontrollsummen.csv)
```

Die Antwort nennt diese zwei Tage als Tabelle und beide Prüfzeilen; es entsteht keine neue HTML-Datei.
