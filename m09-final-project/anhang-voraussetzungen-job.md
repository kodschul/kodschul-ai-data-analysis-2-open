# Checkliste: Voraussetzungen im Job

Was im eigenen Unternehmen geklärt sein muss, bevor das Muster aus dem Kurs (Skript rechnet, KI erklärt, Skill löst aus) mit echten Daten läuft. Hintergrund: Strategie in [Lab 9.1](l01-cost-report/l01-cost-report-thx.md).

## Technik

- [ ] **Python 3** auf dem Arbeitsrechner, mit den Paketen aus `requirements.txt` (pandas, numpy, openpyxl, plotly, scikit-learn).
- [ ] **VS Code** mit den Erweiterungen Python und Jupyter, oder eine andere freigegebene Umgebung.
- [ ] **Freigegebener KI-Assistent** mit Firmenkonto (z. B. GitHub Copilot Business oder Claude Code), der Agent Skills unterstützt; Version und Skill-Ordner vor dem Start prüfen.
- [ ] Ein Ordner für Skripte, Skills und Daten, auf den nur die Berechtigten zugreifen.

## Freigaben

- [ ] **Datenschutz:** Welche Daten dürfen lokal verarbeitet werden? Personen- und Kundenbezug entfernt?
- [ ] **KI-Dienst:** Was darf in Prompts und Chat? Beim Skill gehen Befehl und Terminal-Ausgabe an den Dienst (Lab 7.1), Rohdaten nicht.
- [ ] **API-Schlüssel** (nur für Werkzeuge wie PandasAI, Lab 4.1): Wer stellt ihn, mit welchem Budgetlimit?
- [ ] IT-Sicherheit und, wo nötig, Betriebsrat informiert.
- [ ] EU-KI-Verordnung (Verordnung (EU) 2024/1689): Einordnung des Einsatzes mit der zuständigen Stelle geklärt (Lab 8.1).

## Prüfung und Verantwortung

- [ ] **Kontrollsumme aus dem Vorsystem** (ERP, Hauptbuch, BI) je Monat verfügbar, am besten als Datei für die Sollwert-Prüfung.
- [ ] **Verantwortliche** benannt: wer pflegt Skript und `SKILL.md`, wer gibt den Bericht frei.
- [ ] **Prüfregeln** festgelegt: Toleranz für Abweichungen, Vorgehen bei `STOPP`, wer die Lieferung neu anfordert.
- [ ] Der Bericht geht erst nach Prüfung der beiden Prüfzeilen hinaus.

## Erster Fall

- [ ] Ein wiederkehrender Bericht ausgewählt, ein Empfänger, ein Datensatz im Langformat (Checkliste [Anpassung an eigene Daten](anhang-anpassung-eigene-daten.md)).
- [ ] Ziel für vier Wochen: Bericht entsteht per Satz oder Befehl, Summe stimmt mit dem Vorsystem, eine zweite Person kann ihn erzeugen.

## Material

- [ ] Kursmaterial griffbereit: Handouts, Cheatsheets (z. B. [Skills](../m07-analysis-skill/skill-cheatsheet.md)) und die fertigen Beispiele in `project/examples/`.
