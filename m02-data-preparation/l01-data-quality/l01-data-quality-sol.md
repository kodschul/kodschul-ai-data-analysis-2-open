# Lab 2.1 – Lösung: Datenqualität prüfen

## Aufgabe 1: Prüfungen 1 bis 6

| Prüfung | Ausgabe |
| --- | --- |
| 1 Pflichtspalten | `Fehlende Pflichtspalten: []` |
| 2 `df.info()` | 33.554 Zeilen, `kosten` mit 32.897 gefüllten Werten, `datum` als `object` (Text) |
| 3 fehlende Werte | `kosten 657`, alle anderen Spalten 0 |
| 4 Dubletten | `Dubletten: 398` |
| 5 Datumsformate | `Datum mit Punkt (TT.MM.JJJJ): 7837`, `Datum mit Bindestrich (JJJJ-MM-TT): 25717` |
| 6 Ausreißer | Median 215,27 €, Maximum 32.800 €; vier Zeilen über 5.000 € (drei am 27.11.2025 West, eine am 10.02.2026 Ost) |

## Aufgabe 2: Antwort von Copilot

Der Vorschlag variiert von Lauf zu Lauf. Er passt, wenn er `value_counts()` auf `df["region"]` anwendet, das Ergebnis `regionen` nennt und `df` nicht ändert.

## Aufgabe 3: Lösungs-Snippet für AUFGABE 1

```python
# >>> AUFGABE 1: Schreibweisen der Spalte region zählen – Prompt siehe Übung, Aufgabe 2
regionen = df["region"].value_counts()   # jede Schreibweise mit ihrer Zeilenzahl
print(regionen)
# <<< ENDE AUFGABE 1
```

Die drei Lesefragen: Tabelle `df` (Rohdatei) · verändert nichts · gibt jede Schreibweise mit Anzahl aus.

```text
region
Nord           9416
West           8495
Süd            8195
Ost            5746
Region West     255
west            213
Nord            187
nord            165
Region Nord     159
Region Ost      157
Sued            156
süd             151
Region Süd      135
ost             124
Name: count, dtype: int64
```

Prüfzelle: `OK – 14 Schreibweisen für 4 Regionen gefunden.` Die zweite „Nord"-Zeile ist „Nord " mit Leerzeichen. `value_counts()` sortiert bereits absteigend.

## Aufgabe 4: Problemtabelle

| Problem | Spalte | Anzahl | Vorschlag |
| --- | --- | --- | --- |
| Dubletten (Zeile doppelt geliefert) | alle | 398 | entfernen |
| Kosten fehlen | kosten | 657 | markieren, nicht löschen |
| Datum als TT.MM.JJJJ statt JJJJ-MM-TT | datum | 7837 | beide Formate lesen |
| Schreibweisen für 4 Regionen | region | 14 | vereinheitlichen |
| Umsatz über 5.000 € in einer Zeile | umsatz | 4 | fachlich prüfen |

Gespeichert als `project/playground/probleme.csv`. Nach dem Entfernen der Dubletten bleiben 648 Zeilen ohne Kosten (einige der 657 sind doppelt geliefert); diese Zahl meldet Lab 2.2.

## Erweiterung: `quality_check.py`

Beispiel-Prompt:

> Kontext: Python-Skript mit pandas im Kursordner, Aufruf `python quality_check.py <datei.csv>`.
> Spalten: beleg_nr, datum, jahr, kunde_id, region, produktgruppe, kanal, menge, umsatz, kosten (alle Pflicht).
> Regel: Fehlt eine Pflichtspalte, nur diese melden. Sonst zählen: Dubletten, fehlende Kosten, Datum mit Punkt, Regionsnamen außer Nord/Süd/West/Ost, Umsatz über 5000 je Zeile. Die Datei nicht verändern.
> Gewünschte Ausgabe: Tabelle mit den Spalten Problem, Spalte, Anzahl, Vorschlag im Terminal. Vollständiges Skript.

Vergleichsfassung: [`quality_check.py`](../../project/examples/m02-data-preparation/l01-data-quality/quality_check.py).

```bash
python project/examples/m02-data-preparation/l01-data-quality/quality_check.py data/nordwind_umsatz.csv
```

```text
Datei: data/nordwind_umsatz.csv, 33554 Zeilen, 10 Spalten
Schreibweisen in region: 14
                              Problem Spalte  Anzahl                Vorschlag
  Dubletten (Zeile doppelt geliefert)   alle     398                entfernen
                        Kosten fehlen kosten     657 markieren, nicht löschen
Datum als TT.MM.JJJJ statt JJJJ-MM-TT  datum    7837      beide Formate lesen
  Regionsname nicht Nord/Süd/West/Ost region    1702         vereinheitlichen
    Umsatz über 5000 € in einer Zeile umsatz       4          fachlich prüfen
```

Das Skript zählt bei den Regionen die betroffenen Zeilen (1.702), das Notebook die Schreibweisen (14). Mit der defekten Lieferung:

```text
Datei: lieferungen/nordwind_umsatz_2026_10_defekt.csv, 1124 Zeilen, 10 Spalten
Schreibweisen in region: 14
            Problem Spalte  Anzahl             Vorschlag
Pflichtspalte fehlt umsatz       1 Lieferung zurückgeben
```
