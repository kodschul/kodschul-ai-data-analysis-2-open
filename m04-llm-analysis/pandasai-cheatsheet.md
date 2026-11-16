# Cheatsheet: PandasAI, SQL-Lesehilfe und `classify()` (Modul 4)

Stand: PandasAI 3.0.0 mit `pandasai-litellm` 0.0.1, Modell `gpt-4.1-mini`; 11/2026, vor Kursbeginn prüfen. Schlüssel immer aus der Umgebungsvariable `OPENAI_API_KEY`, nie im Code.

## PandasAI einrichten und fragen

| Befehl | Wirkung |
| --- | --- |
| `import pandasai as pai` | PandasAI laden |
| `from pandasai_litellm.litellm import LiteLLM` | Verbindung zum Sprachmodell über LiteLLM |
| `pai.config.set({"llm": LiteLLM(model="gpt-4.1-mini", temperature=0)})` | Modell für alle Fragen einstellen |
| `df = pai.read_csv(datei)` | CSV als PandasAI-Tabelle laden (pandas-Tabelle mit `.chat`) |
| `antwort = df.chat("Frage")` | Frage stellen; jede Frage beginnt ein neues Gespräch |
| `antwort.value` | Ergebnis: Zahl, Text, Tabelle oder Pfad zum Diagramm |
| `antwort.type` | `"number"`, `"string"`, `"dataframe"`, `"chart"` oder `"error"` |
| `antwort.last_code_executed` | der erzeugte und ausgeführte Code |
| `Image(filename=antwort.value)` | Diagramm (PNG in `exports/charts/`) im Notebook zeigen; `from IPython.display import Image` |
| `bool(os.environ.get("OPENAI_API_KEY"))` | prüfen, ob ein Schlüssel gesetzt ist |
| `python check_setup.py --llm` | Verbindung zum Modell im Terminal testen |

## Beschreibungen mitgeben

| Befehl | Wirkung |
| --- | --- |
| `[s.name for s in df.schema.columns]` | Spalten, die PandasAI an das Modell meldet |
| `spalte.description = "…"` | Beschreibung einer Spalte (in einer Schleife über `df.schema.columns`) |
| `df.schema.description = "…"` | Beschreibung der ganzen Tabelle |

An das Modell gehen: Frage, Tabellenname, Zeilen- und Spaltenzahl, Spalten mit Typ und Beschreibung, die ersten 5 Zeilen.

## SQL in drei Zeilen lesen

| SQL | Bedeutung | pandas / Excel |
| --- | --- | --- |
| `SELECT region, SUM(umsatz)` | Spalten und Rechnungen | Spalten wählen, Summe |
| `WHERE monat = '2026-09'` | Zeilen filtern | `df[df["monat"] == "2026-09"]`, Filter |
| `GROUP BY region` | je Gruppe rechnen | `groupby("region")`, Pivot |

| Außerdem | Bedeutung |
| --- | --- |
| `COUNT(*)` / `COUNT(DISTINCT kunde_id)` | Anzahl Zeilen / Anzahl verschiedener Werte |
| `AVG(...)` | Mittelwert – bei Marge und Umsatzsummen meist falsch |
| `SUM(deckungsbeitrag) / SUM(umsatz)` | Marge einer Gruppe, richtig |
| `ORDER BY umsatz DESC LIMIT 3` | absteigend sortieren, erste drei |
| `FROM table_umsatz_features` | die geladene Tabelle |

Drei Lesefragen für jeden erzeugten Code: Welche Datei? Was wird verändert? Was wird ausgegeben?

## `classify()` und Trefferquote

| Befehl | Wirkung |
| --- | --- |
| `classify(text)` | Kommentar einordnen: `{"stimmung": …, "thema": …, "methode": …}` |
| `classify(text, prompt=PROMPT2)` | mit einem anderen Prompt einordnen |
| `[classify(t) for t in kommentare["kommentar"]]` | alle Kommentare einordnen |
| `kommentare.join(pd.DataFrame(ergebnisse, index=kommentare.index))` | Ergebnis als Spalten anhängen |
| `kommentare["methode"].value_counts()` | wie viele per Sprachmodell, wie viele per Stichwortregeln |
| `(gelabelt["thema"] == gelabelt["thema_label"]).mean()` | Trefferquote (0 bis 1) |
| `kommentare["thema"].value_counts()` | Themen zählen |
| `litellm.completion(model=…, messages=[…], temperature=0, response_format={"type": "json_object"})` | ein Aufruf an das Sprachmodell, Antwort als JSON |
| `json.loads(text)` | JSON-Text in ein Python-Dictionary umwandeln |

| Prompt-Baustein | Beispiel |
| --- | --- |
| Rolle und Kontext | „Ordne einen Kundenkommentar eines Großhändlers … ein." |
| Format | „Antworte nur mit JSON in dieser Form: {"stimmung": "...", "thema": "..."}" |
| erlaubte Werte | „thema: genau einer der Werte Lieferung, Preis, Qualität, Onlineshop, Service" |
| Zusatzregel | „Bei Wartezeit, auch mit ‚endlich', ist die Stimmung negativ." |

## Wann was

| Frage | Weg |
| --- | --- |
| einmalige Frage | Chat oder PandasAI, Code lesen, Gegenprobe |
| Zahl für einen Bericht | Skript, geprüft mit `check_zahlen.py` |
| Freitext einordnen | `classify()`, Trefferquote an gelabelter Stichprobe |
| kein Dienst verfügbar | pandas-Rechnung bzw. Stichwortregeln, klar als solche benannt |
