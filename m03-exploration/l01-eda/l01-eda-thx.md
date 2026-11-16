# Lab 3.1: Muster finden: explorative Analyse

**Leitfragen:**

<details>
<summary>Welche drei Fragen stellt die Geschäftsführung zu jedem Monatsbericht?</summary>

Meist: Wo wachsen wir, wo nicht? Womit verdienen wir Geld? Was hat sich verändert? Genau diese drei Fragen beantwortet das Notebook dieses Labs für Nordwind: Wachstum je Region, Marge je Produktgruppe, Entwicklung der Kanäle.

</details>

<details>
<summary>Steigt der Umsatz, weil mehr Kunden kaufen oder weil sie mehr kaufen?</summary>

Das zeigt erst eine Zerlegung: Anzahl Kunden und Umsatz je Kunde getrennt zählen. Bei Nordwind kaufen Januar bis September 2026 weniger Kunden als im Vorjahr (367 statt 398), aber jeder kauft im Schnitt mehr (Beispiel-Notebook, Erweiterung).

</details>

<details>
<summary>Wie viel ist „auffällig" bei einer Abweichung zum Vorjahr?</summary>

Es kommt auf die übliche Schwankung an. Region Ost lag 2025 bei −7,1 % und springt 2026 auf +9,1 %: Ein solcher Bruch ist ein Anlass nachzufragen, kein Befund. Eine feste Regel dafür folgt in Lab 5.3.

</details>

- Explorative Datenanalyse heißt: Fragen an die Daten stellen und mit Tabellen beantworten, bevor ein Bericht oder Modell entsteht.
- Werkzeuge sind die pandas-Bausteine aus Lab 2.1 (`groupby`, `pivot_table`, `describe`) plus `pct_change` für Veränderungen.

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Explorative Datenanalyse (EDA) | Daten erkunden: verteilen, gruppieren, über die Zeit ansehen, vergleichen, bevor man Schlüsse zieht |
| Verteilung | wie sich die Werte einer Spalte verteilen: kleinster, größter, typischer Wert |
| Veränderungsrate | (neu − alt) / alt, z. B. Umsatz gegen Vorjahr in %; in pandas `pct_change` |
| Year-to-Date (YTD) | „seit Jahresbeginn": Januar bis zum aktuellen Monat, verglichen mit denselben Monaten im Vorjahr |
| Korrelation | zwei Größen bewegen sich gemeinsam; sagt nichts darüber, was die Ursache ist |
| Data Viewer | Tabellenansicht in VS Code für eine Variable aus dem Notebook, mit Filter und Sortierung |

## Vier Blickwinkel einer EDA

| Blickwinkel | Frage | pandas | Im Notebook |
| --- | --- | --- | --- |
| Verteilung | Welche Werte sind typisch, welche extrem? | `describe()` | Überblick |
| Gruppen | Welche Gruppe ist größer, besser? | `groupby(...).sum()` | Frage 2 |
| Zeitverlauf | Wie entwickelt es sich Monat für Monat? | `pivot_table(index="monat", ...)` | Frage 3 |
| Zusammenhang | Bewegen sich zwei Größen gemeinsam? | `corr()` | nur Einordnung |

Schon `describe()` zeigt etwas: Der größte Einzelumsatz ist 32.800 €, drei Viertel aller Buchungen liegen unter 350 €. Solche Werte sind zuerst ein Grund nachzusehen.

![Anscombe-Quartett: vier Streudiagramme mit gleichem Mittelwert, gleicher Streuung und gleicher Korrelation, aber völlig verschiedenen Formen](https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/960px-Anscombe%27s_quartet_3.svg.png)

_Quelle: Anscombe's quartet, Schutz und Avenue, Wikimedia Commons (https://commons.wikimedia.org/wiki/File:Anscombe%27s_quartet_3.svg), CC BY-SA 3.0, abgerufen am 15.11.2026._

Das Anscombe-Quartett (Francis Anscombe, 1973): vier Datensätze mit denselben Kennzahlen, aber ganz anderem Bild. Kennzahlen allein reichen nicht, man muss die Daten ansehen.

## Die drei Fragen an die Nordwind-Daten

Eingabe ist `umsatz_features.csv` aus dem Beispiel von Lab 2.3 (33.156 Zeilen, 01/2024–09/2026).

