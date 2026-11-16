"""Lab 1.1 – KI-Landkarte: drei Aufgabentypen an den Nordwind-Daten.

Aufruf im Kursordner (Terminal in VS Code):
    python project/examples/m01-ai-analysis-basics/l01-ai-landscape/ki_landkarte.py --region Nord

Das Skript liest data/nordwind_umsatz.csv, bereitet die Daten kurz auf und zeigt
für eine Region drei Diagramme in einer HTML-Datei:
  1. Prognose:       Umsatz der nächsten drei Monate (Vorjahresmonat × Trendfaktor)
  2. Clustering:     Kunden in vier Segmenten (k-Means)
  3. Anomalien:      auffällige Tage (mehr als 3 Standardabweichungen vom Mittel)
Die Datei landet in project/playground/ und öffnet sich im Browser.
Alle Bausteine erklärt der Kurs später Schritt für Schritt (Modul 2, 5 und 6).
"""

import argparse
import webbrowser
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

EINGABE = "data/nordwind_umsatz.csv"
ORDNER = "project/playground/"
REGIONEN = ["Nord", "Süd", "West", "Ost"]
FARBEN = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]   # Segment 1–4
SYMBOLE = ["circle", "diamond", "square", "triangle-up"]


def aufbereiten(df):
    """Kurzfassung der Bereinigung aus Lab 2.2: Dubletten, Datum, Regionsnamen."""
    df = df.drop_duplicates().copy()
    deutsch = pd.to_datetime(df["datum"], format="%d.%m.%Y", errors="coerce")
    iso = pd.to_datetime(df["datum"], format="%Y-%m-%d", errors="coerce")
    df["datum"] = deutsch.fillna(iso)
    df["region"] = (df["region"].str.strip().str.replace("Region ", "", regex=False)
                    .str.capitalize().replace({"Sued": "Süd"}))
    return df


def prognose(df, region):
    """Monatsumsatz der Region plus Prognose für drei Monate (Lab 6.1)."""
    monat = df[df["region"] == region].set_index("datum")["umsatz"].resample("MS").sum()
    letzte_12 = monat.iloc[-12:].sum()
    davor_12 = monat.iloc[-24:-12].sum()
    trend = letzte_12 / davor_12                       # z. B. 1.05 = 5 % Wachstum
    zukunft = pd.date_range(monat.index[-1] + pd.offsets.MonthBegin(), periods=3, freq="MS")
    werte = [monat[t - pd.DateOffset(years=1)] * trend for t in zukunft]

    fig = go.Figure()
    fig.add_scatter(x=monat.index, y=monat.values, name="Ist", mode="lines+markers",
                    line=dict(color="#2a78d6", width=2), marker=dict(size=6))
    fig.add_scatter(x=[monat.index[-1], *zukunft], y=[monat.iloc[-1], *werte], name="Prognose",
                    mode="lines+markers", line=dict(color="#eb6834", width=2, dash="dash"),
                    marker=dict(size=8))
    fig.update_layout(title=f"1 · Prognose: Monatsumsatz {region} (Trendfaktor {trend:.3f})",
                      yaxis_title="Umsatz in €", xaxis_title=None, hovermode="x unified")
    return fig, trend, dict(zip(zukunft.strftime("%Y-%m"), werte))


def segmente(df, region):
    """Kunden nach Häufigkeit und Umsatz in vier Segmente teilen (Lab 5.2)."""
    stichtag = df["datum"].max()
    rfm = df.groupby("kunde_id").agg(
        letzter_kauf=("datum", "max"), haeufigkeit=("beleg_nr", "count"),
        umsatz=("umsatz", "sum"), region=("region", lambda r: r.mode()[0]))
    rfm["tage_seit_kauf"] = (stichtag - rfm["letzter_kauf"]).dt.days
    merkmale = StandardScaler().fit_transform(rfm[["tage_seit_kauf", "haeufigkeit", "umsatz"]])
    rfm["cluster"] = KMeans(n_clusters=4, n_init=10, random_state=42).fit_predict(merkmale)
    # Segment 1 = höchster Durchschnittsumsatz, Segment 4 = niedrigster
    rang = rfm.groupby("cluster")["umsatz"].mean().rank(ascending=False).astype(int)
    rfm["segment"] = "Segment " + rfm["cluster"].map(rang).astype(str)

    teil = rfm[rfm["region"] == region].reset_index().sort_values("segment")
    fig = px.scatter(teil, x="haeufigkeit", y="umsatz", color="segment", symbol="segment",
                     hover_name="kunde_id", color_discrete_sequence=FARBEN, symbol_sequence=SYMBOLE,
                     category_orders={"segment": [f"Segment {i}" for i in range(1, 5)]},
                     labels={"haeufigkeit": "Buchungen seit 01/2024", "umsatz": "Umsatz in €",
                             "segment": "Segment"})
    fig.update_traces(marker=dict(size=9, line=dict(width=1, color="white")))
    fig.update_layout(title=f"2 · Clustering: {len(teil)} Kunden der Region {region} in vier Segmenten")
    return fig, teil["segment"].value_counts().sort_index()


