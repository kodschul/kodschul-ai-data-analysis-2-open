# Lab 8.1 – Lösung: Zahlen und Aussagen prüfen

Fertiger Stand: [project/examples/m08-validation/l01-fact-check/](../../project/examples/m08-validation/l01-fact-check/kommentar_oktober_korrigiert.md) mit `kommentar_oktober_korrigiert.md` und dem ausgeführten Notebook `gegenproben.ipynb`.

## Aufgabe 1: Ausgangslage

Erste Zelle:

```text
34267 Zeilen nach Bereinigung, Monate 2024-01 bis 2026-10
```

Prüfzelle mit dem unveränderten Kommentar:

```text
nicht OK – (a) Umsatz Oktober: Zahl im Text mit Gegenprobe 1 (Zeile Gesamt) vergleichen.
nicht OK – (b) Relaunch: Aussage „um 20 %“ ersetzen und das Gesamtwachstum aus Gegenprobe 2 nennen.
nicht OK – (c) Regionen: „alle Regionen“ ersetzen und den Rückgang aus Gegenprobe 3 nennen.
```

## Aufgabe 2: Gegenprobe 1 – falsche Zahl (a)

```text
           Umsatz   Vormonat  Δ Vormonat %    Vorjahr  Δ Vorjahr %    Plan  Δ Plan %  Deckungsbeitrag  Marge %
Region
Nord    101463.16  103872.09          -2.3   99371.29          2.1  104000      -2.4         20534.58     20.2
Ost      52972.84   58995.87         -10.2   58005.14         -8.7   60000     -11.7         11381.24     21.5
Süd      79597.38   83138.94          -4.3   76658.34          3.8   81000      -1.7         16101.07     20.2
West    103105.62   97374.84           5.9   93514.22         10.3  101000       2.1         21433.42     20.8
Gesamt  337139.00  343381.74          -1.8  327548.99          2.9  346000      -2.6         69450.31     20.6
```

| im Kommentar | im Bericht | Ergebnis |
| --- | --- | --- |
| 373.139 € | 337.139,00 € | **falsch** (Ziffern vertauscht) |
| +2,9 % zum Vorjahresmonat | 2.9 | richtig |
| Plan 346.000 €, um 2,6 % verfehlt | 346000, −2.6 | richtig |
| Marge 20,6 % | 20.6 | richtig |

Plausibilität ohne Bericht: 373.139 € wären gegenüber 327.549 € im Vorjahr +13,9 %, nicht +2,9 %. Die Zahl passt nicht zum Prozentwert daneben.

Korrektur: „Der Umsatz im Oktober 2026 betrug **337.139 €** und lag damit 2,9 % über dem Vorjahresmonat.“

## Aufgabe 3: Gegenprobe 2 – behauptete Ursache (b)

```text
             Apr–Okt 2025  Apr–Okt 2026   Δ %  Anteil 2025 %  Anteil 2026 %
kanal
Außendienst     1602810.2     1541379.1  -3.8           78.2           70.1
Onlineshop       446635.5      656559.8  47.0           21.8           29.9
Gesamt          2049445.7     2197938.9   7.2          100.0          100.0
```

- „Um 20 % gesteigert“ stimmt mit keiner Zeile überein: gesamt +7,2 %, Onlineshop +47,0 %, Außendienst −3,8 %.
- Der Onlineshop-Anteil steigt von 21,8 % auf 29,9 %; ein Teil des Online-Wachstums ist Verlagerung aus dem Außendienst.
- „Hat gesteigert“ behauptet eine Ursache, die der Vergleich nicht belegen kann.

Korrektur:

> Seit dem Relaunch im März 2026 wächst der Onlineshop deutlich: Von April bis Oktober 2026 lag sein Umsatz 47,0 % über denselben Monaten 2025, der Außendienst 3,8 % darunter. Der Gesamtumsatz stieg im selben Zeitraum um 7,2 %. Ein Teil des Online-Wachstums ist eine Verlagerung aus dem Außendienst; wie viel davon auf den Relaunch zurückgeht, zeigen diese Zahlen allein nicht.

## Aufgabe 4: Gegenprobe 3 – Verallgemeinerung (c)

```text
        Okt 2025  Okt 2026  Δ Vorjahr %  Anteil Okt 2026 %
region
Nord     99371.3  101463.2          2.1               30.1
Ost      58005.1   52972.8         -8.7               15.7
Süd      76658.3   79597.4          3.8               23.6
West     93514.2  103105.6         10.3               30.6
```

„Alle Regionen sind gewachsen“ ist falsch: Ost liegt 8,7 % unter Oktober 2025. Der Gesamtwert (+2,9 %) verdeckt das, weil Ost nur 15,7 % des Umsatzes ausmacht.

Korrektur:

> Drei von vier Regionen sind gegenüber dem Vorjahresmonat gewachsen, allen voran West mit +10,3 %. Ost lag mit 52.973 € um 8,7 % unter Oktober 2025 und 11,7 % unter Plan.

## Aufgabe 5: korrigierter Kommentar und Prüfzelle

Vollständiger Text: [kommentar_oktober_korrigiert.md](../../project/examples/m08-validation/l01-fact-check/kommentar_oktober_korrigiert.md). Prüfzelle:

```text
OK – (a) Umsatz Oktober wie im Bericht.
OK – (b) Relaunch-Aussage mit dem gemessenen Gesamtwachstum.
OK – (c) Regionen-Aussage nennt den Rückgang.
OK – alle drei Korrekturen sind belegt.
```

| Fehler | stand im Entwurf | Korrektur | Beleg |
| --- | --- | --- | --- |
| (a) | 373.139 € | 337.139 € | Gegenprobe 1, Zeile Gesamt |
| (b) | „hat den Umsatz um 20 % gesteigert“ | Onlineshop +47,0 %, Außendienst −3,8 %, gesamt +7,2 % (Apr–Okt 2026 gegen 2025), Ursache offen | Gegenprobe 2 |
| (c) | „Alle Regionen sind … gewachsen“ | drei von vier; Ost −8,7 % | Gegenprobe 3 |

Der Ausblick („rund 375.000 €“ für November) ist richtig: Der Oktober-Bericht nennt als Prognose 375.345 €.

## Erweiterung: Kommentar des Skills prüfen

Hier kann keine Agent-Antwort gezeigt werden; geprüft wird nach diesem Schema:

| Aussage im Skill-Kommentar | prüfen mit | Erwartung |
| --- | --- | --- |
| Umsatz, Vorjahr, Plan, Marge, Regionen | Gegenprobe 1 | Zahlen identisch mit der Kennzahlentabelle; der Skill liefert sie aus dem Skript |
| Aussage zum Relaunch | Gegenprobe 2 | Der Bericht des Skills enthält **keine** Zahlen je Kanal. Eine Prozentzahl zum Onlineshop im Kommentar stammt nicht aus dem Skript → Skill-Regel 3: selbst gerechnet oder erfunden |
| „alle“, „überall“ | Gegenprobe 3 | Ost −8,7 % muss genannt sein |

Eine gute Antwort sagt offen, dass der Bericht keine Aufteilung nach Kanal enthält und die Frage nach dem Relaunch damit nicht beantwortet werden kann.
