# Cheatsheet: Machine Learning und Prognose

Schnellreferenz für Modul 5 (Wiederkauf, Segmente, Auffälligkeiten) und die Prognose aus Lab 6.1. Alle Befehle laufen in Notebooks mit dem Kursordner als Arbeitsverzeichnis.

## Ablauf überwachtes Lernen (Lab 5.1)

| Befehl | Wirkung |
| --- | --- |
| `X = df[["spalte1", "spalte2"]]` | Merkmale (Features) auswählen |
| `y = df["ziel"]` | Zielgröße auswählen |
| `train_test_split(X, y, test_size=0.2, random_state=42)` | 20 % als Testdaten zurückhalten, jedes Mal gleich aufgeteilt |
| `modell = LogisticRegression(max_iter=1000)` | Modell für Ja/Nein-Fragen (Klassifikation) |
| `modell.fit(X_train, y_train)` | lernen aus den Trainingsdaten |
| `modell.predict(X_test)` | Vorhersage 0/1 für unbekannte Zeilen |
| `modell.predict_proba(X_test)[:, 1]` | Wahrscheinlichkeit für „1“ je Zeile |
| `accuracy_score(y_test, vorhersage)` | Genauigkeit: Anteil richtiger Vorhersagen |
| `y_test.mean()` | Messlatte „alle sind 1“ (Anteil der Einsen) |
| `modell.score(X_train, y_train)` | Genauigkeit auf den Trainingsdaten (Vergleich: Überanpassung?) |
| `confusion_matrix(y_test, vorhersage)` | Fehlerarten: Zeilen = tatsächlich, Spalten = vorhergesagt |

Imports: `from sklearn.linear_model import LogisticRegression`, `from sklearn.model_selection import train_test_split`, `from sklearn.metrics import accuracy_score, confusion_matrix`.

## Clustering (Lab 5.2)

| Befehl | Wirkung |
| --- | --- |
| `StandardScaler().fit_transform(df[spalten])` | jede Spalte auf Mittelwert 0, Standardabweichung 1 |
| `KMeans(n_clusters=4, random_state=42, n_init=10)` | k-Means mit 4 Segmenten, wiederholbar |
| `kmeans.fit_predict(skaliert)` | Segmentnummer je Zeile |
| `kmeans.inertia_` | Abstand innerhalb der Segmente (für das Elbow-Diagramm) |
| `df.groupby("segment").agg(kunden=("kunde_id", "count"), umsatz=("umsatz", "mean"))` | Kennzahlen je Segment |
| `df["segment"].map({1: "Top-Kunden", 2: "Stammkunden"})` | Namen je Nummer zuordnen |
| `px.scatter(df, x=..., y=..., color=df["segment"].astype(str))` | Streudiagramm farbig nach Segment |

Import: `from sklearn.preprocessing import StandardScaler`, `from sklearn.cluster import KMeans`.

## Auffälligkeiten (Lab 5.3)

| Befehl | Wirkung |
| --- | --- |
| `df.groupby(["datum", "region"], as_index=False)["umsatz"].sum()` | Tagesumsatz je Region |
| `df.groupby(["region", "monat"])["umsatz"].transform("mean")` | Gruppenmittel in jede Zeile schreiben |
| `….transform("std")` | Standardabweichung der Gruppe in jede Zeile |
| `(df["umsatz"] - df["mittel"]) / df["streuung"]` | Abstand in Standardabweichungen |
| `df["abstand"].abs() > schwelle` | auffällig nach oben und unten |
| `fig.add_scatter(x=..., y=..., mode="markers")` | Punkte (z. B. rote Kreise) über ein Diagramm legen |

| Schwelle | Nordwind 2024–2026 | Faustregel |
| ---: | ---: | --- |
| 2 | 114 Tage | viele Fehlalarme |
| 3 | 11 Tage | Standard |
| 4 | 2 Tage | nur sehr große Abweichungen |

## Prognose (Lab 6.1)

| Befehl / Formel | Wirkung |
| --- | --- |
| `df.groupby("monat")["umsatz"].sum()` | Monatsumsatz als Series (Index „JJJJ-MM“) |
| `str(int(monat[:4]) - 1) + monat[4:]` | Vorjahresmonat: „2026-10“ → „2025-10“ |
| naiv = `umsatz[vorjahresmonat(monat)]` | Prognose = Vorjahresmonat |
| `bekannt = umsatz[umsatz.index <= stand]` | nur Monate bis einschließlich Stand |
| `bekannt.iloc[-12:].sum() / bekannt.iloc[-24:-12].sum()` | Trendfaktor (letzte 12 Monate / 12 davor) |
| einfach = Vorjahresmonat × Trendfaktor | Saison + aktuelles Wachstum, braucht 24 Monate |
| `(prognose / ist - 1) * 100` | Fehler in % je Monat |
| `fehler.abs().mean()` | MAPE: „im Schnitt x % daneben“ |

Backtest: so tun, als wäre der Stand früher (z. B. 2026-03), Monate mit bekanntem Ist prognostizieren, MAPE vergleichen. Nordwind April–September 2026: naiv 7,7 %, einfach 4,8 %.

## Bericht v2 im Terminal (Lab 6.2)

| Befehl | Wirkung |
| --- | --- |
| `python <pfad>/monatsbericht.py --help` | Befehle anzeigen |
| `… bericht --daten data --monat 2026-09` | HTML-Bericht in `berichte/` |
| `… bericht --daten data --monat 2026-09 --excel` | zusätzlich `kpi_2026_09.xlsx` |
| `… auffaelligkeiten --daten data --monat 2026-09 --schwelle 2` | auffällige Tage mit anderer Schwelle |
| `… prognose --daten data --monat 2026-09` | Prognose der drei Folgemonate |
| `kpi.to_excel(pfad, sheet_name="Kennzahlen")` | Tabelle als Excel-Blatt |
| `with pd.ExcelWriter(pfad) as writer: …` | mehrere Blätter in eine Excel-Datei |

## Begriffe in einem Satz

| Begriff | Bedeutung |
| --- | --- |
| überwacht / unüberwacht | mit bzw. ohne bekannte richtige Antwort lernen |
| Merkmal / Zielgröße | Eingabespalte / vorherzusagende Spalte |
| Messlatte | einfachste Vorhersage ohne Modell, die jedes Modell schlagen muss |
| Überanpassung | Modell merkt sich das Training und versagt bei neuen Daten |
| Skalieren | Spalten auf gemeinsamen Maßstab bringen |
| Standardabweichung | typische Abweichung vom Mittelwert |
| Backtest | Prognose für schon bekannte Monate, um die Methode zu messen |
| MAPE | mittlerer absoluter Fehler in Prozent |
