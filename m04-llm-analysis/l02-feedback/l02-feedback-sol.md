# Lab 4.2 – Lösung: Kundenfeedback auswerten

Beispiel-Notebook: [`project/examples/m04-llm-analysis/l02-feedback/feedback.ipynb`](../../project/examples/m04-llm-analysis/l02-feedback/feedback.ipynb) mit [`feedback_klassifiziert.csv`](../../project/examples/m04-llm-analysis/l02-feedback/feedback_klassifiziert.csv) und `diagramm_themen.html`. Das Beispiel wurde **ohne API-Schlüssel** ausgeführt: Alle 50 Einordnungen stammen aus den **Stichwortregeln** (Spalte `methode`), nicht vom Sprachmodell. Mit Schlüssel entstehen andere Werte; geprüft wird dann genauso.

## Aufgabe 1: Setup und Grenzen der Stichwortregeln

```text
300 Kommentare; davon in den ersten 50 von Hand gelabelt: 20
Ohne Dienst (OPENAI_API_KEY fehlt): classify() nutzt Stichwortregeln.
```

```text
Toner kam zerbrochen an.               -> {'stimmung': 'neutral', 'thema': 'unklar', 'methode': 'Stichwortregeln'}
Rechnung stimmt schon wieder nicht.    -> {'stimmung': 'negativ', 'thema': 'Service', 'methode': 'Stichwortregeln'}
Lieferung kam, endlich.                -> {'stimmung': 'neutral', 'thema': 'Lieferung', 'methode': 'Stichwortregeln'}
```

## Aufgabe 2: 50 Kommentare

Ohne Schlüssel: `Stichwortregeln    50`. Mit Schlüssel: `Sprachmodell    50`; erscheinen einzelne Zeilen mit `Stichwortregeln`, ist für diese Kommentare eine Anfrage gescheitert (Meldung darüber).

## Aufgabe 3: Lösungs-Snippet Trefferquote

Zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1`:

```python
treffer_thema = (gelabelt["thema"] == gelabelt["thema_label"]).mean()          # True = 1, False = 0
treffer_stimmung = (gelabelt["stimmung"] == gelabelt["stimmung_label"]).mean()
print(f"Trefferquote Thema:    {treffer_thema:.0%}")
print(f"Trefferquote Stimmung: {treffer_stimmung:.0%}")
```

Ergebnis im Beispiel (Stichwortregeln):

```text
Trefferquote Thema:    95%
Trefferquote Stimmung: 100%
OK – treffer_thema: 19 von 20 gleich (95%)
OK – treffer_stimmung: 20 von 20 gleich (100%)
```

Die eine Abweichung: Kommentar 15 „Kugelschreiber schreiben nach einer Woche nicht mehr." – Regel `unklar`, Label `Qualität`. Mit Schlüssel gilt dieselbe Rechnung; die Prüfzelle vergleicht mit den tatsächlich vergebenen Werten.

## Aufgabe 4: Themen und Speichern

Themen der ersten 50 (Stichwortregeln): Lieferung 13, Service 11, Onlineshop 8, Qualität 8, Preis 6, unklar 4. Diagrammtitel: „Lieferung ist das häufigste Thema in den ersten 50 Kommentaren (eingeordnet per Stichwortregeln)".

```text
Gespeichert: project/playground/feedback_klassifiziert.csv (50 Zeilen)
stimmung    negativ  neutral  positiv
thema
Lieferung         5        5        3
Onlineshop        4        0        4
Preis             2        0        4
Qualität          3        0        5
Service           4        5        2
unklar            2        2        0
```

Spalten der CSV: `id, datum, kanal, kommentar, stimmung, thema, methode, stimmung_label, thema_label`.

## Aufgabe 5: unklare Kommentare

Vier Zeilen; Ausschnitt mit den Spalten `id` und `kommentar`:

```text
    id                                          kommentar
3    4  Kugelschreiber schreiben nach einer Woche nich...
14  15  Kugelschreiber schreiben nach einer Woche nich...
26  27              Ware war schon am nächsten Morgen da.
44  45              Ware war schon am nächsten Morgen da.
```

Beide Formulierungen enthalten kein Wort aus den Listen. Genau hier liegt der Vorteil eines Sprachmodells: Es braucht keine Wortliste.

## Erweiterung

```python
PROMPT2 = PROMPT.replace(
    "Kommentar: ",
    "Bei Wartezeit, auch mit 'endlich', ist die Stimmung negativ.\n"
    "Produktmängel (kaputt, schreibt nicht) gehören zu Qualität.\n"
    "Kommentar: ",
)
neu = pd.DataFrame([classify(text, prompt=PROMPT2) for text in kommentare["kommentar"]], index=kommentare.index)
gelabelt2 = neu.loc[gelabelt.index]
print(f"Thema:    {(gelabelt2['thema'] == gelabelt['thema_label']).mean():.0%}")
print(f"Stimmung: {(gelabelt2['stimmung'] == gelabelt['stimmung_label']).mean():.0%}")
```

Ohne Schlüssel bleibt es bei 95 % und 100 %, weil die Stichwortregeln den Prompt nicht verwenden. Mit Schlüssel zeigt der Vergleich, ob die zusätzlichen Regeln die Quote verändern; eine Stichprobe von 20 Kommentaren ist dafür nur ein grober Anhaltspunkt.
