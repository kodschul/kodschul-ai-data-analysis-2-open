# Lab 2.1 – Übung: Datenqualität prüfen

**Dauer:** ca. 15 Minuten
**Ändert die Nordwind-Projektbasis?** Nein – die Rohdatei bleibt unverändert; es entsteht die Problemtabelle `probleme.csv` für Lab 2.2.

## Vorbereitung

- Starter: [`project/starters/m02-l01-datenqualitaet.ipynb`](../../project/starters/m02-l01-datenqualitaet.ipynb) · Arbeitsdatei: `project/playground/m02-l01-datenqualitaet.ipynb`
- Kopieren wie in Lab 1.1: Rechtsklick auf den Starter → **Copy**, Rechtsklick auf `project/playground` → **Paste**.

## Aufgaben

1. Kopiere den Starter nach `project/playground/`, öffne ihn und führe die Zellen von oben bis einschließlich „Prüfung 6: Ausreißer" mit **Umschalt+Enter** aus.
2. Öffne den Chat (**Strg+Alt+I**), beginne einen neuen Chat im Modus **Ask** und sende diesen Prompt (`#file:` über `#` auswählen):

   > Kontext: In #file:m02-l01-datenqualitaet.ipynb ist die Nordwind-Umsatzdatei als pandas-DataFrame `df` geladen.
   > Spalten: beleg_nr, datum, jahr, kunde_id, region, produktgruppe, kanal, menge, umsatz, kosten.
   > Regel: Jede unterschiedliche Schreibweise in der Spalte `region` zählt einzeln, auch Leerzeichen am Rand und Groß-/Kleinschreibung. `df` nicht verändern, nichts bereinigen.
   > Gewünschte Ausgabe: eine Variable `regionen` mit jeder Schreibweise und ihrer Zeilenzahl, absteigend sortiert, dazu `print(regionen)`. Nur der Code für eine Notebook-Zelle, ohne Erklärung.

3. Prüfe den vorgeschlagenen Code mit den drei Lesefragen, füge ihn in der Zelle „Prüfung 7" zwischen `# >>> AUFGABE 1` und `# <<< ENDE AUFGABE 1` ein und führe diese Zelle und die Prüfzelle darunter aus.
4. Führe die letzte Zelle „Problemtabelle" aus.

## Checkpoint

- Prüfung 3 und 4 zeigen `kosten 657` und `Dubletten: 398`.
- Die Prüfzelle meldet `OK – 14 Schreibweisen für 4 Regionen gefunden.`
- Bei `nicht OK`: Prompt ein zweites Mal senden; danach das Lösungs-Snippet aus der Lösung einfügen.

## Abschlusskriterien

- Die Problemtabelle hat fünf Einträge mit Anzahl und Vorschlag, keiner davon „fehlt – Aufgabe 1".
- `project/playground/probleme.csv` existiert.

## Erweiterung

Lass Copilot mit einem eigenen Prompt (Kontext + Spalten + Regel + gewünschte Ausgabe) ein Skript `project/playground/quality_check.py` schreiben, das den Dateinamen als Argument bekommt und dieselbe Problemtabelle im Terminal ausgibt. Teste es mit `data/nordwind_umsatz.csv` und mit `lieferungen/nordwind_umsatz_2026_10_defekt.csv` und vergleiche mit [`quality_check.py`](../../project/examples/m02-data-preparation/l01-data-quality/quality_check.py) aus dem Beispiel.

## Fallback

Ohne Copilot: das Lösungs-Snippet aus der Lösung einfügen. Fertiges Notebook mit allen Ausgaben: [`datenqualitaet.ipynb`](../../project/examples/m02-data-preparation/l01-data-quality/datenqualitaet.ipynb).
