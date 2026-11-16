# Cheatsheet Modul 1–2: Terminal, Notebook, Copilot, pandas

## Terminal in VS Code (Lab 1.1)

| Befehl / Handgriff | Wirkung |
| --- | --- |
| Menü **Terminal → Neues Terminal** | Terminal im Kursordner öffnen |
| `python check_setup.py` | Kursumgebung prüfen |
| `python <pfad/skript.py>` | Skript ausführen, Ausgabe im Terminal |
| `python <skript.py> --region West` | Skript mit Argument: Name `--region`, Wert `West` |
| `python <skript.py> --help` | Argumente eines Skripts anzeigen (wenn das Skript sie anbietet) |
| Pfeil nach oben | letzten Befehl zurückholen und ändern |
| Tab | Datei- und Ordnernamen vervollständigen |
| ▷ „Run Python File" oben rechts | Skript ohne Argument starten |

## Notebook (Lab 1.1)

| Handgriff | Wirkung |
| --- | --- |
| Umschalt+Enter | Zelle ausführen, zur nächsten springen |
| Strg+Enter | Zelle ausführen, Cursor bleibt |
| Kernel oben rechts | laufendes Python 3.11; merkt sich Variablen |
| **Restart** in der Leiste | Kernel neu starten, Speicher leer; danach von oben ausführen |
| **Run All** in der Leiste | alle Zellen von oben nach unten |
| Starter kopieren | Explorer: Rechtsklick Starter → **Copy**, Rechtsklick `project/playground` → **Paste** |

## Copilot Chat (Lab 1.2, Stand 11/2026)

| Handgriff | Wirkung |
| --- | --- |
| Strg+Alt+I | Chat öffnen |
| **+** im Chat | neuer Chat ohne alten Verlauf |
| Auswahlfeld **Ask** | antwortet und schlägt Code vor, ändert nichts |
| Auswahlfeld **Agent** | ändert Dateien, führt Befehle aus (mit Bestätigung) |
| `#file:datei.py` | Datei als Kontext anhängen |
| **Allow** / **Skip** | Befehl im Bestätigungsdialog einmal erlauben / auslassen |
| Strg+I in einer Notebook-Zelle | Chat direkt in der Zelle |

## Prompt-Muster für Code (Lab 2.1)

| Teil | Frage |
| --- | --- |
| Kontext | Welche Datei, welche Variable, welche Bibliothek? |
| Spalten | Welche Spalten mit welchem Inhalt? |
| Regel | Was genau soll gelten, was darf nicht passieren? |
| gewünschte Ausgabe | Variable, Format, Umfang („nur der Code für eine Zelle") |

Drei Lesefragen vor dem Ausführen: Welche Datei? Was wird verändert? Was wird ausgegeben?

## pandas ↔ Excel (Lab 2.1)

| Excel | pandas |
| --- | --- |
| Datei öffnen | `df = pd.read_csv("data/nordwind_umsatz.csv")` |
| Spalte markieren | `df["umsatz"]` |
| Formel nach unten ziehen | `df["db"] = df["umsatz"] - df["kosten"]` |
| Filter | `df[df["jahr"] == 2025]` |
| zwei Bedingungen | `df[(df["jahr"] == 2025) & (df["region"] == "Nord")]` |
| Sortieren | `df.sort_values("umsatz", ascending=False)` |
| `SUMME`, `ANZAHL`, `MITTELWERT` | `.sum()`, `.count()`, `.mean()` |
| Pivot-Tabelle | `df.groupby("region")["umsatz"].sum()` oder `pd.pivot_table(...)` |
| SVERWEIS | `df.merge(plan, on=["monat", "region"])` |

## pandas: Daten prüfen (Lab 2.1)

| Befehl | Wirkung |
| --- | --- |
| `df.head()` | erste fünf Zeilen |
| `len(df)` | Zeilenzahl |
| `df.columns` | Spaltennamen |
| `df.info()` | Typ und Anzahl gefüllter Werte je Spalte |
| `df.isna().sum()` | fehlende Werte je Spalte |
| `df.duplicated().sum()` | Anzahl Dubletten |
| `df["region"].value_counts()` | jeder Wert mit Häufigkeit |
| `df["region"].nunique()` | Anzahl verschiedener Werte |
| `df["umsatz"].describe()` | Anzahl, Mittelwert, Streuung, Min, Quartile, Max |
| `df["datum"].str.contains(".", regex=False)` | `True`, wo der Text einen Punkt enthält |

## pandas: bereinigen (Lab 2.2)

| Befehl | Wirkung |
| --- | --- |
| `df = df.copy()` | mit einer Kopie arbeiten, Original bleibt |
| `df.drop_duplicates()` | Dubletten entfernen |
| `pd.to_datetime(s, format="%d.%m.%Y", errors="coerce")` | Text → Datum; Unpassendes wird leer (`NaT`) |
| `a.fillna(b)` | Lücken in `a` mit Werten aus `b` füllen |
| `df["kosten"].isna()` | `True` je Zeile ohne Kosten (Markierung) |
| `.str.strip()` | Leerzeichen am Rand entfernen |
| `.str.replace("Region ", "", regex=False)` | Text ersetzen |
| `.str.capitalize()` | erster Buchstabe groß, Rest klein |
| `.replace({"Sued": "Süd"})` | ganze Werte ersetzen |
| `df.to_csv(ORDNER + "datei.csv", index=False)` | Ergebnis speichern |

Vorsicht: `df.dropna()` löscht jede Zeile mit einem leeren Wert, bei Nordwind 648 Zeilen mit 197.201 € Umsatz.

## pandas: Kennzahlen (Lab 2.3)

| Befehl | Wirkung |
| --- | --- |
| `df["datum"].dt.strftime("%Y-%m")` | Monat als Text, z. B. `2026-09` |
| `df["datum"].dt.to_period("Q").astype(str)` | Quartal, z. B. `2026Q3` |
| `df["umsatz"] - df["kosten"]` | Deckungsbeitrag je Zeile (leer, wo Kosten fehlen) |
| `df["deckungsbeitrag"] / df["umsatz"]` | Marge je Zeile als Anteil |
| `g = df.groupby("monat")`, `g["deckungsbeitrag"].sum() / g["umsatz"].sum()` | Marge je Monat (nie Zeilenmargen mitteln) |
| `df.groupby("kunde_id").agg(letzter_kauf=("datum", "max"), haeufigkeit=("beleg_nr", "count"))` | mehrere Kennzahlen je Gruppe mit eigenen Namen |

## Kursdateien (Modul 1–2)

| Befehl | Wirkung |
| --- | --- |
| `python project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py --region West` | drei KI-Aufgabentypen als HTML |
| `python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py` | Zeilen, Monate, Gesamtumsatz der Rohdatei |
| `python project/examples/m02-data-preparation/l01-data-quality/quality_check.py <datei.csv>` | Problemtabelle einer Lieferung |
| `python project/playground/m02-l02-clean.py` | Bereinigung mit Zeilenbilanz |
| `python project/playground/m02-l03-features.py` | Kennzahlen ableiten |
| `python check_zahlen.py <datei.csv>` | Umsatz, Deckungsbeitrag, Marge gegen `data/kontrollsummen.csv` |