def auffaellige_tage(df, region, schwelle=3):
    """Tagesumsätze, die mehr als `schwelle` Standardabweichungen vom Mittel abweichen (Lab 5.3)."""
    tage = df.groupby(["region", "datum"], as_index=False)["umsatz"].sum()
    tage["monat"] = tage["datum"].dt.strftime("%Y-%m")
    gruppe = tage.groupby(["region", "monat"])["umsatz"]       # Mittel und Streuung je Region und Monat
    tage["abstand"] = (tage["umsatz"] - gruppe.transform("mean")) / gruppe.transform("std")
    tage = tage[tage["region"] == region]
    treffer = tage[tage["abstand"].abs() > schwelle]

    fig = go.Figure()
    fig.add_scatter(x=tage["datum"], y=tage["umsatz"], name="Tagesumsatz", mode="lines",
                    line=dict(color="#2a78d6", width=1))
    fig.add_scatter(x=treffer["datum"], y=treffer["umsatz"], name="auffällig", mode="markers",
                    marker=dict(color="#e34948", size=11, symbol="circle-open", line=dict(width=3)))
    fig.update_layout(title=f"3 · Anomalien: {len(treffer)} auffällige Tage in {region} "
                            f"(mehr als {schwelle} Standardabweichungen)",
                      yaxis_title="Umsatz in €", xaxis_title=None)
    return fig, treffer


def main():
    parser = argparse.ArgumentParser(description="Drei KI-Aufgabentypen an den Nordwind-Daten zeigen.")
    parser.add_argument("--region", default="Nord", choices=REGIONEN, help="Region, Standard: Nord")
    args = parser.parse_args()

    df = aufbereiten(pd.read_csv(EINGABE))
    fig1, trend, werte = prognose(df, args.region)
    fig2, anzahl = segmente(df, args.region)
    fig3, treffer = auffaellige_tage(df, args.region)

    print(f"Region: {args.region}")
    print(f"1 Prognose   Trendfaktor {trend:.3f}; " +
          ", ".join(f"{m}: {w:,.0f} €".replace(",", ".") for m, w in werte.items()))
    print("2 Segmente   " + ", ".join(f"{s}: {n} Kunden" for s, n in anzahl.items()))
    print(f"3 Anomalien  {len(treffer)} auffällige(r) Tag(e): " +
          ", ".join(treffer["datum"].dt.strftime("%d.%m.%Y")))

    for fig in (fig1, fig2, fig3):
        fig.update_layout(template="plotly_white", height=420, margin=dict(t=60, l=60, r=20, b=40))
    teile = [fig.to_html(full_html=False, include_plotlyjs=(i == 0)) for i, fig in enumerate((fig1, fig2, fig3))]
    html = (f"<html><head><meta charset='utf-8'><title>KI-Landkarte {args.region}</title></head>"
            f"<body style='font-family:sans-serif;max-width:1000px;margin:auto'>"
            f"<h1>Nordwind Handel – drei KI-Aufgaben für die Region {args.region}</h1>"
            + "".join(teile) + "</body></html>")
    datei = Path(ORDNER) / "ki_landkarte.html"
    datei.write_text(html, encoding="utf-8")
    print("Gespeichert:", datei)
    webbrowser.open(datei.resolve().as_uri())


if __name__ == "__main__":
    main()
