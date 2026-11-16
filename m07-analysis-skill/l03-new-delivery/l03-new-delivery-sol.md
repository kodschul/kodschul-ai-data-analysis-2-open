# Lab 7.3 – Lösung: Neue Daten, gleicher Bericht

Fertige Ausgaben: [project/examples/m07-analysis-skill/l03-new-delivery/](../../project/examples/m07-analysis-skill/l03-new-delivery/stopp_meldung.txt) mit `berichte/bericht_2026_10_v2.html`, `berichte/kpi_2026_10.xlsx` (Ergebnis der Aufgaben 2 und 5) und `stopp_meldung.txt` (Aufgabe 4). Lab 8.1 liest den Oktober-Bericht aus diesem Ordner.

Die Ausgaben unten stammen vom Befehl aus `SKILL.md`, im Kursordner ausgeführt. Was der Agent im Chat daraus formuliert, steht als **Antwortformat laut `SKILL.md`** darunter: eine Musterantwort aus der Ausgabe, keine aufgezeichnete Agent-Antwort.

## Aufgabe 1: Lieferung verschieben

```text
data/
├── kontrollsummen.csv
├── nordwind_feedback.csv
├── nordwind_plan_2026.csv
├── nordwind_umsatz.csv
└── nordwind_umsatz_2026_10.csv     ← neu
lieferungen/
├── kostenstellen.csv
└── nordwind_umsatz_2026_10_defekt.csv
```

## Aufgabe 2: Oktober-Bericht per Skill

Bestätigungsdialog: `python .github/skills/monatsbericht/scripts/monatsbericht.py bericht --daten data --monat 2026-10 --excel`

```text
Monatsbericht 2026-10 – Umsatz – Daten: data/nordwind_umsatz*.csv
  nordwind_umsatz.csv: 33.554 Zeilen gelesen
  nordwind_umsatz_2026_10.csv: 1.124 Zeilen gelesen
  Dubletten entfernt: 411
  Zeilen ohne Kosten (zählen für Umsatz, nicht für den Deckungsbeitrag): 668
  Schreibweisen Region: 14 -> 4
  Zeilen nach Bereinigung: 34.267, Monate 2024-01 bis 2026-10

           Umsatz   Vormonat  Δ Vormonat %    Vorjahr  Δ Vorjahr %      Plan  Δ Plan %  Deckungsbeitrag  Marge %
Region
Nord    101463.16  103872.09          -2.3   99371.29          2.1  104000.0      -2.4         20534.58     20.2
Ost      52972.84   58995.87         -10.2   58005.14         -8.7   60000.0     -11.7         11381.24     21.5
Süd      79597.38   83138.94          -4.3   76658.34          3.8   81000.0      -1.7         16101.07     20.2
West    103105.62   97374.84           5.9   93514.22         10.3  101000.0       2.1         21433.42     20.8
Gesamt  337139.00  343381.74          -1.8  327548.99          2.9  346000.0      -2.6         69450.31     20.6

Segmente: [14, 87, 56, 243] Kunden je Segment 1–4
Auffällige Tage (Schwelle 3): 0
Prognose 2026-11 bis 2027-01: 375.345, 318.947, 353.586

Bericht: berichte/bericht_2026_10_v2.html
OK – berichte/kpi_2026_10.xlsx mit 5 Zeilen im Blatt 'Kennzahlen' (Blätter: Kennzahlen, Auffaelligkeiten)

Summenkontrolle: 2026-10 – 1.111 Zeilen, Summe Umsatz 337.139,00 – stimmt mit der Kennzahlentabelle überein
Sollwert-Prüfung: bestanden (12 Werte für 2026-10 gegen kontrollsummen.csv)
```

Antwortformat laut `SKILL.md` (Musterantwort aus dieser Ausgabe):

