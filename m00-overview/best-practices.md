# Best Practices

## Daten

| Regel | Warum |
| --- | --- |
| Jede Lieferung zuerst prüfen | Dubletten und Schreibweisen verfälschen jede Summe |
| Bereinigen per Funktion, nicht per Klick | nächsten Monat läuft dieselbe Regel wieder |
| Zeilenbilanz ausgeben | zeigt, dass nichts still verloren ging |
| Fehlende Werte markieren statt löschen | der Umsatz zählt, auch ohne Kosten |
| Marge aus Summen berechnen | der Durchschnitt der Zeilenmargen ist falsch |

## Arbeiten mit dem KI-Assistenten

| Regel | Warum |
| --- | --- |
| Prompt mit Kontext, Spalten, Regel, Ausgabe | weniger Raten, passender Code |
| KI-Code vor dem Ausführen lesen | Welche Datei? Was wird verändert? Was wird ausgegeben? |
| Zahlen nie im Chat rechnen lassen | jeder Lauf kann anders rechnen |
| Nur freigegebene Daten an KI-Dienste | Spalten und Beispielzeilen verlassen das Haus |
| Ein festes Modell für wiederkehrende Aufgaben | gleiches Verhalten bei jedem Lauf |

## Analyse und Modelle

| Regel | Warum |
| --- | --- |
| Befund als Diagrammtitel | die Aussage steht vor dem Bild |
| Jede Prognose gegen die naive Prognose testen | sonst ist unklar, ob das Modell etwas bringt |
| Modell an Testdaten bewerten | Trainingsdaten schmeicheln |
| Jede Auffälligkeit fachlich prüfen | Großauftrag oder Tippfehler sieht die Regel nicht |
| Korrelation nicht als Ursache verkaufen | Saison und Trend erklären oft mehr |

## Bericht und Skill

| Regel | Warum |
| --- | --- |
| Das Skript rechnet, die KI erklärt | Zahlen bleiben gleich und prüfbar |
| Zwei feste Prüfzeilen in jeder Ausgabe | zeigen, dass das Skript gelaufen ist |
| Bei fehlender Pflichtspalte stoppen | kein Bericht ist besser als ein falscher |
| Einstellungen oben im Skript bündeln | neue Daten = Einstellungen ändern, nicht Code |
| Im Bestätigungsdialog nur bekannte Befehle erlauben | der Agent führt sonst beliebige Befehle aus |
