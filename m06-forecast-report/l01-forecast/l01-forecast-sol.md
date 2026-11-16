# Lab 6.1 – Lösung: Umsatz prognostizieren

Fertiger Stand: [project/examples/m06-forecast-report/l01-forecast/](../../project/examples/m06-forecast-report/l01-forecast/) mit `prognose.ipynb` (ausgeführt, mit Erweiterung „Spanne“), `prognose_2026.csv` und `prognose_2026.html`.

## Aufgabe 1: Monatsumsatz und naive Prognose

```text
33 Monate von 2024-01 bis 2026-09
Naive Prognose für 2026-10: 327549
```

## Aufgabe 2: Funktion `prognose_einfach`

Lösungs-Snippet:

```python
# >>> AUFGABE 1: Funktion prognose_einfach(umsatz, monat, stand) schreiben – Prompt siehe Übung, Aufgabe 3
def prognose_einfach(umsatz, monat, stand):
    """Vorjahresmonat × Trendfaktor (letzte 12 Monate bis stand / die 12 Monate davor)."""
    bekannt = umsatz[umsatz.index <= stand]                     # nur Monate bis einschließlich stand
    trendfaktor = bekannt.iloc[-12:].sum() / bekannt.iloc[-24:-12].sum()
    return umsatz[vorjahresmonat(monat)] * trendfaktor
# <<< ENDE AUFGABE 1
```

Ausgabe der Prüfzelle:

```text
OK – 2026-04: 288.113 € (Vorjahr 272.033 € × Trendfaktor 1,059); 2026-10: 354.164 €
```

- `umsatz.index <= stand` vergleicht Texte wie `"2026-03"`; das funktioniert, weil das Format JJJJ-MM alphabetisch und zeitlich gleich sortiert.
- Mit Stand 2026-03 ist der Trendfaktor 1,059, mit Stand 2026-09 schon 1,081: Die letzten Monate sind stärker gewachsen.

## Aufgabe 3: zweiter Versuch

| KI-Code | Prüfzelle |
| --- | --- |
| Trendfaktor über die ganze Series ohne Filter auf `stand` | `nicht OK – Prognose 2026-04 mit Stand 2026-03 ist 294,137 statt 288,113 …` |
| `umsatz.pct_change(12).mean()` als Wachstum | anderer Wert, `nicht OK` mit Hinweis auf die Formel |
| Vorjahresmonat selbst mit `monat - 12` gerechnet | `TypeError` (Text minus Zahl); fertige Funktion `vorjahresmonat` nutzen |

## Aufgabe 4: Backtest

```text
MAPE naiv:    7.7 %
MAPE einfach: 4.8 %
```

| monat | ist | naiv | einfach | fehler_naiv_prozent | fehler_einfach_prozent |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2026-04 | 295548.1 | 272033.2 | 288113.1 | -8.0 | -2.5 |
| 2026-05 | 303560.7 | 292847.2 | 310157.4 | -3.5 | 2.2 |
| 2026-06 | 295463.3 | 246399.1 | 260963.8 | -16.6 | -11.7 |
| 2026-07 | 293057.1 | 257978.9 | 273228.0 | -12.0 | -6.8 |
| 2026-08 | 329789.0 | 324778.3 | 343976.0 | -1.5 | 4.3 |
| 2026-09 | 343381.7 | 327860.0 | 347239.9 | -4.5 | 1.1 |

Die naive Prognose liegt in allen sechs Monaten zu tief, weil sie das Wachstum nicht kennt. Die einfache Prognose liegt mal darüber, mal darunter.

## Aufgabe 5: Prognose Oktober–Dezember 2026

| monat | naiv | einfach |
| --- | ---: | ---: |
| 2026-10 | 327549 | 354164 |
| 2026-11 | 347316 | 375537 |
| 2026-12 | 295129 | 319110 |

Diagrammtitel: `Prognose Q4 2026: 1.05 Mio. € (Backtest: im Schnitt 4.8 % daneben)`. Ein Satz für die Geschäftsführung: „Für das vierte Quartal erwarten wir rund 1,05 Mio. € Umsatz; die Methode lag in den letzten sechs Monaten im Schnitt knapp 5 % daneben, Großaufträge und Kundenverluste sind nicht enthalten.“

## Erweiterung

**Spanne ± MAPE** (im Beispiel enthalten):

```python
# Spanne: Prognose ± Backtest-MAPE als graue Fläche
unten = vorschau["umsatz"] * (1 - mape_einfach / 100)
oben = vorschau["umsatz"] * (1 + mape_einfach / 100)
fig.add_scatter(x=vorschau["monat"], y=oben, mode="lines", line=dict(width=0), showlegend=False)
fig.add_scatter(x=vorschau["monat"], y=unten, mode="lines", line=dict(width=0), fill="tonexty",
                fillcolor="rgba(128,128,128,0.25)", name=f"± {mape_einfach:.1f} % (MAPE)")
fig
```

`fill="tonexty"` füllt die Fläche zwischen der unteren und der zuvor gezeichneten oberen Linie. Für Oktober 2026 reicht die Spanne von rund 337.000 € bis 371.000 €.

**Backtest je Region:**

```python
je_region = df.groupby(["region", "monat"])["umsatz"].sum()
for region in ["Nord", "Ost", "Süd", "West"]:
    u = je_region[region]                                    # Monatsumsatz dieser Region
    bt = pd.DataFrame({"ist": [u[m] for m in TESTMONATE]})
    bt["naiv"] = [prognose_naiv(u, m, "2026-03") for m in TESTMONATE]
    bt["einfach"] = [prognose_einfach(u, m, "2026-03") for m in TESTMONATE]
    mape_n = ((bt["naiv"] / bt["ist"] - 1).abs().mean() * 100).round(1)
    mape_e = ((bt["einfach"] / bt["ist"] - 1).abs().mean() * 100).round(1)
    print(f"{region:<5} MAPE naiv {mape_n:>5} %   MAPE einfach {mape_e:>5} %")
```

| Region | Trendfaktor (Stand 2026-03) | MAPE naiv | MAPE einfach |
| --- | ---: | ---: | ---: |
| Nord | 1,039 | 6,8 % | 5,5 % |
| Ost | 1,043 | 7,0 % | 8,8 % |
| Süd | 1,042 | 9,5 % | 6,6 % |
| West | 1,109 | 12,4 % | 9,6 % |

Je Region sind die Fehler größer als für die Summe, weil sich Zufallsschwankungen der Regionen in der Summe teilweise ausgleichen. In Ost ist die einfache Prognose schlechter als die naive: Der Trendfaktor über 12 Monate (+4 %) passt nicht zur schrumpfenden Region.
