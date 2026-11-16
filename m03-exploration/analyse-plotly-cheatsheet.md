# Cheatsheet: Analyse und plotly (Modul 3)

Alle Befehle im Kursordner; `df` ist die Tabelle aus `umsatz_features.csv`, `import pandas as pd` und `import plotly.express as px` sind ausgeführt.

## Daten laden und überblicken

| Befehl | Wirkung |
| --- | --- |
| `pd.read_csv(datei, parse_dates=["datum"])` | CSV lesen, Spalte `datum` gleich als Datum |
| `df[["umsatz", "marge"]].describe()` | Anzahl, Mittelwert, Streuung, Minimum, Viertelwerte, Maximum |
| `df["datum"].dt.month` | Monatsnummer aus einem Datum (1–12) |
| `df[df["datum"].dt.month <= 9]` | nur Januar bis September |
| `df["monat"].between("2026-01", "2026-09")` | Bereich bei Text im Format JJJJ-MM |

## Gruppieren und vergleichen

| Befehl | Wirkung |
| --- | --- |
| `df.groupby("produktgruppe")[["umsatz", "deckungsbeitrag"]].sum()` | Summen je Gruppe (wie Pivot mit einer Zeilenebene) |
| `df.pivot_table(index="monat", columns="kanal", values="umsatz", aggfunc="sum")` | Pivot: Monate als Zeilen, Kanäle als Spalten |
| `summen["deckungsbeitrag"] / summen["umsatz"]` | Marge einer Gruppe aus den Summen, nie `["marge"].mean()` |
| `tabelle.pct_change()` | Veränderung zur vorherigen Zeile (Anteil, × 100 = %) |
| `tabelle.pct_change(axis="columns")` | Veränderung zur vorherigen Spalte, z. B. Jahr gegen Vorjahr |
| `df["kunde_id"].nunique()` | Anzahl verschiedener Werte |
| `tabelle.sort_values("spalte", ascending=False)` | absteigend sortieren |
| `tabelle.round(1)` | auf eine Nachkommastelle runden |
| `tabelle.reset_index()` | Zeilenbeschriftung wird wieder normale Spalte (für Diagramme) |
| `tabelle.to_csv(ORDNER + "name.csv")` | Ergebnistabelle speichern |

## Diagramme mit plotly express

| Befehl | Wirkung |
| --- | --- |
| `px.line(t, x="monat", y=["Außendienst", "Onlineshop"])` | Verlauf, eine Linie je Spalte |
| `px.bar(t, x="produktgruppe", y="marge_prozent")` | Vergleich als senkrechte Balken |
| `px.bar(t, x="wert", y="gruppe", orientation="h")` | liegende Balken |
| `px.bar(..., color="lage")` | einfärben nach den Werten einer Spalte |
| `title="Befund in einem Satz"` | Titel mit der Aussage |
| `text="marge_prozent"` | Wert auf den Balken |
| `labels={"monat": "Monat", "value": "Umsatz in €"}` | deutsche Achsentitel |
| `fig` als letzte Zeile der Zelle | Diagramm im Notebook anzeigen |
| `fig.write_html(datei, include_plotlyjs="cdn")` | als kleine HTML-Datei speichern (plotly aus dem Internet) |
| `fig.to_html(full_html=False, include_plotlyjs="cdn")` | Diagramm als HTML-Baustein für einen Bericht |

| Aussage | Diagramm |
| --- | --- |
| Verlauf | `px.line` |
| Vergleich | `px.bar` |
| Anteil | `px.bar` mit `color`, selten `px.pie` |
| Abweichung | `px.bar` um die Nulllinie |

## Monatsbericht v1

| Befehl | Wirkung |
| --- | --- |
| `python project/playground/monatsbericht.py data/nordwind_umsatz.csv --monat 2026-09` | Bericht und KPI-Tabelle für September 2026 |
| `python project/playground/monatsbericht.py --help` | Argumente anzeigen |
| `python check_zahlen.py project/playground/kpi_2026_09.csv` | KPI-Tabelle gegen `data/kontrollsummen.csv` prüfen |
| `pd.Period("2026-09", freq="M") - 1` | Vormonat `2026-08`; `- 12` ergibt den Vorjahresmonat |
| `f"{wert:,.0f} €".replace(",", ".")` | `343381.7` → `343.382 €` |

## Prompt-Muster für eine Code-Stelle

| Teil | Inhalt |
| --- | --- |
| Kontext | Notebook oder Datei, Name der Tabelle, was importiert ist |
| Spalten | Spaltennamen mit Bedeutung und Einheit |
| Regel | Rechnung oder Diagrammtyp, Titel als Befund |
| Ausgabe | nur Code, Ergebnis in fester Variable, nichts speichern |
