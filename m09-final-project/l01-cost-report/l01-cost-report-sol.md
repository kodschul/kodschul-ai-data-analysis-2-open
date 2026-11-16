# Lab 9.1 – Lösung: Das Muster auf eigene Daten übertragen

Fertiger Stand: [project/examples/m09-final-project/l01-cost-report/](../../project/examples/m09-final-project/l01-cost-report/kostenbericht/SKILL.md) mit dem Skill `kostenbericht/` (`SKILL.md` + `scripts/monatsbericht.py`, nur Einstellungen geändert), dem ausgeführten Notebook `gegenrechnung.ipynb` und dem Bericht `berichte/kosten/bericht_2026_09_v2.html` + `kpi_2026_09.xlsx`.

## Aufgabe 1: Skill kopieren, Name und Beschreibung

```text
.github/skills/
├── kostenbericht/          ← Kopie, umbenannt
│   ├── SKILL.md            ← name: kostenbericht, neue description
│   └── scripts/monatsbericht.py
├── kpi-kurzcheck/
└── monatsbericht/          ← unverändert
```

VS Code legt beim Einfügen zuerst `monatsbericht copy` an; nach **F2** heißt der Ordner `kostenbericht` wie `name` im Frontmatter (Feldregel aus Lab 7.1).

## Aufgabe 2: Datenordner

```text
data_kosten/
└── kostenstellen.csv
```

`lieferungen/` enthält danach nur noch `nordwind_umsatz_2026_10_defekt.csv`.

## Aufgabe 3: Einstellungen und erster Lauf

Unterschied zur Kopie von v2 (alle anderen Zeilen gleich):

```python
DATEN_STANDARD = "data_kosten"            # Ordner mit den Lieferungen (relativ zum Kursordner)
MUSTER_STANDARD = "kostenstellen*.csv"    # welche Dateien im Ordner gelesen werden
AUSGABE_STANDARD = "berichte/kosten"      # hier landen HTML und Excel (eigener Ordner, damit der Umsatzbericht bleibt)

SPALTEN = {
    "datum": "Buchungsdatum",   # Pflicht
    "betrag": "Betrag",         # Pflicht
    "gruppe": "Kostenstelle",   # optional: Kennzahlen und Auffälligkeiten je Gruppe
    "kunde": None,              # optional: Kundensegmente – gibt es hier nicht
    "kosten": None,             # optional: Deckungsbeitrag und Marge – gibt es hier nicht
}
ANZEIGENAMEN = {"betrag": "Kosten", "gruppe": "Kostenstelle", "kunde": "Kunde", "kosten": "Kosten"}
```

Ausgabe von `python .github/skills/kostenbericht/scripts/monatsbericht.py bericht --daten data_kosten`:

```text
Monatsbericht 2026-09 – Kosten – Daten: data_kosten/kostenstellen*.csv
  kostenstellen.csv: 1.639 Zeilen gelesen
  Dubletten entfernt: 0
  Deckungsbeitrag und Marge übersprungen: keine Spalte für die Rolle kosten
  Schreibweisen Kostenstelle: 6 -> 6
  Zeilen nach Bereinigung: 1.639, Monate 2023-10 bis 2026-09
  Plan-Spalte übersprungen: keine Planwerte für 2026-09 (nordwind_plan_2026.csv)

                       Kosten  Vormonat  Δ Vormonat %   Vorjahr  Δ Vorjahr %
Kostenstelle
Fuhrpark              1893.93   2119.29         -10.6   2186.83        -13.4
Gebäude               1210.15   4875.87         -75.2   6045.16        -80.0
IT                    3001.15   5511.19         -45.5   1837.65         63.3
Marketing             4170.72   2825.62          47.6   2752.17         51.5
Personalentwicklung   1252.58   1272.69          -1.6   1009.70         24.1
Vertrieb              5562.94   7853.82         -29.2   5640.81         -1.4
Gesamt               17091.47  24458.48         -30.1  19472.32        -12.2

Segmente übersprungen: keine Spalte für die Rolle kunde
Auffällige Tage (Schwelle 3): 0
Prognose 2026-10 bis 2026-12: 20.517, 21.195, 18.297

Bericht: berichte/kosten/bericht_2026_09_v2.html

Summenkontrolle: 2026-09 – 42 Zeilen, Summe Kosten 17.091,47 – stimmt mit der Kennzahlentabelle überein
Sollwert-Prüfung: keine Sollwert-Datei – übersprungen
```

