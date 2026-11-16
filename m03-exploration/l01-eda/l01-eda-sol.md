# Lab 3.1 – Lösung: Muster finden: explorative Analyse

Fertiges Notebook mit Ausgaben: [`project/examples/m03-exploration/l01-eda/eda.ipynb`](../../project/examples/m03-exploration/l01-eda/eda.ipynb). Dieselben drei Funktionen als Modul: [`analyse.py`](../../project/examples/m03-exploration/l01-eda/analyse.py), Aufruf im Kursordner:

```bash
python project/examples/m03-exploration/l01-eda/analyse.py
```

## Aufgabe 1: Starter kopieren

`project/playground/m03-l01-eda.ipynb` ist geöffnet; die erste Zelle zeigt `33156 Zeilen von 2024-01 bis 2026-09`.

## Aufgabe 2: Frage 1 und 2

```text
            2024      2025      2026  wachstum_prozent
region
West    656796.9  721872.8  792757.2               9.8
Süd     594101.8  617795.6  674400.2               9.2
Ost     513457.4  477187.9  520396.9               9.1
Nord    750940.8  792446.5  826874.9               4.3
```

```text
                  umsatz  deckungsbeitrag  marge_prozent
produktgruppe
Schreibwaren    747713.0         260383.0           34.8
Ordnung        1165892.9         337800.7           29.0
Küche           909567.4         246211.4           27.1
Reinigung      1342746.3         323431.6           24.1
Papier         2818190.6         481976.9           17.1
Technik        2815639.6         399081.1           14.2
```

Papier und Technik bringen den meisten Umsatz, aber die niedrigste Marge. Ost +9,1 % enthält die Buchung vom 10.02.2026 über 32.800 € (Höchstwert in `describe()`), ohne sie läge Ost bei rund +2 %.

## Aufgabe 3: Lösungs-Snippet `kanal_monat`

Zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1`:

```python
kanal_monat = df.pivot_table(index="monat", columns="kanal", values="umsatz", aggfunc="sum")
kanal_monat["anteil_online_prozent"] = (
    kanal_monat["Onlineshop"] / (kanal_monat["Außendienst"] + kanal_monat["Onlineshop"]) * 100
).round(1)
```

Gleichwertig: dieselbe Rechnung als Funktion `kanal_je_monat(df)` wie im Beispiel, oder `groupby(["monat", "kanal"])["umsatz"].sum().unstack()` statt `pivot_table`.

Letzte Zeilen:

```text
         Außendienst  Onlineshop  anteil_online_prozent
monat
2026-05     221267.0     82293.7                   27.1
2026-06     220478.1     74985.2                   25.4
2026-07     196548.9     96508.2                   32.9
2026-08     230718.3     99070.7                   30.0
2026-09     240058.1    103323.6                   30.1
```

## Aufgabe 4: Lesefragen und Prüfzelle

| Lesefrage | Antwort für das Snippet |
| --- | --- |
| Welche Datei? | keine; der Code arbeitet nur mit `df` im Speicher |
| Was wird verändert? | eine neue Tabelle `kanal_monat` entsteht, `df` bleibt unverändert |
| Was wird ausgegeben? | nichts; die letzte Zeile der Zelle (`kanal_monat`) zeigt die Tabelle |

Prüfzelle: `OK – 33 Monate, Onlineshop-Anteil im September 2026: 30,1 %`

## Aufgabe 5: Speichern

```text
Gespeichert: drei Tabellen in project/playground/
```

## Erweiterung

Eine mögliche Frage (Leitfrage 2): „Steigt der Umsatz, weil mehr Kunden kaufen oder weil sie mehr kaufen?"

```python
jan_sep = df[df["datum"].dt.month <= 9]
kunden = jan_sep.groupby("jahr").agg(kunden=("kunde_id", "nunique"), umsatz=("umsatz", "sum"))
kunden["umsatz_je_kunde"] = kunden["umsatz"] / kunden["kunden"]
kunden["veraenderung_umsatz_je_kunde_prozent"] = kunden["umsatz_je_kunde"].pct_change() * 100
kunden.round(1)
```

```text
      kunden     umsatz  umsatz_je_kunde  veraenderung_umsatz_je_kunde_prozent
jahr
2024     395  2515296.9           6367.8                                   NaN
2025     398  2609302.9           6556.0                                   3.0
2026     367  2814429.1           7668.7                                  17.0
```

Januar bis September 2026 kaufen weniger Kunden als im Vorjahr, jeder im Schnitt deutlich mehr. Weitere typische Fragen: Umsatz je Wochentag, Top-10-Kunden, Anteil der Buchungen ohne Kosten je Monat, Durchschnittsbetrag je Kanal.