> **Kurzfazit:** Der Umsatz im Oktober 2026 beträgt 337.139,00 €: −1,8 % zum Vormonat, +2,9 % zum Vorjahresmonat und −2,6 % zum Plan. Ost liegt deutlich unter Vorjahr (−8,7 %) und Plan (−11,7 %), West deutlich darüber.
>
> | Region | Umsatz | Δ Vormonat % | Δ Vorjahr % | Δ Plan % | Marge % |
> | --- | ---: | ---: | ---: | ---: | ---: |
> | Nord | 101463.16 | -2.3 | 2.1 | -2.4 | 20.2 |
> | Ost | 52972.84 | -10.2 | -8.7 | -11.7 | 21.5 |
> | Süd | 79597.38 | -4.3 | 3.8 | -1.7 | 20.2 |
> | West | 103105.62 | 5.9 | 10.3 | 2.1 | 20.8 |
> | Gesamt | 337139.00 | -1.8 | 2.9 | -2.6 | 20.6 |
>
> Summenkontrolle: 2026-10 – 1.111 Zeilen, Summe Umsatz 337.139,00 – stimmt mit der Kennzahlentabelle überein
> Sollwert-Prüfung: bestanden (12 Werte für 2026-10 gegen kontrollsummen.csv)
>
> Dateien: `berichte/bericht_2026_10_v2.html`, `berichte/kpi_2026_10.xlsx`

Im Oktober gibt es bei Schwelle 3 keinen auffälligen Tag; der Abschnitt Auffälligkeiten im HTML zeigt „keine auffälligen Tage“.

## Aufgabe 3: Lieferung austauschen

`data/` enthält jetzt `nordwind_umsatz_2026_10_defekt.csv` statt `nordwind_umsatz_2026_10.csv`.

## Aufgabe 4: Stopp statt Bericht

Bestätigungsdialog: derselbe Befehl wie in Aufgabe 2. Ausgabe (Datei `stopp_meldung.txt` im Beispiel):

```text
STOPP: Pflichtspalte umsatz fehlt in nordwind_umsatz_2026_10_defekt.csv
```

Exit-Code 2, keine neue HTML- oder Excel-Datei. Antwortformat laut `SKILL.md`, Vorgehen Schritt 3 (Musterantwort):

> `STOPP: Pflichtspalte umsatz fehlt in nordwind_umsatz_2026_10_defekt.csv`
>
> Es wurde kein Bericht erstellt. Die Lieferung enthält die Pflichtspalte `umsatz` nicht.

Nicht in Ordnung wären: Oktober-Zahlen in der Antwort, ein zweiter Befehl mit geändertem `--muster` oder ein Vorschlag, die Datei selbst umzubenennen. Dann **Skip** bzw. Skill-Regel 3. Die Datei `berichte/bericht_2026_10_v2.html` aus Aufgabe 2 liegt noch im Ordner; sie stammt von der richtigen Lieferung, nicht von diesem Lauf.

## Aufgabe 5: richtige Datei zurück

Ordner wie nach Aufgabe 1. Der Befehl im Terminal liefert dieselbe Ausgabe wie in Aufgabe 2 und überschreibt Bericht und Excel mit identischem Inhalt.

## Erweiterung: Rückfrage nach dem Stopp

Ergänzung in `SKILL.md`, Vorgehen Schritt 3:

```markdown
3. Beginnt eine Zeile der Ausgabe mit `STOPP:`, diese Zeile wörtlich melden, sagen, dass kein Bericht entstanden ist, und nichts weiter rechnen oder ausführen.
   Danach genau diese Rückfrage stellen: „Die Lieferung ist so nicht verwendbar. Soll eine korrigierte Datei beim Absender angefordert werden, oder liegt schon eine korrigierte Fassung in `lieferungen/`?“
```

Antwortformat nach Aufgabe 4 mit der Ergänzung (Musterantwort): die `STOPP`-Zeile, der Satz „Es wurde kein Bericht erstellt.“ und die festgelegte Rückfrage. Die Rückfrage führt zu keinem weiteren Befehl; das Verschieben der richtigen Datei bleibt Handarbeit (Aufgabe 5).
