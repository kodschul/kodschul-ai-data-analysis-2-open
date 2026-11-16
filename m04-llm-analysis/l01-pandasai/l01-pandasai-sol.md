# Lab 4.1 – Lösung: PandasAI: fragen, prüfen, verbessern

Beispiel-Notebook: [`project/examples/m04-llm-analysis/l01-pandasai/pandasai_fragen.ipynb`](../../project/examples/m04-llm-analysis/l01-pandasai/pandasai_fragen.ipynb). Es wurde **ohne API-Schlüssel** ausgeführt: Alle Fragezellen zeigen `Ohne Dienst – keine PandasAI-Antwort`, die Vergleichstabelle enthält zusätzlich die zwei pandas-Rechnungen der Zelle „Ohne Dienst". Es enthält keine gespeicherten Antworten von PandasAI, denn jede Antwort entsteht bei jedem Lauf neu und kann anders ausfallen. Die richtigen Werte stehen deshalb hier als pandas-Rechnung.

## Aufgabe 1: Setup und Testfrage

Mit Schlüssel: `Bereit: 33156 Zeilen, Modell gpt-4.1-mini`. Die Testfrage „Wie viele Zeilen hat die Tabelle?" muss `33156` ergeben; im Code steht eine Abfrage mit `COUNT(*)` auf `table_umsatz_features`.

## Aufgabe 2: vier Fragen und Gegenprobe

Sollwerte aus der Zelle **Gegenprobe mit pandas**:

| Frage | richtige Antwort | Woran der Code zu erkennen ist |
| --- | --- | --- |
| `a1` Umsatz September 2026 insgesamt | 343.381,74 € | `SUM(umsatz)` mit `WHERE monat = '2026-09'` |
| `a2` Produktgruppe mit dem höchsten Umsatz 2025 | Papier | `WHERE jahr = 2025`, `GROUP BY produktgruppe`, absteigend sortiert |
| `a3` verschiedene Kunden 2026 im Onlineshop | 340 | `COUNT(DISTINCT kunde_id)` mit Filter auf Jahr und Kanal |
| `a4` Umsatz je Monat als Liniendiagramm | Linie über 33 Monate | `GROUP BY monat`, danach ein Diagramm, gespeichert als PNG in `exports/charts/` |

Häufige Abweichungen: `COUNT(kunde_id)` statt `COUNT(DISTINCT kunde_id)` bei `a3` (zählt Buchungen statt Kunden), fehlender Kanalfilter, `jahr` als Text verglichen.

## Aufgabe 3 und 4: Vorher/Nachher

Sollwerte September 2026 aus `data/kontrollsummen.csv`:

| Region | Sollwert Marge |
| --- | --- |
| Nord | 20,30 % |
| Ost | 20,62 % |
| Süd | 20,41 % |
| West | 20,89 % |

| Antwort im Code | Ergebnis der Prüfzelle |
| --- | --- |
| `SUM(deckungsbeitrag) / SUM(umsatz)` mit `WHERE monat = '2026-09'` | `OK` |
| `AVG(marge)` | `nicht OK – bis zu 4,9 Prozentpunkte daneben` (Werte um 25 %) |
| kein Monatsfilter oder alle Septembermonate | `nicht OK`, Werte weichen ab |
| Antwort als Satz statt Tabelle | `nicht OK – keine Tabelle mit Region und Marge` |

Die Spaltenbeschreibung für `marge` nennt die Regel ausdrücklich („Nie mitteln … SUM(deckungsbeitrag) / SUM(umsatz)"). Damit bekommt das Modell die Rechenregel mit jeder Frage mit. Ob Vorher oder Nachher stimmt, kann von Lauf zu Lauf verschieden sein; belegt wird es nur durch die Prüfzelle und die Vergleichstabelle.

## Fallback: Zelle „Ohne Dienst"

Ausgabe im Beispiel (pandas-Rechnung, keine PandasAI-Antwort):

| Durchgang | Nord | Ost | Süd | West | Ergebnis |
| --- | --- | --- | --- | --- | --- |
| Sollwert (kontrollsummen.csv) | 20,30 | 20,62 | 20,41 | 20,89 | |
| Vorher: PandasAI ohne Beschreibungen | – | – | – | – | nicht OK – keine Tabelle mit Region und Marge |
| Nachher: PandasAI mit Beschreibungen | – | – | – | – | nicht OK – keine Tabelle mit Region und Marge |
| pandas: Mittelwert der Zeilenmargen (typischer Fehler) | 25,06 | 25,39 | 25,32 | 25,34 | nicht OK – bis zu 4,9 Prozentpunkte daneben |
| pandas: Summe DB / Summe Umsatz (Regel) | 20,30 | 20,62 | 20,41 | 20,89 | OK |

Vorher und Nachher stehen ohne Dienst als „nicht OK" in der Tabelle, weil keine Antwort vorliegt.

## Erweiterung

Gegenrechnung für die Beispielfrage „Welche drei Kunden hatten 2026 den höchsten Umsatz im Onlineshop?":

```python
online_2026 = df[(df["jahr"] == 2026) & (df["kanal"] == "Onlineshop")]
online_2026.groupby("kunde_id")["umsatz"].sum().sort_values(ascending=False).head(3)
```

Im erzeugten Code auf `WHERE` mit beiden Bedingungen, `GROUP BY kunde_id`, `ORDER BY ... DESC` und `LIMIT 3` achten.