Ohne `--monat` nimmt v2 den letzten Monat der Daten, hier 2026-09. `;`, Dezimalkomma und cp1252 hat die automatische Erkennung gelesen; am Rechenteil des Skripts hat sich nichts geändert.

## Aufgabe 4: `SKILL.md` anpassen und auslösen

Ergebnis der Anpassung (Ausschnitt, vollständig im [Beispiel](../../project/examples/m09-final-project/l01-cost-report/kostenbericht/SKILL.md)):

````markdown
## Vorgehen

1. Berichtsmonat als JJJJ-MM bestimmen (September 2026 = `2026-09`). Nennt die Frage keinen eindeutigen Monat, zuerst nachfragen („Für welchen Monat, z. B. 2026-09?“) und nicht raten.
2. Im Wurzelordner des Arbeitsbereichs genau einen dieser Befehle ausführen, `JJJJ-MM` durch den Monat ersetzen:

   Kostenbericht (HTML und Excel):

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py bericht --daten data_kosten --monat JJJJ-MM --excel
   ```

   Nur die auffälligen Tage:

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py auffaelligkeiten --daten data_kosten --monat JJJJ-MM
   ```

   Nur die Prognose der drei Folgemonate:

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py prognose --daten data_kosten --monat JJJJ-MM
   ```

3. Beginnt eine Zeile der Ausgabe mit `STOPP:`, diese Zeile wörtlich melden, sagen, dass kein Bericht entstanden ist, und nichts weiter rechnen oder ausführen.

## Antwortformat

1. **Kurzfazit:** 2–3 Sätze zu den Gesamtkosten und der Abweichung zu Vormonat und Vorjahr; nur Zahlen aus der Ausgabe.
2. **Kennzahlentabelle:** die Tabelle aus der Ausgabe als Markdown-Tabelle (Kostenstelle, Kosten, Δ Vormonat %, Δ Vorjahr %). Bei `auffaelligkeiten` oder `prognose` stattdessen deren Tabelle.
3. **Prüfung:** die Zeilen `Summenkontrolle: …` und `Sollwert-Prüfung: …` wörtlich aus der Ausgabe.
4. **Dateien:** Pfade zu `berichte/kosten/bericht_JJJJ_MM_v2.html` und `berichte/kosten/kpi_JJJJ_MM.xlsx` (nur beim Befehl `bericht`).
````

Alle drei Befehle wurden mit `2026-09` getestet und enden mit denselben zwei Prüfzeilen.

Bestätigungsdialog nach „Erstelle den Kostenbericht je Kostenstelle für September 2026.“:

```text
python .github/skills/kostenbericht/scripts/monatsbericht.py bericht --daten data_kosten --monat 2026-09 --excel
```

Die Ausgabe gleicht Aufgabe 3, zusätzlich:

```text
OK – berichte/kosten/kpi_2026_09.xlsx mit 7 Zeilen im Blatt 'Kennzahlen' (Blätter: Kennzahlen, Auffaelligkeiten)
```

Antwortformat laut `SKILL.md` (Musterantwort aus der Ausgabe, keine aufgezeichnete Agent-Antwort):

> **Kurzfazit:** Die Kosten im September 2026 betragen 17.091,47 €: −30,1 % zum Vormonat und −12,2 % zum Vorjahresmonat. Den größten Anteil hat Vertrieb mit 5.562,94 €.
>
> | Kostenstelle | Kosten | Δ Vormonat % | Δ Vorjahr % |
> | --- | ---: | ---: | ---: |
> | Fuhrpark | 1893.93 | -10.6 | -13.4 |
> | Gebäude | 1210.15 | -75.2 | -80.0 |
> | IT | 3001.15 | -45.5 | 63.3 |
> | Marketing | 4170.72 | 47.6 | 51.5 |
> | Personalentwicklung | 1252.58 | -1.6 | 24.1 |
> | Vertrieb | 5562.94 | -29.2 | -1.4 |
> | Gesamt | 17091.47 | -30.1 | -12.2 |
>
> Summenkontrolle: 2026-09 – 42 Zeilen, Summe Kosten 17.091,47 – stimmt mit der Kennzahlentabelle überein
> Sollwert-Prüfung: keine Sollwert-Datei – übersprungen
>
> Dateien: `berichte/kosten/bericht_2026_09_v2.html`, `berichte/kosten/kpi_2026_09.xlsx`

„übersprungen“ ist hier richtig: In `data_kosten/` liegt keine `kontrollsummen.csv`. Die Prüfung übernimmt Aufgabe 5.

## Aufgabe 5: Gegenrechnung

Erste Zelle (im Kursordner, eigener Bericht vorhanden):

```text
Datei:   data_kosten/kostenstellen.csv
Bericht: berichte/kosten/bericht_2026_09_v2.html
Summenkontrolle: 2026-09 – 42 Zeilen, Summe Kosten 17.091,47 – stimmt mit der Kennzahlentabelle überein
```

Fehlen `data_kosten/` oder der eigene Bericht, nimmt das Notebook `lieferungen/kostenstellen.csv` und den Bericht aus dem Beispiel (so im ausgeführten Beispiel-Notebook).

Lösungs-Snippet:

```python
# >>> AUFGABE 1: kostenstellen.csv lesen, je Monat Anzahl Buchungen und Summe bilden – Prompt siehe Übung, Aufgabe 5
kosten = pd.read_csv(DATEI, sep=";", decimal=",", encoding="cp1252")
kosten["monat"] = pd.to_datetime(kosten["Buchungsdatum"], format="%d.%m.%Y").dt.strftime("%Y-%m")
je_monat = kosten.groupby("monat").agg(zeilen=("Betrag", "count"), summe=("Betrag", "sum"))
je_monat.tail(3)
# <<< ENDE AUFGABE 1
```

```text
         zeilen     summe
