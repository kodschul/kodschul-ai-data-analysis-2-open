# Setup und Installation

Alle Übungen laufen in **VS Code** auf einer vorbereiteten Schulungs-VM. Diese Seite zeigt, was installiert ist, wie der Kursordner aufgebaut ist, wie die Anmeldung im KI-Assistenten vorbereitet wird und wie sich die eigenen Python-Grundlagen vorab prüfen lassen.

## Ausstattung der Schulungs-VM

| Software | Zweck im Kurs | Prüfen mit |
| --- | --- | --- |
| Python 3.11 | alle Übungen; in VS Code als Interpreter vorausgewählt | `python --version` |
| VS Code mit den Erweiterungen Python, Jupyter, GitHub Copilot Chat | Hauptfenster: Notebooks, Terminal, KI-Assistent, Skills, Handouts | Erweiterungen-Ansicht (`Strg+Umschalt+X`) |
| GitHub Copilot Chat oder Claude Code | KI-Assistent ab Lab 1.2, Skills ab Modul 7 | Chat-Ansicht öffnet sich (`Strg+Alt+I`) |
| Excel oder LibreOffice Calc | Excel-Export ansehen (Lab 6.2) | Datei öffnen |
| Browser | HTML-Berichte und Diagramme ansehen | – |
| Python-Pakete aus `requirements.txt` | pandas, numpy, openpyxl, plotly, scikit-learn, pandasai, pandasai-litellm, matplotlib, ipykernel | `python check_setup.py` |
| Umgebungsvariable `OPENAI_API_KEY` | Kurs-Schlüssel für PandasAI (Lab 4.1) und `classify()` (Lab 4.2) | `python check_setup.py` |

Git und Docker Desktop sind auf der VM vorhanden, werden aber in keinem Lab gebraucht.

**Claude Code:** Wird statt Copilot Chat Claude Code genutzt, ist es auf der VM vorkonfiguriert; die Labs bleiben gleich, abweichende Bedienung steht jeweils in einer eigenen Zeile.

## Der Kursordner

VS Code öffnet den Kursordner als einzigen Arbeitsbereich. Alle Befehle laufen im Terminal von VS Code (`Terminal > Neues Terminal`), das automatisch in diesem Ordner startet.

```text
Kursordner/
├── 00-setup-and-installation.md     diese Seite
├── m00-overview/ … m09-final-project/   Handouts je Modul und Lab
├── data/                Startbestand: Umsatz, Plan, Feedback, Kontrollsummen
├── lieferungen/         spätere Lieferungen (erst ab Lab 7.3 gebraucht)
├── project/
│   ├── examples/        fertiges Ergebnis je Lab
│   ├── starters/        Startdateien der Übungen
│   └── playground/      eigener Arbeitsbereich
├── .github/skills/      Skills für den KI-Assistenten (ab Lab 7.1)
├── check_setup.py       prüft die Umgebung
├── check_zahlen.py      prüft Zahlen gegen die Kontrollsummen
└── requirements.txt     Python-Pakete mit festen Versionen
```

- Handouts lassen sich in VS Code lesbar anzeigen: Datei öffnen, dann `Strg+Umschalt+V` (Markdown-Vorschau).
- Alle Pfade in Skripten und Notebooks gelten ab dem Kursordner, z. B. `data/nordwind_umsatz.csv`. Damit das auch in Notebooks gilt, ist in VS Code die Einstellung `jupyter.notebookFileRoot` auf `${workspaceFolder}` gesetzt.
- Dateien verschieben oder kopieren: im Explorer von VS Code per Rechtsklick (`Kopieren`, `Einfügen`) oder Ziehen.
- Startzustand der Daten wiederherstellen: `python project/data/generate_data.py` erzeugt alle Dateien in `data/` und `lieferungen/` neu.

## Umgebung prüfen

```bash
python check_setup.py
```

Erwartete Ausgabe (Versionen gekürzt):

```text
OK          Python 3.11.x (erwartet 3.11)
OK          pandas 2.3.3
…
OK          .github/skills/kpi-kurzcheck/SKILL.md
OK          Umgebungsvariable OPENAI_API_KEY gesetzt (Wert wird nicht angezeigt)

Alles bereit.
```

`python check_setup.py --llm` schickt zusätzlich eine Testfrage an das Sprachmodell des Kurses.

