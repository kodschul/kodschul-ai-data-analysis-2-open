---
name: kpi-kurzcheck
description: Schneller Überblick über die Nordwind-Umsatzdatei data/nordwind_umsatz.csv – Zeilenzahl, Monatsbereich und Gesamtumsatz der Rohdaten. Verwenden, wenn nach dem KPI-Kurzcheck, einem Kurzcheck, Schnellcheck oder Überblick über die Nordwind-Daten gefragt wird.
---

# KPI-Kurzcheck

Zeigt drei Eckdaten der Rohdatei `data/nordwind_umsatz.csv`. Die Zahlen rechnet immer das Skript, nie das Sprachmodell.

## Vorgehen

1. Im Wurzelordner des Arbeitsbereichs diesen Befehl ausführen:

   ```bash
   python .github/skills/kpi-kurzcheck/scripts/kpi_kurzcheck.py
   ```

2. Die vier Ausgabezeilen des Skripts unverändert wiedergeben.
3. Danach in einem Satz sagen, dass es Rohdaten vor der Bereinigung sind.

## Regeln

- Keine Zahl selbst berechnen, schätzen oder runden.
- Meldet das Skript `STOPP`, die Meldung wiedergeben und nichts weiter rechnen.
