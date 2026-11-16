# Lab 9.1 – Übung: Das Muster auf eigene Daten übertragen

**Dauer:** ca. 35 Minuten, danach kurze Vorstellung
**Ändert die Nordwind-Projektbasis?** Nein — es entsteht ein zweiter Skill `kostenbericht`; der Skill `monatsbericht` bleibt unverändert.
**Arbeitsdateien:** `.github/skills/kostenbericht/` (Kopie des eigenen Skills `monatsbericht`), `project/playground/m09-l01-gegenrechnung.ipynb`
**Starter:** `project/starters/m09-l01-gegenrechnung.ipynb` · **Beispiel:** `project/examples/m09-final-project/l01-cost-report/` (Skill `kostenbericht/`, `gegenrechnung.ipynb`, `berichte/kosten/`)

## Vorbereitung

- Der Skill `.github/skills/monatsbericht/` aus Lab 7.2 ist vorhanden.
- `lieferungen/kostenstellen.csv` liegt bereit (`;`, Dezimalkomma, cp1252, Spalten Buchungsdatum, Kostenstelle, Betrag).
- Checkliste zum Nachschlagen: [Anpassung an eigene Daten](../anhang-anpassung-eigene-daten.md).

## Aufgaben

1. Kopiere im Explorer den Ordner `.github/skills/monatsbericht` (Rechtsklick → **Copy**, dann Rechtsklick auf `.github/skills` → **Paste**) und benenne die Kopie mit **F2** in `kostenbericht` um. Ändere sofort in `.github/skills/kostenbericht/SKILL.md` die Zeilen `name` und `description` und speichere:

   ```yaml
   name: kostenbericht
   description: Erstellt den Monatsbericht Kosten je Kostenstelle (Vertrieb, Marketing, IT, Fuhrpark, Gebäude, Personalentwicklung) mit Vormonat, Vorjahr, auffälligen Tagen und Prognose aus data_kosten/kostenstellen.csv mit dem Skript scripts/monatsbericht.py und meldet Summenkontrolle und Sollwert-Prüfung. Verwenden bei Fragen nach Kosten, Kostenbericht, Kostenstelle oder Kosten je Kostenstelle eines Monats.
   ```

2. Lege im Wurzelordner einen Ordner `data_kosten` an (Rechtsklick auf eine freie Stelle im Explorer → **New Folder…**) und verschiebe `lieferungen/kostenstellen.csv` dorthin.
3. Öffne `.github/skills/kostenbericht/scripts/monatsbericht.py` und ändere nur im Block **1. EINSTELLUNGEN** diese Werte; speichere und führe den Bericht aus:

   | Einstellung | bisher | neu |
   | --- | --- | --- |
   | `DATEN_STANDARD` | `"data"` | `"data_kosten"` |
   | `MUSTER_STANDARD` | `"nordwind_umsatz*.csv"` | `"kostenstellen*.csv"` |
   | `AUSGABE_STANDARD` | `"berichte"` | `"berichte/kosten"` |
   | `SPALTEN` | `datum`, `umsatz`, `region`, `kunde_id`, `kosten` | `"Buchungsdatum"`, `"Betrag"`, `"Kostenstelle"`, `None`, `None` |
   | `ANZEIGENAMEN` | `"betrag": "Umsatz"`, `"gruppe": "Region"` | `"betrag": "Kosten"`, `"gruppe": "Kostenstelle"` |

   ```bash
   python .github/skills/kostenbericht/scripts/monatsbericht.py bericht --daten data_kosten
   ```

   Öffne `berichte/kosten/bericht_2026_09_v2.html` im Browser.

4. Beginne einen neuen Chat im Modus **Agent** und lass Copilot das Vorgehen anpassen; prüfe die Änderung und wähle **Keep**:

   > Die Datei `#file:.github/skills/kostenbericht/SKILL.md` ist eine Kopie des Skills monatsbericht. Der Skill wertet jetzt `data_kosten/kostenstellen.csv` aus (Kosten je Kostenstelle; Spalten Buchungsdatum, Kostenstelle, Betrag). Passe nur die Abschnitte `## Wann verwenden`, `## Vorgehen` und `## Antwortformat` sowie den Titel an: Beispielfragen zu Kosten je Kostenstelle, nicht verwenden für Umsatz; Skriptpfad `.github/skills/kostenbericht/scripts/monatsbericht.py`; in jedem Befehl `--daten data_kosten` statt `--daten data`; Kennzahlentabelle mit Kostenstelle, Kosten, Δ Vormonat %, Δ Vorjahr %; Berichtspfade `berichte/kosten/bericht_JJJJ_MM_v2.html` und `berichte/kosten/kpi_JJJJ_MM.xlsx`. Die Zeilen Summenkontrolle und Sollwert-Prüfung bleiben wörtlich im Antwortformat, die Regel zu `STOPP:` bleibt. Ändere `name` und `description` nicht und führe keine Befehle aus.

   Sende danach in einem neuen Chat „Erstelle den Kostenbericht je Kostenstelle für September 2026.“ und erlaube nur den Befehl aus `SKILL.md` (Skill-Regeln 2–5).
