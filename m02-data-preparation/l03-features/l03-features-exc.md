# Lab 2.3 – Übung: Kennzahlen ableiten und gegenprüfen

**Dauer:** ca. 15 Minuten
**Ändert die Nordwind-Projektbasis?** Ja – es entsteht `umsatz_features.csv`. Modul 3 liest die Fassung aus dem Beispiel von Lab 2.3.

## Vorbereitung

- Starter: [`project/starters/m02-l03-features.py`](../../project/starters/m02-l03-features.py) · Arbeitsdatei: `project/playground/m02-l03-features.py`
- Eingabe (fest im Starter): `project/examples/m02-data-preparation/l02-cleaning/umsatz_clean.csv` aus dem Beispiel von Lab 2.2
- Ergebnis: `project/playground/umsatz_features.csv`

## Aufgaben

1. Kopiere den Starter nach `project/playground/` und führe ihn aus:

   ```bash
   python project/playground/m02-l03-features.py
   ```

2. Öffne `project/playground/m02-l03-features.py`, beginne einen neuen Chat im Modus **Ask** und sende diesen Prompt:

   > Kontext: In #file:m02-l03-features.py ergänzt die Funktion `add_features(df)` neue Spalten in einem pandas-DataFrame; `deckungsbeitrag` ist schon berechnet.
   > Spalten: umsatz (Euro), kosten (Euro, teils leer), deckungsbeitrag = umsatz − kosten (leer, wo kosten fehlen).
   > Regel: Marge = Deckungsbeitrag geteilt durch Umsatz, je Zeile, als Anteil (0.25 = 25 %), nicht in Prozent. Leere Werte bleiben leer, nichts mit 0 auffüllen, keine Zeile löschen.
   > Gewünschte Ausgabe: genau eine Codezeile für die Funktion (vier Leerzeichen eingerückt), die die Spalte `df["marge"]` anlegt, mit kurzem Kommentar.

3. Füge die Zeile zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` ein, speichere und führe das Skript erneut aus.
4. Prüfe das Ergebnis gegen die Kontrollsummen:

   ```bash
   python check_zahlen.py project/playground/umsatz_features.csv
   ```

## Checkpoint

- Aufgabe 1 meldet `nicht OK  Spalte marge fehlt`.
- Nach Aufgabe 3: `OK        marge = Deckungsbeitrag / Umsatz in jeder Zeile (leer, wo Kosten fehlen)`, 33.156 Zeilen, 648 ohne Kosten.
- `check_zahlen.py` endet mit `Ergebnis: 0 Abweichungen – Prüfung bestanden`.
- Bei `nicht OK`: Prompt ein zweites Mal senden; danach das Lösungs-Snippet aus der Lösung einfügen.

## Abschlusskriterien

- `project/playground/umsatz_features.csv` enthält die Spalten `monat`, `quartal`, `deckungsbeitrag` und `marge`.
- Die Prüfung gegen `data/kontrollsummen.csv` ist bestanden.

## Erweiterung

Lass Copilot mit eigenem Prompt eine Funktion `kunden_rfm(df, stichtag)` ergänzen, die je `kunde_id` die Tage seit dem letzten Kauf bis zum Stichtag 30.09.2026, die Zahl der Buchungen und die Umsatzsumme berechnet und als `project/playground/kunden_rfm.csv` speichert (Spalten `kunde_id, tage_seit_kauf, haeufigkeit, umsatz`). Vergleiche mit [`kunden_rfm.csv`](../../project/examples/m02-data-preparation/l03-features/kunden_rfm.csv) aus dem Beispiel.

## Fallback

Ohne Copilot: Lösungs-Snippet aus der Lösung einfügen. Fertige Fassung: [`features.py`](../../project/examples/m02-data-preparation/l03-features/features.py) mit `umsatz_features.csv` und `kunden_rfm.csv` im selben Ordner.
