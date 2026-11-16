# Lab 1.1 – Lösung: Das große Bild und die Nordwind-Daten

## Aufgabe 1: Kursumgebung prüfen

```bash
python check_setup.py
```

Erwartete Ausgabe (gekürzt; Versionen laut `requirements.txt`):

```text
OK          Python 3.11.12 (erwartet 3.11)
OK          pandas 2.3.3
...
OK          .github/skills/kpi-kurzcheck/SKILL.md
OK          Umgebungsvariable OPENAI_API_KEY gesetzt (Wert wird nicht angezeigt)

Alles bereit.
```

Jede Zeile mit `NICHT OK` nennt, was fehlt. Ein fehlender API-Schlüssel stört erst ab Modul 4.

## Aufgabe 2: KI-Landkarte für Nord

```bash
python project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py --region Nord
```

```text
Region: Nord
1 Prognose   Trendfaktor 1.042; 2026-10: 103.595 €, 2026-11: 96.205 €, 2026-12: 87.964 €
2 Segmente   Segment 1: 3 Kunden, Segment 2: 23 Kunden, Segment 3: 18 Kunden, Segment 4: 79 Kunden
3 Anomalien  1 auffällige(r) Tag(e): 31.10.2024
Gespeichert: project/playground/ki_landkarte.html
```

Der Browser öffnet `ki_landkarte.html` mit den drei Diagrammen.

## Aufgabe 3: dasselbe Skript, anderes Argument

```bash
python project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py --region West
```

```text
Region: West
1 Prognose   Trendfaktor 1.131; 2026-10: 105.775 €, 2026-11: 124.809 €, 2026-12: 86.122 €
2 Segmente   Segment 1: 4 Kunden, Segment 2: 23 Kunden, Segment 3: 13 Kunden, Segment 4: 62 Kunden
3 Anomalien  4 auffällige(r) Tag(e): 24.01.2024, 29.02.2024, 24.04.2024, 27.11.2025
Gespeichert: project/playground/ki_landkarte.html
```

Der 27.11.2025 ist der höchste Punkt im dritten Diagramm (rund 25.000 € an einem Tag, ein Großauftrag). Die Datei `ki_landkarte.html` wird bei jedem Lauf überschrieben. Weitere gültige Werte: `--region Süd`, `--region Ost`; ohne Argument nimmt das Skript `Nord`.

## Aufgabe 4: Starter kopieren

Im Explorer liegt danach `project/playground/m01-l01-erste-zahlen.ipynb`. Der Starter in `project/starters/` bleibt unverändert und dient als Neuanfang.

## Aufgabe 5: Notebook ausführen

```python
umsatz_2025 = df[df["jahr"] == 2025].groupby("region")["umsatz"].sum().round(2)
umsatz_2025
```

```text
region
Nord           993077.30
Nord            29920.43
Ost            614156.26
Region Nord     30047.41
Region Ost      30478.39
Region Süd      18252.36
Region West     46324.91
Sued            29604.44
Süd            799512.90
West           925573.15
nord            28392.29
ost             17289.65
süd             18673.98
west            39641.17
Name: umsatz, dtype: float64
```

Die zweite Zeile „Nord" ist „Nord " mit Leerzeichen am Ende. 14 Werte für 4 Regionen: Diese Schreibweisen bereinigt Modul 2. Vollständiges Notebook mit allen Ausgaben: [`erste_zahlen.ipynb`](../../project/examples/m01-ai-analysis-basics/l01-ai-landscape/erste_zahlen.ipynb).

## Erweiterung: nach Kanal statt Region

```python
umsatz_2025 = df[df["jahr"] == 2025].groupby("kanal")["umsatz"].sum().round(2)
umsatz_2025
```

```text
kanal
Außendienst    2839158.77
Onlineshop      781785.87
Name: umsatz, dtype: float64
```

Die Spalte `kanal` hat nur zwei saubere Werte; nicht jede Spalte hat dasselbe Problem. Beide Summen enthalten noch die doppelt gelieferten Zeilen (Lab 2.1).
