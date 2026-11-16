# Lab 2.2 – Lösung: Bereinigen und transformieren

## Aufgabe 1: Starter ausführen

```text
Zeilen vorher:         33554
Dubletten entfernt:      398
Zeilen nachher:        33156
Zeilen ohne Kosten:      648
OK        keine Dubletten mehr
OK        jedes Datum gelesen
nicht OK  genau 4 Regionen
          gefunden: ['Nord', 'Nord ', 'Ost', 'Region Nord', 'Region Ost', 'Region Süd', 'Region West', 'Sued', 'Süd', 'West', 'nord', 'ost', 'süd', 'west']
Gespeichert: project/playground/umsatz_clean.csv
```

Schritte 1 bis 3 wirken bereits; nur die Regionen sind noch roh.

## Aufgabe 2: Antwort von Copilot

Der Vorschlag variiert. Er passt, wenn er nur `df["region"]` überschreibt, in der Reihenfolge strip → Vorsilbe entfernen → Groß-/Kleinschreibung → „Sued" ersetzen arbeitet und keine Zeile löscht.

## Aufgabe 3: Lösungs-Snippet für AUFGABE 1

Eingerückt um vier Leerzeichen, innerhalb von `clean_umsatz`:

```python
    # >>> AUFGABE 1: Schritt 4 – Regionen vereinheitlichen ("Region Nord", "nord", "Sued" …) – Prompt siehe Übung, Aufgabe 2
    df["region"] = (
        df["region"]
        .str.strip()                                   # Leerzeichen am Rand weg
        .str.replace("Region ", "", regex=False)       # Vorsilbe "Region " weg
        .str.capitalize()                              # "nord" -> "Nord"
        .replace({"Sued": "Süd"})                      # Umschreibung ersetzen
    )
    # <<< ENDE AUFGABE 1
```

```text
Zeilen vorher:         33554
Dubletten entfernt:      398
Zeilen nachher:        33156
Zeilen ohne Kosten:      648
OK        keine Dubletten mehr
OK        jedes Datum gelesen
OK        genau 4 Regionen
Gespeichert: project/playground/umsatz_clean.csv
```

Die Zeilenbilanz bleibt gleich: Schritt 4 ändert nur Texte, keine Zeilenzahl. `umsatz_clean.csv` stimmt Zeile für Zeile mit dem Beispiel [`clean.py`](../../project/examples/m02-data-preparation/l02-cleaning/clean.py) überein. Verteilung danach: Nord 9.809, West 8.853, Süd 8.527, Ost 5.967 Zeilen.

## Erweiterung: fehlende Kosten

Kommentar über Schritt 3 und zusätzliche Zeilen in `pruefen` (nach der Zeile „Zeilen ohne Kosten"):

```python
    # Schritt 3: fehlende Kosten markieren (nicht löschen: der Umsatz zählt trotzdem)
    # Regel: Zeilen ohne Kosten bleiben in der Tabelle. Sie zählen für Umsatz und Zeilenzahl,
    # aber nicht für den Deckungsbeitrag (bleibt leer, Lab 2.3). Die Spalte kosten_fehlt zeigt sie.
    df["kosten_fehlt"] = df["kosten"].isna()
```

```python
    ohne = nachher.loc[nachher["kosten_fehlt"], "umsatz"].sum()       # Umsatz der Zeilen ohne Kosten
    print(f"Umsatz ohne Kosten:   {ohne:>12,.2f} € ({ohne / nachher['umsatz'].sum():.1%} vom Umsatz)")
```

```text
Zeilen ohne Kosten:      648
Umsatz ohne Kosten:     197,201.41 € (2.0% vom Umsatz)
```

Ein `dropna()` hätte diese 197.201,41 € still aus jedem Bericht entfernt.
