# MARKETINGBERICHT

Im Rahmen des Praxisprojektes „Positionierung mittels LoRaWAN“ beschäftigten sich die Studierende des Masterstudiengangs Data Science & Intelligent Analytics der FH Kufstein Tirol in der Zusammenarbeit mit dem in Innsbruck ansässigen Deep-Tech Startup emergo Technologies GmbH mit der Entwicklung einer Helium API Schnittstelle.

**PROJEKTHINTERGRUND UND AUFTRAGGEBER**

Die Helium Foundation ist eine gemeinnützige Organisation, die sich darauf konzentriert, eine dezentralisierte Infrastruktur für Low-Power Wide-Area-Networking (LPWAN) mit Hilfe von LongFi-Technologie aufzubauen, die auf dem LoRaWAN-Protokoll basiert. Das LoRaWAN Protokoll für drahtlose Netzwerke biwtet eine lange Reichweite bei geringem Stromverbrauch. Es ermöglicht die Übertragung von Daten über große Entfernungen (bis zu 15 km in urbanen Umgebungen und bis zu 30 km in ländlichen Gebieten) bei geringer Latenz und geringen Kosten. Dies macht es ideal für Anwendungen wie Internet of Things (IoT), Smart Cities und die Überwachung von Umweltbedingungen.
Das Unternehmen emergo technologies GmbH aus Innsbruck erstellt B2B-Lösungen als Deep-Tech-Startup und hat bis jetzt in seinem Portfolio Software auf allen Ressourcenebenen, sowie Mechanik und Elektronik. Bei diesem Projekt interessiert sich Unternehmen für die Ausprobung des Netzwerkverkehrs von LoRaWAN und Helium in Bezug auf mögliche Features zur Positionierung und Anbindung. 

**PROJEKTABLAUF**

Im ersten Arbeitspaket beschäftigten sich die Studierenden mit der Entwicklung einer einfachen und benutzerfreundlichen Schnittstelle, die über http-API die Längen- und Breitengraden der Geräten, sowie weitere für die Positionierung erforderlichen Informationen, abrufen kann.
Im nächsten Schritt beschäftige sich ein Teil der Studierendengruppe mit der Vorverarbeitung der Daten und anschließend mit der Modellentwicklung für die Distanzschätzungen. Die Daten wurden sowie über die neuentwickelten Helium Schnittstelle sowie in der Zusammenarbeit mit dem Praxisprojekt des Masterstudiengangs „Smart Products & Solutions“ erhalten und für das Training der Modelle eingesetzt. Zusätzlich zu den Helium Daten verwenden die Modelle auch weitere öffentliche Datenquellen, z.B. Wetterdaten.
Parallel arbeitete die zweite Arbeitsgruppe daran, die Positionierung API auf der Grundlage maschinellen Lernens zu entwickeln. Der Arbeitspaket baute auf den Ergebnissen der ersten zwei Arbeitspaketen auf und erlaubt auf Grundlage der Distanzschätzungen durch Trilateration die Koordinaten des Endgerätes zu bestimmen.

**PROJEKTERGEBNIS**

Als Endprodukt wurden an emergo technologies drei GitHub Repositories übergeben, die das Code und die detaillierte technische Dokumentation dazu enthalten. Weiteres Ausarbeiten der Schnittstellen erfolgt durch das Unternehmen mit der Unterstützung der internationalen Helium Community, das bereits sein Interesse an die Weiterentwicklung des Projektproduktes angedeutet hat.
