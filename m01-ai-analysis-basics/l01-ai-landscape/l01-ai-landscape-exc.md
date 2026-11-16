# Lab 1.1 – Übung: Das große Bild und die Nordwind-Daten

**Dauer:** ca. 20 Minuten
**Ändert die Nordwind-Projektbasis?** Nein – erste Läufe im eigenen Arbeitsbereich `project/playground/`.

## Vorbereitung

- VS Code ist geöffnet, im Explorer links steht der Kursordner mit `data/`, `project/` und `check_setup.py`.
- Skript: [`project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py`](../../project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py)
- Starter: [`project/starters/m01-l01-erste-zahlen.ipynb`](../../project/starters/m01-l01-erste-zahlen.ipynb) · Arbeitsdatei: `project/playground/m01-l01-erste-zahlen.ipynb`

## Aufgaben

1. Öffne über das Menü **Terminal → Neues Terminal** ein Terminal und führe die Prüfung der Kursumgebung aus:

   ```bash
   python check_setup.py
   ```

2. Führe die KI-Landkarte für die Region Nord aus; der Browser öffnet eine Seite mit drei Diagrammen:

   ```bash
   python project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py --region Nord
   ```

3. Hole den Befehl mit der Pfeiltaste nach oben zurück, ändere nur das Argument auf `--region West` und führe ihn erneut aus. Suche im dritten Diagramm den 27.11.2025.
4. Kopiere den Starter in den Arbeitsbereich: im Explorer Rechtsklick auf `project/starters/m01-l01-erste-zahlen.ipynb` → **Copy**, dann Rechtsklick auf den Ordner `project/playground` → **Paste**.
5. Öffne `project/playground/m01-l01-erste-zahlen.ipynb` und führe alle Zellen von oben nach unten mit **Umschalt+Enter** aus, bis die Tabelle „Umsatz 2025 je Region" erscheint.

## Checkpoint

- `check_setup.py` endet mit „Alles bereit." (oder nennt genau die Punkte, die noch fehlen).
- Das Terminal zeigt für West `Trendfaktor 1.131` und `4 auffällige(r) Tag(e)`, darunter `27.11.2025`.
- Die Notebook-Zelle „Umsatz 2025 je Region" zeigt 14 Zeilen statt 4, z. B. `Nord` 993077.30 und `Region Nord` 30047.41.

## Abschlusskriterien

- `project/playground/ki_landkarte.html` existiert und zeigt drei Diagramme.
- `project/playground/m01-l01-erste-zahlen.ipynb` ist ausgeführt, jede Zelle hat eine Ausgabe.

## Erweiterung

Ersetze in der Zelle „Umsatz 2025 je Region" den Spaltennamen `"region"` durch `"kanal"` und führe die Zelle erneut aus. Vergleiche die Zahl der Zeilen mit der Ausgabe für `region`.

## Fallback

- Startet der Browser nicht: `project/playground/ki_landkarte.html` im Explorer per Rechtsklick → **Reveal in File Explorer** (macOS: **Reveal in Finder**) öffnen und doppelklicken.
- Läuft das Notebook nicht: das fertige Beispiel [`project/examples/m01-ai-analysis-basics/l01-ai-landscape/erste_zahlen.ipynb`](../../project/examples/m01-ai-analysis-basics/l01-ai-landscape/erste_zahlen.ipynb) öffnen; es enthält alle Ausgaben.
