# Glossar

| Begriff | Bedeutung | Lab |
| --- | --- | --- |
| Agent-Modus | Chat-Modus, in dem der KI-Assistent Dateien ändert und Befehle ausführt | 1.2 |
| Anomalie | Wert, der deutlich vom Üblichen abweicht; nicht automatisch ein Fehler | 5.3 |
| Argument | Zusatzangabe beim Start eines Skripts, z. B. `--monat 2026-09` | 1.1 |
| Ask-Modus | Chat-Modus, in dem der KI-Assistent nur antwortet | 1.2 |
| Backtest | Prognose für Monate, deren Ergebnis schon bekannt ist | 6.1 |
| Bestätigungsdialog | Rückfrage des Agenten, bevor er einen Befehl ausführt | 7.1 |
| Bias | systematische Verzerrung in Daten oder Ergebnis | 8.1 |
| Clustering | Gruppieren ähnlicher Datensätze ohne vorgegebene Zielgröße | 5.2 |
| CSV | Textdatei mit einer Tabellenzeile pro Zeile, Werte durch Trennzeichen getrennt | 1.1 |
| DataFrame | Tabelle in pandas, entspricht einem Tabellenblatt | 2.1 |
| Deckungsbeitrag | Umsatz minus Kosten | 2.3 |
| Deep Learning | Machine Learning mit vielschichtigen neuronalen Netzen | 1.1 |
| deterministisch | gleiche Eingabe ergibt immer dasselbe Ergebnis | 3.3 |
| Dublette | doppelt gelieferte, identische Zeile | 2.1 |
| Elbow-Diagramm | Hilfe zur Wahl der Segmentanzahl: der Knick zeigt eine sinnvolle Zahl | 5.2 |
| explorative Datenanalyse (EDA) | erstes Erkunden von Daten nach Mustern und Auffälligkeiten | 3.1 |
| Feature (Merkmal) | Spalte, aus der ein Modell lernt | 2.3 |
| Feature Engineering | neue Spalten aus vorhandenen ableiten | 2.3 |
| Fehlalarm | als auffällig markierter Wert, der fachlich normal ist | 5.3 |
| generative KI | KI, die neue Inhalte wie Text oder Code erzeugt | 1.1 |
| Genauigkeit | Anteil richtiger Vorhersagen | 5.1 |
| `groupby` | pandas-Befehl zum Gruppieren und Zusammenfassen, wie eine Pivot-Tabelle | 2.1 |
| k-Means | Clustering-Verfahren, das Punkte um k Mittelpunkte gruppiert | 5.2 |
| Kernel | Python-Prozess, der die Zellen eines Notebooks ausführt | 1.1 |
| Kontrollsumme | unabhängig ermittelter Sollwert zum Abgleich, z. B. aus dem Vorsystem | 2.3 |
| Langformat | Tabelle mit einer Zeile je Buchung oder Monat statt einer Spalte je Monat | 9.1 |
| LiteLLM | Python-Bibliothek, die viele Sprachmodell-Dienste einheitlich anspricht | 4.1 |
| Machine Learning (ML) | Verfahren, die Regeln aus Beispieldaten lernen | 1.1 |
| MAPE | mittlere prozentuale Abweichung: „im Schnitt x % daneben" | 6.1 |
| Marge | Deckungsbeitrag geteilt durch Umsatz, immer aus Summen berechnet | 2.3 |
| Messlatte (Baseline) | einfachste Vergleichslösung, die ein Modell schlagen muss | 5.1 |
| Mittelwert | Summe geteilt durch Anzahl | 5.3 |
| naive Prognose | Prognose = Wert des Vorjahresmonats | 6.1 |
| Notebook | Datei aus Code- und Textzellen mit Ergebnis direkt darunter | 1.1 |
| PandasAI | Bibliothek, mit der sich einer Tabelle Fragen in Alltagssprache stellen lassen | 4.1 |
| pandas | Python-Bibliothek für Tabellen | 2.1 |
| plotly | Python-Bibliothek für interaktive Diagramme | 3.2 |
| Pflichtspalte | Spalte, ohne die das Skript nicht rechnet und stoppt | 6.2 |
| prädiktive KI | KI, die Werte vorhersagt oder einordnet | 1.1 |
| Prompt | Auftrag in Textform an ein Sprachmodell | 1.2 |
| Prüfzelle | fertige Notebook-Zelle, die „OK" oder „nicht OK" meldet | 2.1 |
| RFM | Kundenmerkmale: wie lange her, wie oft, wie viel gekauft | 2.3 |
| Saison | wiederkehrendes Muster im Jahresverlauf | 6.1 |
| Segment | Gruppe ähnlicher Kunden | 5.2 |
| Skalieren | Spalten auf vergleichbare Größenordnung bringen | 5.2 |
| Skill | Ordner mit `SKILL.md` und Skript, den der KI-Assistent bei Bedarf nutzt | 7.1 |
| `SKILL.md` | Beschreibung eines Skills: Name, Auslöser, Vorgehen, Antwortformat | 7.1 |
| Sollwert-Prüfung | Abgleich der Ergebnisse mit `kontrollsummen.csv` | 6.2 |
| Spaltenrolle | Zuordnung einer echten Spalte zu einer Aufgabe, z. B. `betrag` = „Umsatz" | 6.2 |
| Sprachmodell (LLM) | KI, die Text versteht und erzeugt | 1.1 |
| SQL | Abfragesprache für Tabellen: `SELECT`, `WHERE`, `GROUP BY` | 4.1 |
| Standardabweichung | typischer Abstand der Werte vom Mittelwert | 5.3 |
| strukturierte Daten | Daten in Tabellenform mit festen Spalten | 1.1 |
| Summenkontrolle | Prüfzeile mit Zeilenzahl und Summe des Berichtsmonats | 6.2 |
| Terminal | Fenster für Textbefehle, z. B. `python check_setup.py` | 1.1 |
| Testdaten | zurückgehaltene Daten, an denen ein Modell geprüft wird | 5.1 |
| Trainingsdaten | Daten, aus denen ein Modell lernt | 5.1 |
| Trend | langfristige Richtung einer Zeitreihe | 6.1 |
| Trendfaktor | Umsatz der letzten 12 Monate geteilt durch die 12 Monate davor | 6.1 |
| Überanpassung | Modell lernt Trainingsdaten auswendig und versagt bei neuen Daten | 5.1 |
| überwachtes Lernen | Lernen aus Beispielen mit bekannter Zielgröße | 5.1 |
| unstrukturierte Daten | Freitext, Bilder, E-Mails ohne feste Spalten | 1.1 |
| unüberwachtes Lernen | Muster finden ohne Zielgröße | 5.1 |
| Zielgröße | Spalte, die ein Modell vorhersagen soll, z. B. `wiederkauf` | 5.1 |
