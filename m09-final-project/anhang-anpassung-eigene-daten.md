# Checkliste: Anpassung an eigene Daten

Schritt für Schritt vom Skill `monatsbericht` zu einem Skill für eine eigene CSV-Datei. Vorlage ist der Kostenbericht aus [Lab 9.1](l01-cost-report/l01-cost-report-thx.md); fertiges Beispiel: `project/examples/m09-final-project/l01-cost-report/kostenbericht/`.

## 1. Datei prüfen, bevor etwas kopiert wird

- [ ] Freigabe von Datenschutz und IT liegt vor; Namen von Personen und Kunden sind entfernt oder ersetzt.
- [ ] **Langformat:** eine Zeile je Buchung oder je Monat; Monate stehen nicht als Spalten nebeneinander.
- [ ] Mindestens eine Datumsspalte und eine Betragsspalte; optional eine Gruppenspalte (Region, Kostenstelle, Produkt).
- [ ] Datum als TT.MM.JJJJ oder JJJJ-MM-TT.
- [ ] Trennzeichen `;` oder `,`; Dezimalkomma oder Dezimalpunkt; Zeichensatz UTF-8 oder Excel (cp1252).
- [ ] Historie: ab 13 Monaten Vorjahresvergleich, ab 24 Monaten Prognose.
- [ ] Eine Kontrollsumme aus dem Vorsystem für mindestens einen Monat ist bekannt.

| passt | passt nicht |
| --- | --- |
| `Buchungsdatum;Kostenstelle;Betrag` | `Kostenstelle;Jan;Feb;Mär;…` (Monate als Spalten) |
| `datum,produkt,umsatz` | Datei mit Summenzeilen und Leerzeilen zwischen den Blöcken |
| `Monat;Betrag` mit `01.09.2026;1234,50` | Datum als „Sep 26“ |

## 2. Skill-Ordner kopieren

- [ ] Explorer: `.github/skills/monatsbericht` kopieren, im Ordner `.github/skills` einfügen, Kopie mit **F2** umbenennen (Kleinbuchstaben, Bindestriche, z. B. `umsatz-produkte`).
- [ ] In der Kopie von `SKILL.md` sofort `name` = neuer Ordnername und eine neue `description` mit den Wörtern des neuen Themas.
- [ ] Der Skill `monatsbericht` bleibt unverändert.

## 3. Daten ablegen

- [ ] Eigenen Datenordner im Kursordner anlegen (z. B. `data_kosten/`), Datei hineinlegen.
- [ ] Nicht nach `data/`: Dort liest der Nordwind-Skill jede Datei `nordwind_umsatz*.csv`.

## 4. Einstellungen in `scripts/monatsbericht.py`

Nur Block **1. EINSTELLUNGEN** ändern, danach speichern.

| Einstellung | Nordwind | Kostenstellen | eigene Datei |
| --- | --- | --- | --- |
| `DATEN_STANDARD` | `"data"` | `"data_kosten"` | eigener Ordner |
| `MUSTER_STANDARD` | `"nordwind_umsatz*.csv"` | `"kostenstellen*.csv"` | Dateiname, `*` für spätere Monate |
| `AUSGABE_STANDARD` | `"berichte"` | `"berichte/kosten"` | eigener Unterordner von `berichte/` |
| `LESE_OPTIONEN` | `"auto"` | `"auto"` | `"auto"`; nur bei Fehlern festsetzen, z. B. `"trennzeichen": ";"` |
| `SPALTEN["datum"]` | `"datum"` | `"Buchungsdatum"` | Name der Datumsspalte (Pflicht) |
| `SPALTEN["betrag"]` | `"umsatz"` | `"Betrag"` | Name der Betragsspalte (Pflicht) |
| `SPALTEN["gruppe"]` | `"region"` | `"Kostenstelle"` | Gruppenspalte oder `None` |
| `SPALTEN["kunde"]` | `"kunde_id"` | `None` | Kundenspalte oder `None` (ohne: keine Segmente) |
| `SPALTEN["kosten"]` | `"kosten"` | `None` | Kostenspalte oder `None` (ohne: kein Deckungsbeitrag) |
| `ANZEIGENAMEN` | Umsatz, Region | Kosten, Kostenstelle | Wörter für den Bericht |
| `GRUPPE_VORSILBEN`, `GRUPPE_ERSETZEN` | `"Region "`, `"Sued"` → `"Süd"` | unverändert (greift nicht) | eigene Schreibweisen vereinheitlichen |

Spaltennamen genau so schreiben wie in der Kopfzeile der Datei, mit Groß- und Kleinschreibung.

## 5. Testlauf im Terminal

- [ ] `python .github/skills/<name>/scripts/monatsbericht.py bericht --daten <ordner>` läuft ohne `STOPP`.
- [ ] Qualitätscheck lesen: gelesene Zeilen, Dubletten, Schreibweisen, Monatsbereich plausibel.
- [ ] `Summenkontrolle:` gegen die Kontrollsumme aus dem Vorsystem oder eine Gegenrechnung (Notebook aus Lab 9.1) prüfen.

| Meldung | Lösung |
| --- | --- |
| `STOPP: keine Datei … im Ordner … gefunden` | `--daten` und `MUSTER_STANDARD` prüfen |
| `STOPP: Pflichtspalte … fehlt in …` | Spaltenname in `SPALTEN` wie in der Kopfzeile |
| `STOPP: … der Werte in Spalte … nicht lesbar` | Datumsformat oder Dezimalzeichen passen nicht; `LESE_OPTIONEN` setzen |
| `Prognose übersprungen: nur n Monate Historie` | erwartet bei weniger als 24 Monaten |

## 6. Sollwerte (optional)

- [ ] `kontrollsummen.csv` in den eigenen Datenordner legen, Spalten `monat` (JJJJ-MM), die Gruppenspalte und die Betragsspalte mit denselben Namen wie in `SPALTEN`, z. B. `monat,Kostenstelle,Betrag`.
- [ ] Nur mit Gruppenspalte: Ist `SPALTEN["gruppe"]` gleich `None`, meldet v2 auch bei richtigen Zahlen Abweichungen. Dann ohne `kontrollsummen.csv` arbeiten und die Zeile `Summenkontrolle:` gegen das Vorsystem prüfen.
- [ ] Danach meldet die Ausgabe `Sollwert-Prüfung: bestanden` oder `n Abweichungen` statt „übersprungen“.

## 7. `SKILL.md` anpassen und auslösen

- [ ] Befehle: Skriptpfad `.github/skills/<name>/scripts/monatsbericht.py`, `--daten <ordner>`.
- [ ] Wann verwenden: Beispielfragen des neuen Themas; „nicht verwenden für Umsatz“.
- [ ] Antwortformat: Spalten der eigenen Kennzahlentabelle, Prüfzeilen wörtlich, Pfade unter dem eigenen Ausgabeordner.
- [ ] Neuer Chat, Satz mit den Wörtern aus der Beschreibung; Skill-Regeln 2–5.
- [ ] Gegenprobe: Eine Umsatzfrage löst weiterhin `monatsbericht` aus, nicht den neuen Skill.
