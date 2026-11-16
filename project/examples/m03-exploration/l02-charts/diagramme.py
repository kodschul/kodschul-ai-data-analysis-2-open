"""Lab 3.2 – drei Diagramme mit Aussage als Funktionen.

Aufruf im Kursordner:  python project/examples/m03-exploration/l02-charts/diagramme.py
Liest die Ergebnistabellen aus dem Beispiel von Lab 3.1 und speichert drei
interaktive Diagramme als HTML in ORDNER. Dieselben Funktionen stehen in Lab 3.3
in monatsbericht.py; dort entsteht der Titel (der Befund) jeden Monat aus den Zahlen.
"""

import pandas as pd
import plotly.express as px

QUELLE = "project/examples/m03-exploration/l01-eda/"
ORDNER = "project/examples/m03-exploration/l02-charts/"


def diagramm_kanal(kanal_monat, titel):
    """Verlauf: Umsatz je Monat, eine Linie je Kanal."""
    return px.line(
        kanal_monat, x="monat", y=["Außendienst", "Onlineshop"], title=titel,
        labels={"monat": "Monat", "value": "Umsatz in €", "variable": "Kanal"},
    )


def diagramm_marge(marge, titel):
    """Vergleich: Marge je Produktgruppe als Balken, höchste zuerst."""
    return px.bar(
        marge, x="produktgruppe", y="marge_prozent", title=titel, text="marge_prozent",
        labels={"produktgruppe": "Produktgruppe", "marge_prozent": "Marge in %"},
    )


def diagramm_wachstum(wachstum, titel):
    """Abweichung: Veränderung zum Vorjahr je Region in %."""
    return px.bar(
        wachstum, x="region", y="wachstum_prozent", title=titel, text="wachstum_prozent",
        labels={"region": "Region", "wachstum_prozent": "Veränderung zum Vorjahr in %"},
    )


if __name__ == "__main__":
    kanal_monat = pd.read_csv(QUELLE + "kanal_monat.csv")
    marge = pd.read_csv(QUELLE + "marge_produktgruppe.csv")
    wachstum = pd.read_csv(QUELLE + "wachstum_region.csv")

    diagramme = {
        "diagramm_kanal.html": diagramm_kanal(
            kanal_monat, "Seit dem Relaunch im März 2026 wächst der Onlineshop, der Außendienst bleibt flach"),
        "diagramm_marge.html": diagramm_marge(
            marge, "Schreibwaren mit der höchsten Marge (34,8 %), Technik mit der niedrigsten (14,2 %)"),
        "diagramm_wachstum.html": diagramm_wachstum(
            wachstum, "West, Süd und Ost wachsen um 9 bis 10 %, Nord nur um 4,3 % (Jan.–Sep. 2026 zum Vorjahr)"),
    }
    for datei, fig in diagramme.items():
        fig.write_html(ORDNER + datei, include_plotlyjs="cdn")   # "cdn": kleine Datei, plotly kommt aus dem Netz
        print("Gespeichert:", ORDNER + datei)
