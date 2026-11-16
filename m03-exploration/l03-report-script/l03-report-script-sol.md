# Lab 3.3 – Lösung: Der Monatsbericht als Skript

Fertige Fassung v1: [`project/examples/m03-exploration/l03-report-script/monatsbericht.py`](../../project/examples/m03-exploration/l03-report-script/monatsbericht.py) mit Ergebnis [`bericht_2026_09.html`](../../project/examples/m03-exploration/l03-report-script/bericht_2026_09.html) und [`kpi_2026_09.csv`](../../project/examples/m03-exploration/l03-report-script/kpi_2026_09.csv). Sie unterscheidet sich vom Starter nur in `ORDNER` und den drei Zeilen aus Aufgabe 2.

## Aufgabe 1: Starter ausführen

```text
nicht OK – sauber fehlt oder hat nicht genau 4 Regionen: clean_umsatz(roh) aufrufen.
```

Das Skript stoppt vor dem Speichern; es entstehen keine Dateien.

## Aufgabe 2: Lösungs-Snippet

Zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` in `main()`:

```python
    sauber = clean_umsatz(roh)
    df = add_features(sauber)
    kpi = kpi_tabelle(df, args.monat, plan)
```

Die Reihenfolge zählt: `add_features` braucht das gelesene Datum aus `clean_umsatz`, `kpi_tabelle` die Spalten `monat` und `deckungsbeitrag` aus `add_features`.

## Aufgabe 3: Lauf mit OK

```text
OK – 4 Regionen, Summe der Regionen = Umsatz aller Buchungen im Monat (343.382 €)
Gespeichert: project/playground/bericht_2026_09.html
Gespeichert: project/playground/kpi_2026_09.csv
Prüfen mit:  python check_zahlen.py project/playground/kpi_2026_09.csv
```

## Aufgabe 4: Bericht und Prüfung

KPI-Tabelle September 2026 im Bericht:

| Region | Umsatz | Deckungsbeitrag | Marge | Vormonat | Vorjahresmonat | Plan |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Nord | 103.872 € | 21.086 € | 20,3 % | 101.047 € | 103.297 € | 108.000 € |
| Ost | 58.996 € | 12.163 € | 20,6 % | 57.563 € | 61.561 € | 63.000 € |
| Süd | 83.139 € | 16.968 € | 20,4 % | 79.259 € | 75.063 € | 80.000 € |
| West | 97.375 € | 20.345 € | 20,9 % | 91.920 € | 87.939 € | 95.000 € |
| **Gesamt** | **343.382 €** | **70.562 €** | **20,5 %** | **329.789 €** | **327.860 €** | **346.000 €** |

Diagramm-Titel im Bericht: „Onlineshop-Anteil im September: 30,1 %", „Marge im September: Schreibwaren am höchsten (34,6 %), Technik am niedrigsten (13,3 %)", „Januar bis September zum Vorjahr: West wächst am stärksten (+9,8 %)".

```text
Prüfung von project/playground/kpi_2026_09.csv gegen data/kontrollsummen.csv
Monate: 1 (2026-09 bis 2026-09), Regionen: Nord, Ost, Süd, West
Verglichen: 4 Monat-Region-Werte je Kennzahl
Ergebnis: 0 Abweichungen – Prüfung bestanden
```

## Aufgabe 5: August 2026

```bash
python project/playground/monatsbericht.py data/nordwind_umsatz.csv --monat 2026-08
python check_zahlen.py project/playground/kpi_2026_08.csv
```

```text
OK – 4 Regionen, Summe der Regionen = Umsatz aller Buchungen im Monat (329.789 €)
...
Ergebnis: 0 Abweichungen – Prüfung bestanden
```

Der Augustumsatz (329.789 €) ist genau der Vormonatswert im Septemberbericht: dieselbe Rechnung, derselbe Wert.

## Erweiterung: Plan-Abweichung

In `kpi_tabelle` vor `kpi = kpi.reset_index()`:

```python
    kpi["plan_abweichung_prozent"] = ((kpi["umsatz"] - kpi["plan"]) / kpi["plan"] * 100).round(1)
```

In `mit_gesamt` nach der Zeile mit `gesamt["marge"]` (die Abweichung der Gesamtzeile wieder aus den Summen):

```python
    gesamt["plan_abweichung_prozent"] = round((gesamt["umsatz"] - gesamt["plan"]) / gesamt["plan"] * 100, 1)
```

In `html_tabelle` Kopfzeile und Zellen ergänzen:

```python
    kopf = ["Region", "Umsatz", "Deckungsbeitrag", "Marge", "Vormonat", "Vorjahresmonat", "Plan", "Abw. Plan"]
    ...
        zellen = [z["region"], euro(z["umsatz"]), euro(z["deckungsbeitrag"]), prozent(z["marge"]),
                  euro(z["vormonat"]), euro(z["vorjahr"]), euro(z["plan"]),
                  "–" if pd.isna(z["plan_abweichung_prozent"]) else veraenderung(z["plan_abweichung_prozent"])]
```

Ergebnis September 2026: Nord −3,8 %, Ost −6,4 %, Süd +3,9 %, West +2,5 %, Gesamt −0,8 %. `check_zahlen.py` besteht weiterhin, weil es nur `umsatz`, `deckungsbeitrag` und die Marge vergleicht.
