# Lab 1.2 – Lösung: Vier Wege, KI einzusetzen

## Aufgabe 1: drei Skripte, drei Zahlen

```text
Antwort A: West wuchs 2025 am stärksten, um +3.6 %.
           (gerechnet mit 33554 Zeilen)
Antwort B: West wuchs 2025 am stärksten, um +2.9 %.
           (gerechnet mit 25717 Zeilen)
Zeilen roh: 33554, nach Bereinigung: 33156, Regionen: Nord, Ost, Süd, West
Wachstum 2025 gegenüber 2024 je Region:
  West   +13.4 %
  Nord    +5.1 %
  Süd     +4.5 %
  Ost     -4.9 %
Referenz:  West wuchs 2025 am stärksten, um +13.4 %.
```

Gleiche Region, drei Zahlen. Für einen Bericht zählt nur die Referenz: Sie bereinigt die Daten, bevor sie rechnet.

## Aufgabe 2: Der Agent erklärt und korrigiert

### Erklärung

Die Formulierung im Chat ist bei jedem Lauf anders. Inhaltlich muss die Erklärung diese Punkte treffen (von Hand am Code geprüft):

| Unterschied | Antwort A | Referenz | Wirkung auf West |
| --- | --- | --- | --- |
| Dubletten | rechnet alle 33.554 Zeilen, 398 doppelt gelieferte zählen zweimal | entfernt sie, 33.156 Zeilen | kleine Verzerrung in beiden Jahren |
| Regionsnamen | gruppiert die Spalte `region` wie geliefert | vereinheitlicht „Region West", „west" … zu „West" | 2025 fehlen rund 86.000 € unter „Region West" und „west" in der Zeile West; 2024 gab es diese Schreibweisen noch nicht, das Wachstum fällt von +13,4 % auf +3,6 % |
| Schreibweisen ohne Vorjahr | „Region West" hat 2024 keinen Wert, das Wachstum ist leer und fällt aus dem Vergleich | – | der Fehler bleibt unbemerkt, es gibt keine Fehlermeldung |
| Jahr | Spalte `jahr` | Jahr aus dem gelesenen Datum | kein Unterschied, `jahr` passt zu jedem Datum |

Antwort B hat einen weiteren Fehler: Sie liest nur Datumswerte im Format `JJJJ-MM-TT` und entfernt alle anderen. Damit fallen die 7.837 Onlineshop-Zeilen (`TT.MM.JJJJ`) weg, die Zahl beschreibt nur den Außendienst.

### Neue Datei und Befehl

Der Bestätigungsdialog zeigt:

```bash
python project/playground/antwort_a_korrigiert.py
```

Eine geprüfte Fassung der Datei, die der Agent anlegt (seine Fassung kann anders aussehen, muss aber dasselbe tun):

```python
"""Antwort A, korrigiert: Dubletten entfernen und Regionsnamen vereinheitlichen."""

import pandas as pd

df = pd.read_csv("data/nordwind_umsatz.csv")

# doppelte Zeilen entfernen
df = df.drop_duplicates()

# Regionsnamen vereinheitlichen wie in kpi_reference.py
df["region"] = (df["region"].str.strip().str.replace("Region ", "", regex=False)
                .str.capitalize().replace({"Sued": "Süd"}))

# Umsatz je Region und Jahr (Spalte "jahr" aus der Datei)
umsatz = df.groupby(["region", "jahr"])["umsatz"].sum().unstack()

# Wachstum 2025 gegenüber 2024 in Prozent
wachstum = (umsatz[2025] / umsatz[2024] - 1) * 100
sieger = wachstum.idxmax()

print(f"Antwort A (korrigiert): {sieger} wuchs 2025 am stärksten, um {wachstum[sieger]:+.1f} %.")
print(f"           (gerechnet mit {len(df)} Zeilen)")
```

```text
Antwort A (korrigiert): West wuchs 2025 am stärksten, um +13.4 %.
           (gerechnet mit 33156 Zeilen)
```

Zeigt die Datei des Agenten eine andere Zahl, den Code mit der Referenz vergleichen: Fehlt `drop_duplicates()` oder ein Schritt der Regionsbereinigung, weicht die Zahl ab.

## Aufgabe 3: Technik-Test `kpi-kurzcheck`

Der Bestätigungsdialog zeigt diesen Befehl:

```bash
python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py
```

Ausgabe des Skripts, die der Agent in seiner Antwort wiedergibt:

```text
KPI-Kurzcheck data/nordwind_umsatz.csv (Rohdaten, vor Bereinigung)
Zeilen:        33554
Monate:        2024-01 bis 2026-09 (33 Monate)
Umsatz gesamt: 9.917.522,56 €
```

Stimmen die Zahlen und lief der Befehl, ist der Agent-Modus für Tag 2 bereit.

## Erweiterung: dieselbe Frage zweimal live

Jeder Agent-Lauf schreibt eigenen Code; die Prozentwerte hängen davon ab, ob er Dubletten entfernt, Regionsnamen vereinheitlicht und beide Datumsformate liest. Die beiden Werte können voneinander und von der Referenz (+13,4 %) abweichen; der Grund steht im Code, den der Agent im Chat zeigt. Gleich bleibt nur die Referenz, weil sie als Datei bleibt (Weg 3).
