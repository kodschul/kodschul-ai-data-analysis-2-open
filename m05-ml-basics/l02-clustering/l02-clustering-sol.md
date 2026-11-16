# Lab 5.2 – Lösung: Kundensegmente mit Clustering

Fertiger Stand: [project/examples/m05-ml-basics/l02-clustering/](../../project/examples/m05-ml-basics/l02-clustering/) mit `segmente.ipynb` (ausgeführt), `kunden_segmente.csv` und `segmente.html`.

## Aufgabe 1: Starter kopieren

`project/playground/m05-l02-segmente.ipynb` ist geöffnet; Ausgaben gibt es erst nach dem Ausführen.

## Aufgabe 2: Segmente und Kennzahlen

Nach dem Skalieren haben alle drei Spalten Mittelwert 0,0 und Standardabweichung 1,0. Segmentgrößen und Kennzahlen:

| segment | kunden | tage_seit_kauf | haeufigkeit | umsatz | umsatz_summe | anteil_umsatz_prozent |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 14 | 2 | 443 | 191977 | 2687683 | 27.4 |
| 2 | 90 | 4 | 157 | 45684 | 4111553 | 42.0 |
| 3 | 55 | 302 | 54 | 13040 | 717216 | 7.3 |
| 4 | 241 | 27 | 41 | 9474 | 2283298 | 23.3 |

Im Streudiagramm liegen die 14 Top-Kunden oben rechts (bis 703 Buchungen, bis 311.637 €); Segment 3 und 4 überlappen unten links, weil sie sich vor allem in `tage_seit_kauf` unterscheiden.

## Aufgabe 3: Spalte `segment_name`

Lösungs-Snippet:

```python
# >>> AUFGABE 1: Spalte segment_name mit einem Namen je Segment ergänzen – Prompt siehe Übung, Aufgabe 3
namen = {
    1: "Top-Kunden",           # wenige Kunden, sehr viele Buchungen, höchster Umsatz
    2: "Stammkunden",          # kaufen laufend, mittlerer bis hoher Umsatz
    3: "Abgesprungen",         # letzter Kauf im Schnitt vor rund 300 Tagen
    4: "Gelegenheitskunden",   # aktiv, aber wenige Buchungen und kleiner Umsatz
}
kunden["segment_name"] = kunden["segment"].map(namen)
# <<< ENDE AUFGABE 1
kunden.groupby(["segment", "segment_name"], dropna=False).size()
```

Ausgabe der Prüfzelle:

```text
OK – 1 = Top-Kunden, 2 = Stammkunden, 3 = Abgesprungen, 4 = Gelegenheitskunden
```

- `map(namen)` setzt für jede Segmentnummer den Namen aus dem dict ein; alle Kunden eines Segments bekommen denselben Namen.
- Andere Namen („A-Kunden“, „Inaktiv“, „Neukunden-Potenzial“) sind ebenso richtig, solange jedes Segment genau einen eigenen Namen hat.

## Aufgabe 4: zweiter Versuch

Häufige Abweichungen in KI-Antworten und ihre Prüfmeldung:

| KI-Code | Prüfzelle |
| --- | --- |
| dict mit Schlüsseln `0` bis `3` (alte k-Means-Nummern) | `nicht OK – Spalte segment_name fehlt oder ist leer …` (Segment 4 bekommt keinen Namen) |
| Namen als Zeichenkette `"1"` statt Zahl `1` im dict | `nicht OK – … leer …` |
| zweimal derselbe Name | `nicht OK – 3 verschiedene Namen statt 4 …` |

## Aufgabe 5: Ergebnis speichern

```text
Gespeichert: project/playground/kunden_segmente.csv und project/playground/segmente.html
```

Erste Zeilen von `kunden_segmente.csv`:

```text
kunde_id,tage_seit_kauf,haeufigkeit,umsatz,segment,segment_name
K0001,1,64,10343.82,4,Gelegenheitskunden
K0002,26,38,7411.2,4,Gelegenheitskunden
```

## Erweiterung: Elbow und 3 oder 5 Segmente

Abstand innerhalb der Segmente (`inertia_`) für 1 bis 8 Segmente: 1200,0 · 683,7 · 349,9 · 204,4 · 149,8 · 116,5 · 85,4 · 67,8. Bis 3–4 Segmente fällt die Kurve stark, danach nur noch wenig.

| Segmente | Kunden je Segment (nach Ø Umsatz) | Was sich ändert |
| --- | --- | --- |
| 3 | 19 · 326 · 55 | Top- und Stammkunden teilen sich anders auf; Stamm- und Gelegenheitskunden verschmelzen zu einem großen Segment mit 326 Kunden |
| 4 | 14 · 90 · 55 · 241 | Kursstand |
| 5 | 3 · 15 · 88 · 55 · 239 | drei Großkunden (Ø 291.432 €) bilden ein eigenes Segment; für ein Vertriebsteam kaum eine eigene Behandlung wert |

Das Segment „Abgesprungen“ (55 Kunden, Ø 302 Tage) bleibt in allen drei Varianten gleich: Es ist das stabilste Muster in den Daten.
