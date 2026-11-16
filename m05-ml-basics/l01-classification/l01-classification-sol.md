# Lab 5.1 – Lösung: Wie eine Maschine aus Daten lernt

Fertiger Stand: [project/examples/m05-ml-basics/l01-classification/wiederkauf.ipynb](../../project/examples/m05-ml-basics/l01-classification/wiederkauf.ipynb), ausgeführt mit Testanteil 20 % und mit der Erweiterung.

## Aufgabe 1: Starter kopieren

Im Explorer liegt danach `project/playground/m05-l01-wiederkauf.ipynb`. Der Starter enthält keine Ausgaben; sie entstehen erst beim Ausführen.

## Aufgabe 2: Merkmale und Zielgröße

```text
33156 Buchungen von 2024-01 bis 2026-09
400 Kunden, davon kaufen wieder: 329
```

Die ersten Zeilen von `kunden.head()`:

| kunde_id | tage_seit_kauf | haeufigkeit | umsatz | wiederkauf |
| --- | ---: | ---: | ---: | ---: |
| K0001 | 15 | 53 | 8388.68 | 1 |
| K0002 | 13 | 35 | 5942.09 | 1 |
| K0003 | 253 | 74 | 18149.81 | 0 |
| K0004 | 1 | 44 | 11290.21 | 1 |
| K0005 | 20 | 68 | 18976.18 | 1 |

K0003 hat seit 253 Tagen nicht gekauft und kauft auch nach dem Stichtag nicht wieder.

## Aufgabe 3: Testanteil ändern

Lösungs-Snippet für die markierte Stelle (zweiter Lauf):

```python
# >>> AUFGABE 1: Testanteil ändern (erst 0.3, dann 0.5) – siehe Übung, Aufgabe 3
TESTANTEIL = 0.3
# <<< ENDE AUFGABE 1
```

| Testanteil | Testkunden | Genauigkeit Modell | Messlatte „alle kaufen wieder“ | Prüfzelle |
| --- | ---: | ---: | ---: | --- |
| 0.2 | 80 | 96,2 % | 77,5 % | OK |
| 0.3 | 120 | 95,0 % | 79,2 % | OK |
| 0.5 | 200 | 96,0 % | 82,5 % | OK |

Ausgabe bei 0.2:

```text
Testanteil:                          20% (80 Kunden)
Genauigkeit Modell (Testdaten):      96.2%
Messlatte 'alle kaufen wieder':      77.5%
Genauigkeit Modell (Trainingsdaten): 92.8%
OK – Testanteil 20%: Modell 96.2% liegt über der Messlatte 77.5%
```

- Das Modell liegt immer etwa 14 bis 18 Prozentpunkte über der Messlatte.
- Mit mehr Testkunden wird die Messung verlässlicher, dafür lernt das Modell aus weniger Kunden; 20–30 % sind ein üblicher Kompromiss.

## Aufgabe 4: Grenzfälle

Bei Testanteil 20 % (Auszug):

| kunde_id | tage_seit_kauf | haeufigkeit | umsatz | wiederkauf | vorhersage | wahrscheinlichkeit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| K0386 | 131 | 65 | 15602.58 | 0 | 0 | 0.28 |
| K0194 | 119 | 72 | 18092.70 | 0 | 0 | 0.39 |
| K0370 | 111 | 88 | 23781.38 | 0 | 1 | 0.52 |
| K0377 | 90 | 96 | 23995.89 | 0 | 1 | 0.58 |
| K0058 | 76 | 31 | 5317.98 | 1 | 1 | 0.67 |

Die Grenzfälle haben 2 bis 4 Monate nicht gekauft. K0370 und K0377 liegen knapp über 0,5 und sind falsch eingeordnet: Genau bei solchen Kunden lohnt ein Anruf.

## Aufgabe 5: Vergleich mit dem Beispiel

Bei Testanteil 20 % sind alle Zahlen gleich (96,2 % gegen 77,5 %), weil `random_state=42` dieselbe Aufteilung erzeugt.

## Erweiterung: Verwechslungsmatrix

```python
from sklearn.metrics import confusion_matrix

matrix = confusion_matrix(y_test, vorhersage)   # Zeilen = tatsächlich, Spalten = vorhergesagt
pd.DataFrame(matrix,
             index=["tatsächlich 0 (kauft nicht)", "tatsächlich 1 (kauft wieder)"],
             columns=["vorhergesagt 0", "vorhergesagt 1"])
```

Ergebnis bei Testanteil 20 %:

| | vorhergesagt 0 | vorhergesagt 1 |
| --- | ---: | ---: |
| tatsächlich 0 (kauft nicht) | 15 | 3 |
| tatsächlich 1 (kauft wieder) | 0 | 62 |

Alle drei Fehler sind Kunden, die abspringen, obwohl das Modell „kauft wieder“ sagt. Für den Vertrieb ist das die teurere Fehlerart; die Genauigkeit von 96,2 % allein zeigt das nicht.
