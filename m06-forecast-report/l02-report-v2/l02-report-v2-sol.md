# Lab 6.2 – Lösung: Der Bericht v2 mit Excel-Export

Fertiger Stand: [project/examples/m06-forecast-report/l02-report-v2/monatsbericht.py](../../project/examples/m06-forecast-report/l02-report-v2/monatsbericht.py) mit den gespeicherten Ausgaben `berichte/bericht_2026_09_v2.html` und `berichte/kpi_2026_09.xlsx` (Basis und Erweiterung: zwei Blätter). Diese Fassung wird in Lab 7.2 zum Skill.

## Aufgabe 1: Hilfe

```text
usage: monatsbericht.py [-h] {bericht,auffaelligkeiten,prognose} ...

Monatsbericht v2: Kennzahlen, Segmente, Auffälligkeiten und Prognose aus allen
Lieferungen eines Ordners.

positional arguments:
  {bericht,auffaelligkeiten,prognose}
    bericht             HTML-Bericht mit allen Abschnitten
    auffaelligkeiten    nur die auffälligen Tage des Monats
    prognose            nur die Prognose der nächsten Monate
```

`bericht --help` listet die Optionen `--daten`, `--muster`, `--monat`, `--schwelle`, `--ausgabe` und `--excel` mit ihren Standardwerten (`data`, `nordwind_umsatz*.csv`, letzter Monat, 3, `berichte`).

## Aufgabe 2: Bericht September 2026

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

Summenkontrolle: 2026-09 – 1.144 Zeilen, Summe Umsatz 343.381,74 – stimmt mit der Kennzahlentabelle überein
Sollwert-Prüfung: bestanden (12 Werte für 2026-09 gegen kontrollsummen.csv)
```

| Abschnitt im HTML | stammt aus | Inhalt September 2026 |
| --- | --- | --- |
| Prüfung | v2 neu | die zwei Prüfzeilen |
| Qualitätscheck | Lab 2.1/2.2 | Dubletten, fehlende Kosten, 14 → 4 Schreibweisen |
| Kennzahlen | Lab 3.3 | Tabelle oben + Balken Ist/Vorjahr/Plan |
| Kundensegmente | Lab 5.2 | 14 · 90 · 55 · 241 Kunden, Streudiagramm |
| Auffälligkeiten | Lab 5.3 | 01.09.2026 Süd (Abstand 3,1), 24.09.2026 Ost (3,2) |
| Prognose | Lab 6.1 | 354.164 · 375.537 · 319.110 €, Trendfaktor 1,081 |

## Aufgabe 3: `--excel` mit leerer Funktion

```text
nicht OK – berichte/kpi_2026_09.xlsx fehlt: Funktion export_excel schreibt noch keine Datei
```

Der HTML-Bericht entsteht trotzdem; nur die Excel-Datei fehlt.

## Aufgabe 4: Funktion `export_excel`

Lösungs-Snippet (Basis):

```python
def export_excel(kpi, auffaellige, pfad):
    """Schreibt die Kennzahlentabelle als Blatt "Kennzahlen" in die Excel-Datei pfad.

    kpi: Kennzahlen je Region (Index = Region), auffaellige: auffällige Tage (Erweiterung: zweites Blatt).
    """
    # >>> AUFGABE 1: Blatt "Kennzahlen" mit pandas nach Excel schreiben – Prompt siehe Übung, Aufgabe 4
    kpi.to_excel(pfad, sheet_name="Kennzahlen")
    # <<< ENDE AUFGABE 1
```

Ausgabe nach dem erneuten Lauf mit `--excel`:

```text
OK – berichte/kpi_2026_09.xlsx mit 5 Zeilen im Blatt 'Kennzahlen' (Blätter: Kennzahlen)
```

## Aufgabe 5: zweiter Versuch und Excel-Datei

| KI-Code | Meldung |
| --- | --- |
| `kpi.to_excel(pfad, sheet_name="Kennzahlen", index=False)` | `OK`, aber die Spalte Region fehlt in Excel (sie steckt im Index) – `index=False` entfernen |
| Blatt `"KPI"` oder `"Sheet1"` | `nicht OK – Blatt 'Kennzahlen' fehlt, gefunden: KPI` |
| eigener fester Dateiname statt `pfad` | `nicht OK – berichte/kpi_2026_09.xlsx fehlt …` |
| Zeilen ohne Einrückung eingefügt | `IndentationError` beim Start – Zeilen vier Leerzeichen einrücken |

Blatt „Kennzahlen“ in `kpi_2026_09.xlsx`:

| Region | Umsatz | Vormonat | Δ Vormonat % | Vorjahr | Δ Vorjahr % | Plan | Δ Plan % | Deckungsbeitrag | Marge % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Nord | 103872.09 | 101046.86 | 2.8 | 103297.45 | 0.6 | 108000 | -3.8 | 21085.71 | 20.3 |
| Ost | 58995.87 | 57563.11 | 2.5 | 61560.70 | -4.2 | 63000 | -6.4 | 12163.13 | 20.6 |
| Süd | 83138.94 | 79258.85 | 4.9 | 75062.71 | 10.8 | 80000 | 3.9 | 16967.93 | 20.4 |
| West | 97374.84 | 91920.21 | 5.9 | 87939.19 | 10.7 | 95000 | 2.5 | 20344.76 | 20.9 |
| Gesamt | 343381.74 | 329789.03 | 4.1 | 327860.05 | 4.7 | 346000 | -0.8 | 70561.53 | 20.5 |

Die Werte sind echte Zahlen, keine Texte: In Excel lässt sich direkt weiterrechnen.

## Erweiterung

**1. Schwelle 2:**

```text
Auffällige Tage 2026-09 (Schwelle 2): 5
     Datum Region  Umsatz  Monatsmittel  Abstand (Std.-Abw.)
01.09.2026    Süd 7185.31       3779.04                  3.1
09.09.2026   Nord 8317.44       4721.46                  2.5
22.09.2026   West 7968.47       4426.13                  2.5
23.09.2026   West 7901.97       4426.13                  2.4
24.09.2026    Ost 6640.98       2681.63                  3.2
```

Schwelle 2 meldet fünf statt zwei Tage im Monat; die drei zusätzlichen sind starke, aber normale Tage. Die Prüfzeilen bleiben gleich, weil die Schwelle keine Kennzahl ändert.

**2. Zweites Blatt** (so steht es im Beispiel):

```python
    with pd.ExcelWriter(pfad) as writer:                                  # mehrere Blätter in einer Datei
        kpi.to_excel(writer, sheet_name="Kennzahlen")
        auffaellige.to_excel(writer, sheet_name="Auffaelligkeiten", index=False)
```

```text
OK – berichte/kpi_2026_09.xlsx mit 5 Zeilen im Blatt 'Kennzahlen' (Blätter: Kennzahlen, Auffaelligkeiten)
```
