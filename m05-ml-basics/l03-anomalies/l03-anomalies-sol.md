# Lab 5.3 – Lösung: Auffälligkeiten erkennen

Fertiger Stand: [project/examples/m05-ml-basics/l03-anomalies/](../../project/examples/m05-ml-basics/l03-anomalies/) mit `auffaelligkeiten.ipynb` (ausgeführt, mit Erweiterung) und `auffaellige_tage.csv`.

## Aufgabe 1: Starter kopieren

`project/playground/m05-l03-auffaelligkeiten.ipynb` ist geöffnet.

## Aufgabe 2: Mittel und Streuung

```text
2872 Zeilen (Tag × Region)
```

| datum | region | umsatz | monat | mittel | streuung |
| --- | --- | ---: | --- | ---: | ---: |
| 2025-11-25 | West | 8268 | 2025-11 | 5517 | 4807 |
| 2025-11-26 | West | 2881 | 2025-11 | 5517 | 4807 |
| 2025-11-27 | West | 25329 | 2025-11 | 5517 | 4807 |
| 2025-11-28 | West | 4276 | 2025-11 | 5517 | 4807 |

`mittel` und `streuung` sind in allen Zeilen eines Monats gleich: `transform` schreibt den Gruppenwert in jede Zeile.

## Aufgabe 3: Funktion `find_anomalies`

Lösungs-Snippet:

```python
# >>> AUFGABE 1: Funktion find_anomalies(df, schwelle=3) schreiben – Prompt siehe Übung, Aufgabe 3
def find_anomalies(df, schwelle=3):
    """Markiert Tage, die mehr als schwelle Standardabweichungen vom Monatsmittel abweichen."""
    df = df.copy()
    df["abstand"] = (df["umsatz"] - df["mittel"]) / df["streuung"]   # in Standardabweichungen
    df["auffaellig"] = df["abstand"].abs() > schwelle                   # nach oben oder unten
    return df
# <<< ENDE AUFGABE 1
```

Ausgabe der Prüfzelle:

```text
OK – 11 auffällige Tage bei Schwelle 3, darunter 27.11.2025 West und 10.02.2026 Ost
```

- `df.copy()` lässt die Tabelle `tage` unverändert; die Funktion liefert eine neue Tabelle.
- `abs()` nimmt den Betrag, damit auch ungewöhnlich schwache Tage zählen (bei Nordwind liegt keiner unter −3).

## Aufgabe 4: zweiter Versuch

| KI-Code | Prüfzelle |
| --- | --- |
| ohne `abs()`: `df["abstand"] > schwelle` | hier zufällig ebenfalls 11 Treffer und `OK`; bei Daten mit Einbrüchen fehlen diese – `abs()` trotzdem ergänzen |
| fest `> 3` statt `> schwelle` | `nicht OK – der Parameter schwelle wird nicht verwendet …` |
| Spalte heißt `z` oder `zscore` statt `abstand` | `nicht OK – Spalten abstand und auffaellig fehlen …` |
| Mittel neu über alle Tage gerechnet (`df["umsatz"].mean()`) | `nicht OK – nicht gefunden: …` oder falsche Trefferzahl |

## Aufgabe 5: Diagramm und Liste

`auffaellige_tage.csv` nach Abstand sortiert:

| datum | region | umsatz | mittel | streuung | abstand |
| --- | --- | ---: | ---: | ---: | ---: |
| 2026-02-10 | Ost | 33969.2 | 4206.4 | 7029.4 | 4.2 |
| 2025-11-27 | West | 25329.5 | 5517.1 | 4806.7 | 4.1 |
| 2024-04-24 | West | 6505.7 | 3176.3 | 982.3 | 3.4 |
| 2024-08-08 | Süd | 6966.4 | 3350.6 | 1100.0 | 3.3 |
| 2024-10-31 | Nord | 7773.6 | 4114.0 | 1144.5 | 3.2 |
| 2026-09-24 | Ost | 6641.0 | 2681.6 | 1223.0 | 3.2 |
| 2024-01-24 | West | 5713.0 | 3264.2 | 781.5 | 3.1 |
| 2024-02-29 | West | 6366.2 | 3137.4 | 1057.0 | 3.1 |
| 2026-09-01 | Süd | 7185.3 | 3779.0 | 1095.4 | 3.1 |
| 2025-01-21 | Ost | 5553.3 | 2827.5 | 896.6 | 3.0 |
| 2026-06-01 | Ost | 4668.6 | 2186.9 | 820.0 | 3.0 |

Die zwei dokumentierten Fälle stehen oben und sind im Diagramm die einzigen Spitzen über 10.000 €. Die übrigen neun liegen knapp über 3 und sind normale starke Tage.

## Erweiterung: Schwellen vergleichen

```python
bekannt = [("2025-11-27", "West"), ("2026-02-10", "Ost")]    # die zwei dokumentierten Fälle
for schwelle in [2, 3, 4]:
    treffer = find_anomalies(tage, schwelle)
    treffer = treffer[treffer["auffaellig"]]
    gefunden = sum(((treffer["datum"] == d) & (treffer["region"] == r)).any() for d, r in bekannt)
    print(f"Schwelle {schwelle}: {len(treffer):>3} Treffer, davon {gefunden} dokumentiert, "
          f"{len(treffer) - gefunden:>3} Fehlalarme")
```

```text
Schwelle 2: 114 Treffer, davon 2 dokumentiert, 112 Fehlalarme
Schwelle 3:  11 Treffer, davon 2 dokumentiert,   9 Fehlalarme
Schwelle 4:   2 Treffer, davon 2 dokumentiert,   0 Fehlalarme
```

Schwelle 2 meldet im Schnitt mehr als drei Tage pro Monat und ist für ein Controlling-Team nicht prüfbar; Schwelle 3 meldet etwa einen Tag alle drei Monate.