| Symptom | Ursache | Lösung |
| --- | --- | --- |
| `NICHT OK  pandas fehlt …` | Pakete nicht im gewählten Interpreter | `python -m pip install -r requirements.txt` |
| `NICHT OK  data/…` | Terminal steht nicht im Kursordner | neues Terminal öffnen; VS Code muss den Kursordner geöffnet haben |
| `NICHT OK  Umgebungsvariable …` | Schlüssel fehlt | VS Code neu starten; sonst Trainer fragen |
| Python 3.12 oder neuer | falscher Interpreter | `Strg+Umschalt+P` > `Python: Select Interpreter` > Python 3.11 |

## Anmeldung im KI-Assistenten vorbereiten

Pro Kurs wird eine von zwei Varianten genutzt; die Einladung nennt die gültige.

| Variante | Vor dem Kurs | Am Kurstag |
| --- | --- | --- |
| **A: GitHub Copilot** | GitHub-Konto anlegen oder vorhandenes nutzen, Einladung in die Kurs-Organisation per E-Mail annehmen, Zwei-Faktor-Anmeldung einrichten ([GitHub Docs](https://docs.github.com/de/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)) | in VS Code unten links über das Konto-Symbol mit GitHub anmelden, Chat öffnen, Testfrage stellen |
| **B: Claude Code** | nichts | ist auf der VM angemeldet; Chat öffnen, Testfrage stellen |

Stand: 11/2026, vor Kursbeginn prüfen. Copilot Free reicht wegen des begrenzten Chat-Kontingents für den Kurs voraussichtlich nicht.

## Python-Selbstcheck

Der Kurs setzt Python-Grundlagen voraus. Fünf kurze Aufgaben zeigen, ob sie sitzen; jede ist in wenigen Minuten lösbar. Schreibe den Code in eine Datei `selbstcheck.py` und führe sie mit `python selbstcheck.py` aus.

1. Lege eine Variable `umsatz = 1250.5` an und gib `Umsatz: 1250.5 €` aus.
2. Lege eine Liste `monate = ["Jan", "Feb", "Mär"]` an und gib die Anzahl der Einträge aus.
3. Lege ein Dictionary `regionen = {"Nord": 120, "Süd": 95}` an und gib den Wert für `"Süd"` aus.
4. Schreibe eine Funktion `marge(umsatz, kosten)`, die `(umsatz - kosten) / umsatz` zurückgibt, und gib `marge(200, 150)` aus.
5. Gib mit einer `for`-Schleife jede Region aus `regionen` mit ihrem Wert aus.

<details>
<summary>Lösung</summary>

```python
umsatz = 1250.5
print(f"Umsatz: {umsatz} €")

monate = ["Jan", "Feb", "Mär"]
print(len(monate))                 # 3

regionen = {"Nord": 120, "Süd": 95}
print(regionen["Süd"])             # 95

def marge(umsatz, kosten):
    return (umsatz - kosten) / umsatz

print(marge(200, 150))             # 0.25

for name, wert in regionen.items():
    print(name, wert)
```

</details>

Laufen alle fünf ohne Hilfe, passt die Vorbereitung. pandas, Terminal und Notebooks sind nicht nötig; Lab 1.1 und Lab 2.1 führen sie ein.

## Optional: eigene Daten für das Abschlussprojekt

Im Abschlussprojekt (Lab 9.1) lässt sich als Erweiterung eine eigene Datei verwenden. Sie muss anonymisiert und für die Nutzung freigegeben sein.

| Anforderung | Beispiel |
| --- | --- |
| CSV im **Langformat**: eine Zeile je Buchung oder Monat | `Buchungsdatum;Kostenstelle;Betrag` |
| mindestens eine Datums- und eine Betragsspalte | `01.03.2026;Marketing;1250,40` |
| Trennzeichen `;` oder `,`, Dezimalkomma erlaubt | Excel-Export „CSV (Trennzeichen-getrennt)" |
| mindestens 13 Monate (Vorjahresvergleich), 24 Monate für die Prognose | 01/2024–09/2026 |

Breite Exporte mit einer Spalte je Monat passen nicht. Für alle anderen Fälle liegt der Übungsdatensatz `lieferungen/kostenstellen.csv` bereit.