```python
df = pd.read_csv(EINGABE, parse_dates=["datum"])            # datum gleich als Datum lesen

# Frage 1: Umsatz Januar–September je Region und Jahr, Veränderung zum Vorjahr
zeitraum = df[df["datum"].dt.month <= 9]                     # gleiche Monate in jedem Jahr
tabelle = zeitraum.pivot_table(index="region", columns="jahr", values="umsatz", aggfunc="sum")
veraenderung = tabelle.pct_change(axis="columns") * 100     # Spalte gegen Spalte davor

# Frage 2: Marge je Produktgruppe aus den Summen (Regel aus Lab 2.3)
summen = df.groupby("produktgruppe")[["umsatz", "deckungsbeitrag"]].sum()
summen["marge_prozent"] = summen["deckungsbeitrag"] / summen["umsatz"] * 100
```

| Frage | Ergebnis im Beispiel |
| --- | --- |
| 1 · Wachstum je Region (Jan.–Sep. 2026 zum Vorjahr) | West +9,8 %, Süd +9,2 %, Ost +9,1 %, Nord +4,3 % |
| 2 · Marge je Produktgruppe (01/2024–09/2026) | Schreibwaren 34,8 % … Technik 14,2 % |
| 3 · Kanäle je Monat | Onlineshop-Anteil von rund 22 % (2024/2025) auf 30,1 % im September 2026 |

`pct_change` rechnet immer gegen die vorherige Zeile oder, mit `axis="columns"`, gegen die vorherige Spalte. Darum werden nur gleiche Zeiträume verglichen: 2026 liegt erst bis September vor, ein Vergleich mit dem ganzen Jahr 2025 ergäbe scheinbar −21 %.

Das Ost-Plus von 9,1 % passt nicht zum Vorjahr (−7,1 %). Der größte Teil davon ist eine einzelne Buchung vom 10.02.2026 über 32.800 €, genau der Höchstwert aus `describe()`.

## Ergebnistabellen ansehen

Im Notebook erscheint eine Tabelle unter der Zelle. Größere Tabellen öffnet die Ansicht **Jupyter: Variables** (Schaltfläche **Variables** in der Notebook-Leiste) mit dem Symbol neben der Variable im **Data Viewer**: filtern und sortieren wie in Excel, ohne Code.

![VS Code Data Viewer: eine Tabelle aus einem Notebook mit Filterfeldern über jeder Spalte](https://code.visualstudio.com/assets/docs/datascience/jupyter/data-viewer.png)

_Quelle: Visual Studio Code Docs, „Jupyter Notebooks in VS Code" (https://code.visualstudio.com/docs/datascience/jupyter-notebooks), abgerufen am 15.11.2026. Stand: 11/2026, vor Kursbeginn prüfen._

## Korrelation ist keine Ursache

![Punktwolken mit Korrelationswerten von 1 bis −1 sowie Beispiele mit Korrelation 0 trotz klarer Form](https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/Correlation_examples2.svg/960px-Correlation_examples2.svg.png)

_Quelle: Correlation examples2, DenisBoigelot, Wikimedia Commons (https://commons.wikimedia.org/wiki/File:Correlation_examples2.svg), CC0, abgerufen am 15.11.2026._

- Die Korrelation ist eine Zahl zwischen −1 und 1: 1 = steigen immer gemeinsam, 0 = kein linearer Zusammenhang.
- Beispiel Nordwind: Seit März 2026 wächst der Onlineshop. Ob der Relaunch die Ursache ist oder Kunden nur vom Außendienst wechseln, sagt eine Korrelation nicht; das prüft Lab 8.1 mit einer Gegenprobe.

## KI als Ideengeber

Copilot findet schnell weitere Fragen an eine Tabelle, wenn Spalten und Zweck im Prompt stehen. Die Antwort sind Ideen, keine Ergebnisse: Jede Frage wird erst durch eine Rechnung im Notebook beantwortet.

## Typische Fehler

| Symptom | Ursache | Lösung |
| --- | --- | --- |
| `AttributeError: Can only use .dt accessor` | `datum` ist Text | `pd.read_csv(..., parse_dates=["datum"])` |
| 2026 zeigt rund −21 % | Teiljahr mit ganzem Jahr verglichen | Zeitraum auf dieselben Monate begrenzen |
| Marge je Gruppe zu hoch | Mittelwert der Zeilenmarge gebildet | Summe Deckungsbeitrag / Summe Umsatz |
| `FileNotFoundError` | Notebook läuft nicht im Kursordner | Kursordner in VS Code öffnen, Zelle erneut ausführen |

## Fazit

- EDA beantwortet wenige klare Fragen mit Tabellen, bevor Diagramme oder Berichte entstehen.
- Vergleiche brauchen gleiche Zeiträume; Margen entstehen aus Summen.
- Auffällige Werte sind Fragen an die Daten, keine Ergebnisse.

In der Übung entstehen die drei Ergebnistabellen; die dritte mit einem vorgegebenen Prompt.
