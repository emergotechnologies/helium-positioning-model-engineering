## Abstimmung Fabio - Fabian zur Klärung des Projektauftrags
*18.10.2022*

## Reflektion des Projektauftrags
Zum Abgleich des Verständnisses des Projektauftrags wurde dieser "zurückgespiegelt".

1. Helium Gateways/Hotspot (Positionen bekannt)
2. Sendegerät (Position unbekannt)
3. Sendegerät verbindet sich Gateways
4. Sendegerät erhält Empfangsstärke
5. Modell zur Umrechnung der Empfangsstärke in Distanzmaß (Meter)
6. Math. Triangulation

Die Position der Helium Gateways lässt sich über deren ID am entsprechenden API Endpoint abfragen.

## Vorgehen
Da kein "Sendegerät" zur Verfügung steht, sollen erste Daten (auch Trainingsdaten) über die Helium API erhoben werden.
Dazu werden Challenges eines Hotspots abgefragt, indenen dieser als Challengee auftritt.

1. Signalstärkster Witness = Location des Hotspots --> Baseline RSME o.ä. als Benchmark.
2. Schätzung der Distanz basierend auf Signalstärke. Die Position bzw. Distanz zwischen einem oder mehreren Witnesses und dem Hotspot ist bekannt

## Command Line Interface
Einfache Befehlseingabe mit Parametern zum Laden eines Datensatzes.

generate dataset
- sample size
- export format
- flag: nearest witness/highest rssi or 3 or more witnesses (Tri- or Multilat)
- path

Beispiel:
```
python load_helium_data.py -samples 1000 -format csv -mode trilateral -path ./data
```

Anschließend wird über mehrere Abfragen der API ein Datensatz erstellt, der zu 1000 Hotspots die 3 signalstärksten Witnesses lädt und die diese als csv unter ./data abspeichert.

## REST API
Selbe Anforderungen wie an Command Line Interface aber 2. rangig.

## Testdaten
Die Testdaten der Smart Products Gruppe orientieren sich an folgendem Format
![sample_dataframe](uploads/40efd98ea40bc9f8078b8c0bc7629b97/sample_dataframe.png)
*Kann final abweichen*

Jeder Datensatz ist die Signalmessung eines Hotspots. *y_lat* und *y_lon* sind zu ermitteln. *x_lat* und *x_lon* sind die bekannten Positionen der Hotspots.

## Dokumentation
Sprache: Englisch
Docstrings: einheitlich nach Format (Vorschlag: [PEP 257](https://peps.python.org/pep-0257/)