5. Kopiere `project/starters/m09-l01-gegenrechnung.ipynb` nach `project/playground/`, führe die erste Zelle aus und fülle die Zelle mit `AUFGABE 1` mit Copilot (Modus Ask, Notebook mit `#file` anhängen) und diesem Prompt; führe danach die Prüfzelle aus:

   > Im Notebook ist `DATEI` der Pfad zu `kostenstellen.csv`, einem deutschen Excel-Export: Trennzeichen `;`, Dezimalkomma, Zeichensatz cp1252, Spalten `Buchungsdatum` (Format TT.MM.JJJJ), `Kostenstelle`, `Betrag`. Schreibe Code für eine Notebook-Zelle: Lies die Datei mit pandas (`sep=";"`, `decimal=","`, `encoding="cp1252"`) in die Variable `kosten`, bilde eine Spalte `monat` im Format JJJJ-MM aus `Buchungsdatum` und erzeuge die Tabelle `je_monat` mit Index `monat` und den Spalten `zeilen` (Anzahl Buchungen) und `summe` (Summe von `Betrag`). Zeige zum Schluss `je_monat.tail(3)`. Gib nur den Code aus.

   **Claude Code:** Prompts im Claude-Code-Panel senden, Dateien mit `@` nennen.

## Checkpoint

- Nach Aufgabe 3 enden Terminal und Bericht mit:

  ```text
  Summenkontrolle: 2026-09 – 42 Zeilen, Summe Kosten 17.091,47 – stimmt mit der Kennzahlentabelle überein
  Sollwert-Prüfung: keine Sollwert-Datei – übersprungen
  ```

- Nach Aufgabe 4 enthält die Antwort dieselben zwei Zeilen und die Kennzahlentabelle mit sechs Kostenstellen und Gesamt.
- Nach Aufgabe 5 meldet die Prüfzelle `OK – Gegenrechnung 2026-09: 42 Buchungen, Summe 17.091,47 € = Summenkontrolle des Berichts`.

## Abschlusskriterien

- Zweiter Skill `.github/skills/kostenbericht/` löst mit einem Satz zu Kosten aus; `monatsbericht` reagiert weiter auf Umsatzfragen.
- `berichte/kosten/bericht_2026_09_v2.html` liegt vor; die Gegenrechnung bestätigt die Summenkontrolle.

## Erweiterung

Dasselbe mit der eigenen CSV im Langformat (Datum und Betrag je Zeile, mindestens 13 Monate): Datei nach `data_kosten/` legen, in der Skript-Kopie `MUSTER_STANDARD` und `SPALTEN` auf die eigene Datei und ihre Spaltennamen setzen, `bericht` ausführen. Das Muster nennt den eigenen Dateinamen, damit `kostenstellen.csv` im selben Ordner nicht mitgelesen wird. In der Gegenrechnung `DATEI` sowie Trennzeichen, Dezimalzeichen, Zeichensatz und Spaltennamen anpassen.

## Abschluss

- **Vorstellung:** zwei Berichte im Browser zeigen (je 2–3 Minuten).
- **Transfer im Kursabschluss:** [Checkliste Voraussetzungen im Job](../anhang-voraussetzungen-job.md) für den eigenen ersten Fall durchgehen.

## Fallback

- Kopie kaputt: Ordner `.github/skills/kostenbericht` löschen und `project/examples/m09-final-project/l01-cost-report/kostenbericht/` nach `.github/skills/` kopieren.
- KI-Assistent nicht verfügbar: Aufgabe 4 mit `SKILL.md` aus dem Beispiel; Befehl aus Aufgabe 3 im Terminal (Skill-Regel 4); in Aufgabe 5 das Lösungs-Snippet aus der Lösung einsetzen.
