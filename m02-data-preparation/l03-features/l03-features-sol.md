# Lab 2.3 – Lösung: Kennzahlen ableiten und gegenprüfen

## Aufgabe 1: Starter ausführen

```text
Zeilen:                33156
Zeilen ohne Kosten:      648
nicht OK  Spalte marge fehlt – Code aus Aufgabe 1 zwischen die Markierungen setzen
Gespeichert: project/playground/umsatz_features.csv
```

## Aufgabe 2: Antwort von Copilot

Der Vorschlag passt, wenn er `df["deckungsbeitrag"] / df["umsatz"]` rechnet, nicht mit 100 multipliziert und kein `fillna(0)` oder `dropna()` enthält.

## Aufgabe 3: Lösungs-Snippet für AUFGABE 1

```python
    # >>> AUFGABE 1: Spalte marge = Deckungsbeitrag / Umsatz – Prompt siehe Übung, Aufgabe 2
    df["marge"] = df["deckungsbeitrag"] / df["umsatz"]            # Anteil, z. B. 0.25 = 25 %
    # <<< ENDE AUFGABE 1
```

```text
Zeilen:                33156
Zeilen ohne Kosten:      648
OK        marge = Deckungsbeitrag / Umsatz in jeder Zeile (leer, wo Kosten fehlen)
Gespeichert: project/playground/umsatz_features.csv
```

Erste Zeile der Datei: Umsatz 39,89 €, Kosten 25,92 €, `monat` 2024-01, `quartal` 2024Q1, `deckungsbeitrag` 13,97, `marge` 0,350.

## Aufgabe 4: Gegenprüfung

```bash
python check_zahlen.py project/playground/umsatz_features.csv
```

```text
Prüfung von project/playground/umsatz_features.csv gegen data/kontrollsummen.csv
Monate: 33 (2024-01 bis 2026-09), Regionen: Nord, Ost, Süd, West
Verglichen: 132 Monat-Region-Werte je Kennzahl
Ergebnis: 0 Abweichungen – Prüfung bestanden
```

132 = 33 Monate × 4 Regionen. `check_zahlen.py` nutzt die Spalte `marge` der Datei nicht: Es rechnet die Marge je Monat und Region selbst aus den Summen. Darum prüft es unabhängig.

## Erweiterung: `kunden_rfm`

Beispiel-Prompt:

> Kontext: In #file:m02-l03-features.py liegt nach `add_features` ein pandas-DataFrame `df` mit einer Zeile je Buchung, `datum` ist ein Datum.
> Spalten: kunde_id, beleg_nr, datum, umsatz.
> Regel: Nur Buchungen bis einschließlich Stichtag. Je Kunde: Tage zwischen letztem Kauf und Stichtag, Anzahl Buchungen, Umsatzsumme, auf 2 Stellen gerundet.
> Gewünschte Ausgabe: Funktion `kunden_rfm(df, stichtag)`, die einen DataFrame mit den Spalten kunde_id, tage_seit_kauf, haeufigkeit, umsatz zurückgibt, und zwei Zeilen im Hauptteil, die sie mit "2026-09-30" aufrufen und als ORDNER + "kunden_rfm.csv" speichern.

Geprüfte Fassung (wie im Beispiel [`features.py`](../../project/examples/m02-data-preparation/l03-features/features.py)):

```python
def kunden_rfm(df, stichtag):
    """Je Kunde: wie lange her (Tage), wie oft (Buchungen), wie viel (Umsatz)."""
    bis = df[df["datum"] <= stichtag]
    rfm = bis.groupby("kunde_id").agg(
        letzter_kauf=("datum", "max"),
        haeufigkeit=("beleg_nr", "count"),
        umsatz=("umsatz", "sum"),
    )
    rfm["tage_seit_kauf"] = (pd.Timestamp(stichtag) - rfm["letzter_kauf"]).dt.days
    return rfm[["tage_seit_kauf", "haeufigkeit", "umsatz"]].round(2).reset_index()
```

Im Hauptteil nach `df.to_csv(...)`:

```python
    rfm = kunden_rfm(df, "2026-09-30")
    rfm.to_csv(ORDNER + "kunden_rfm.csv", index=False)
```

Ergebnis: 400 Kunden, identisch mit dem Beispiel; erste Zeilen K0001 (1 Tag, 64 Buchungen, 10.343,82 €), K0002 (26, 38, 7.411,20 €), K0003 (345, 74, 18.149,81 €).