monat
2026-07      52  19664.61
2026-08      46  24458.48
2026-09      42  17091.47
```

Prüfzelle:

```text
OK – Gegenrechnung 2026-09: 42 Buchungen, Summe 17.091,47 € = Summenkontrolle des Berichts
```

| KI-Code | Meldung der Prüfzelle |
| --- | --- |
| ohne `decimal=","` | `nicht OK – summe ist keine Zahl: beim Lesen decimal="," setzen.` |
| Tabelle heißt anders als `je_monat` | `nicht OK – Tabelle je_monat fehlt noch (Aufgabe 1).` |
| ohne `encoding="cp1252"` | `UnicodeDecodeError` beim Lesen (Umlaut in „Gebäude“) |

Der Vormonat 2026-08 (24.458,48 €) stimmt mit der Spalte Vormonat der Kennzahlentabelle überein: eine zweite Gegenprobe ohne Mehraufwand.

## Erweiterung: eigene CSV

Beispiel für eine eigene Datei `data_kosten/eigene.csv` mit nur zwei Spalten `Datum;Betrag` (eine Zeile je Monat):

```python
MUSTER_STANDARD = "eigene*.csv"
SPALTEN = {"datum": "Datum", "betrag": "Betrag", "gruppe": None, "kunde": None, "kosten": None}
```

Getestet mit 33 Monatszeilen: Das Skript läuft durch, die Kennzahlentabelle hat nur die Zeile `Gesamt`, Segmente und Plan werden übersprungen, die Prognose läuft ab 24 Monaten. Für die Gegenrechnung `DATEI = "data_kosten/eigene.csv"` und in Aufgabe 1 `Buchungsdatum` durch `Datum` ersetzen; Trennzeichen, Dezimalzeichen und Zeichensatz wie in der eigenen Datei. Weitere Fälle: [Checkliste Anpassung an eigene Daten](../anhang-anpassung-eigene-daten.md).
