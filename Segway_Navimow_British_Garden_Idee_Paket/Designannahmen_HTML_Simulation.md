# Implementierte Designannahmen der HTML-Simulation

**Basis:** Quellcode-Analyse von `Version_korrigiert_1_4_1_british_recovery.html` (239 Zeilen, JavaScript ab Zeile 107).
**Stand:** 23.11.2025 · Quelle jeder Angabe: Datei + Zeilennummer im HTML-Quelltext.

---

## A. Welt- und Zeitmodell

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| A1 | Die Welt ist ein 2D-Canvas ohne Physik: Bewegung = Positionsverschiebung in Blickrichtung, keine Trägheit, keine Beschleunigung, kein Wendekreis. | Z. 142 (`updatePhysics`), Z. 193 (`steer`) | Fahrverhalten eines echten Mähers (Schleppergeometrie, Drehradius) ist nicht nachgebildet. |
| A2 | Simulationszeit = Bildwiederholrate: 1 Animation-Frame = 1 Simulationsschritt; keine Zeitskalierung (`dt`). | Z. 141 (`animate`, `requestAnimationFrame`) | Ergebnisse (z. B. Recovery-Zähler) sind framerate-abhängig; auf einem 144-Hz-Monitor läuft alles schneller. |
| A3 | Umrechnung Pixel → Quadratmeter über eine feste Konstante (0,0035 m² pro px²), unabhängig von Fenstergröße und DPI. | Z. 108 (`M2_PER_PX2`), Z. 127 | Die Rasenfläche wächst mit dem Fenster, der m²-Wert darüber mit; „m²"-Angaben sind modellhaft, nicht kalibriert (deckt sich mit „Bekannte Grenzen" der Testanleitung). |
| A4 | GPS-Koordinaten sind Dekoration: fester Anker (52,3676° N, 4,9041° E ≈ Amsterdam), linear +0,00001° pro Pixel Abstand vom Zentrum. | Z. 66 (HTML), Z. 223 (`updateTelemetry`) | Keine Georeferenz, keine Skalenkorrektur; Koordinaten für Export/Konzept ohne kartografische Bedeutung. |

## B. Gartenmodell

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| B1 | Der Rasen ist ein festes 6-Eck-Polygon, dessen Form und Größe sich proportional aus der Bildschirmgröße ableiten (`12 % / 14 %` Rand). | Z. 126 (`initLawnIfNeeded`) | Kein „wirklicher" Garten; Grenzform nur über den Editor veränderbar (6 Punkte maximal). |
| B2 | Hindernisse sind genau zwei Kreise mit fester, vom Rasenrahmen abgeleiteter Lage („Pool", r = 40; „Tree", r = 25) und einem Kollisionspuffer von 12 px. | Z. 126, Z. 207 (`hitObstacle`) | Keine beliebigen No-Go-Zonen; No-Go = Hinderniskreis + Puffer (Legende rot). |
| B3 | Es existiert genau ein Dock, fest an Position `px+25, py+85 %` des Rasens. | Z. 114, 126 (`dock`) | Dockposition nicht nutzerkonfigurierbar. |
| B4 | Flächen der Nazca-Zone werden **nicht** aus der Geometrie gemessen, sondern aus **fest codierten Anteilen pro Form** (Kolibri 22 %, Affe 28 %, Spirale 35 %, Ringe 18 % der Rasenfläche). | Z. 127 (`calculateMetrics`) | Die „m²"-Anzeigen für Layer 1/Layer 2 sind abgeleitet, nicht gemessen; sie ändern sich mit Fenstergröße, aber nicht mit der tatsächlichen gezeichneten Nazca-Geometrie. |

## C. Mährmodell und Coverage

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| C1 | Gemäht = Kreis mit fixem Radius 18 px um die Mäherposition pro Frame; keine variable Schnitthöhe im Normalbetrieb (45 mm). | Z. 108 (`MOW_RADIUS`), Z. 142, Z. 201 (`markMowed`) | Mähdauer/Flächenleistung skaliert nicht mit „Gerätedaten". |
| C2 | Coverage ist zellbasiert: Ein 10 × 10-px-Raster über der Rasenfläche, gemähte Zellen in einem Set; Prozentanzeige = Zellen × 100 px² / Rasenfläche, Deckel bei 100 %. | Z. 108 (`CELL`), Z. 201, Z. 203 (`updateCoverage`) | Deckungsgleich mit „Bekannte Grenzen": Berechnung auf Canvas-Pixelbasis, nur modellhaft. |
| C3 | **Innerhalb der sichtbaren Nazca-Zone wird gemäht, nicht stehen gelassen:** Der Mäher setzt dort nur die simulierte Schnitthöhe auf „High-Grass" (60–100 mm) und markiert die Zellen gelb als „hoch". Die Zellen zählen weiterhin als gemäht. | Z. 142 (`mower.blade=(showNazca&&inNazca(...))?highGrass:45; markMowed(...)`), Z. 201 | ⚠️ Wichtigste Abweichung zur Idee: „Biodiversität: High-Grass-Zonen bleiben stehen" ist im Code nicht als *ungemähte* Zone implementiert. Ausgespart wird die Zone nur in der *British-Planung* (D 1) und in der *Smart-Zielsuche* (D 2); im Random-Modus fährt der Mäher durch die Nazca-Zone und markiert sie als (hoch) gemäht. |
| C4 | Fläche löschen = Coverage-Reset, aber British-Plan wird mitgebaut/neu berechnet; gemähte Karte und Planzustand sind entkoppelt. | Z. 202 (`clearMowedMap`) | Erwartung vermessen: Coverage % läuft unabhängig vom Plan weiter. |

## D. Navigation

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| D1 | British-Planung: Linienschar über die Bounding-Box des Rasens (Richtung = Winkel), Abtastschritt `max(10, Abstand/2)`, Wegpunkte nur wenn: im Rasen, kein Hindernis, Randabstand > 28 px, nicht in Nazca (wenn sichtbar); Segmente < 3 Punkte oder < 45 px verworfen; Zickzack-Fahrt. | Z. 110, Z. 139 (`buildBritishPlan`) | Aussparung ist segmentbasiert (Waypoints in Nazca werden gar nicht erzeugt) – konsistent mit C3: die Zone ist im *Plan* ausgespart, physisch „magisch". |
| D2 | Smart-Navigation = nächstgelegener ungemähter Rasterpunkt (20-px-Raster) mit Strafpunktzahl für Wandnähe (Schwellwert 34 px, Strafe 420 bzw. linear) und für gemiedene Ziele (70-px-Radius, max. 14 Merker). Zielwechsel, wenn Ziel erreicht, gemäht oder weg. | Z. 109 (`WALL_SAFE`), Z. 143 (`applySmart`), Z. 199 (`findNearestUnmowed`) | „Intelligenz" ist ein Gier-Score, keine Pfadplanung (kein A* / Routeplanung); Umwege um Hindernisse entstehen nur durch Blockaden, nicht durch Planung. |
| D3 | Random-Navigation hat kein Ziel: bei blockierter Bewegung Zufallsdrehung um 118°–168°. | Z. 194 (`blockedTurn`) | Referenzverhalten rein stochastisch. |
| D4 | Moduswechsel im Betrieb ist erlaubt: Ziele und Recovery-Zähler werden zurückgesetzt, Mäherposition und gemähte Karte bleiben erhalten. Blindpuffer: In British-Waypoints wird der Index nicht neu positioniert (Plan startet wieder vorn). | Z. 137 (`setNavigationMode`) | Wechsel ist stabil getestet, Hintergrund hier: Uneinheitlicher Verlauf, wenn mitten im Plan gewechselt wird. |
| D5 | Der Editor (6 Eckpunkte ziehen) rechnet Nazca-Geometrie und British-Plan sofort neu und pausiert die Simulation während der Bearbeitung. | Z. 141, Z. 230 (`moveDrag`) | Kennnzeichnung der Waise „Editor": testet, nicht spezifiziert in den Texten. |

## E. Recovery / Anti-Stuck

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| E1 | „Festfahren" heißt im Code: Der Abstand zum Ziel sinkt über mehr als 58 Frames nicht mehr um mindestens 0,45 px. Kollision wird für diesen Mechanismus nicht erkannt. | Z. 110 (`BRITISH_PROGRESS_LIMIT`), Z. 175–190 (`monitorBritishProgress`) | Recovery basiert auf Fortschrittsmessung („Toter-Reckung"), nicht auf Kollisionssensoren. |
| E2 | Escape-Drehung ist randomisiert: +132° bis +192°, danach 42 Frames Kaminspinn-Drehung (+3,4°/Frame), **dann wird der problematische Wegpunkt übersprungen (inkl. +3 in der Reihenfolge)** – kein erneuter Versuch desselben Wegpunkts. | Z. 110 (`BRITISH_ESCAPE_FRAMES`, `BRITISH_HARD_SKIP`), Z. 144–156, 174, 184 | „Der Mower versucht nicht endlos denselben Waypoint anzufahren" ist *garantiert* durch Skip, nicht durchãy Recovery-Erfolg. |
| E3 | Unsafe Waypoints (zu nah am Rand < 21 px [0,75 × 28], Hindernis oder Nazca bei Sichtbarkeit) werden sofort und still übersprungen (+3). | Z. 157–163 | „Kritische Waypoints am Rand werden übersprungen" ist Programm, nicht emergentes Verhalten. |
| E4 | Globaler Anti-Stuck: < 1,4 px Bewegung pro Frame erhöht Zähler; > 55 % des Limits → `Warn`; > 85 → Recovery (Zufallsdrehung +145°–200°, 48 Frames). In British zusätzlich: blockierte Grenze → sofortiger Waypoint-Skip. | Z. 109, Z. 194, 195 | Zwei unabhängige Recovery-Stufen (global Anti-Stuck + British-spezifisch), die in der Testanleitung nicht unterschieden werden. |

## F. Batterie, Dock, Export

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| F1 | Batterie startet bei 84 % und verbraucht linear und modusunabhängig 0,002 % pro Frame; kein Ladeprozess simuliert (Dock = Simulations-Stopp). | Z. 119, Z. 142, Z. 200 (`moveToDock`, `docked` → `sim=false`) | Energiewirtschaft ist Deko; kein Ladezyklus, kein Erschöpfungsproblem. |
| F2 | Auto-Dock bei < 10 % während des Mähens; Dockfahrt mit konstant 2,2 px/Frame über direkte Linie (ohne Umfahrung von Hindernissen). | Z. 142, Z. 200 | Dockanfahrt kann durch Hindernisse laufen (Kollisionscheck wird dort nicht geprüft). |
| F3 | Export = vollständiger Zustands-Snapshot als JSON (inkl. Grenzpolygon, Wegpunkt-Indizes, Randabstand, Recovery-Zähler); Weg=Download oder LocalStorage; **kein Import/Laden**. | Z. 232 (`config`), Z. 234 (`openSaveModal`, `saveLocal`, `downloadJSON`) | Anforderung A9 existiert und ist implementiert, aber ungetestet (siehe Traceability-Diagramm). |

## G. Zusammenarbeit mit der Anforderungs-/Testbasis

| # | Designannahme | Beleg (Datei, Zeile) | Implikation |
|---|---|---|---|
| G1 | Antworten auf „Umschaltung" und „Anzeige-Details" (Smart-Ziel blau, gestrichelte Bahnen, Fortschritt `n/total`) sind im Code vorhanden – die in der Traceability als Waisen markierten visuellen Detail tests sind also **implementierte, aber undokumentierte Anforderungen**. | Z. 219 (`drawSmart`), Z. 214 (`drawBritish`), Z. 141 (`updateBritishMetric`) | Empfehlung: Rails nachziehen (in die Idea/Anforderungsliste aufnehmen), damit die Waisen zu geprüften Anforderungen werden. |
| G2 | Der Editor (Fläche bearbeiten) ist eine **implementierte, dokumentierte (in der Testanleitung), aber im Ideendokument nicht geforderte** Funktion. | Z. 227–230 | Umgekehrter Fall: dokumentierter Test ohne Anforderung. |

---

## Zusammenfassung: die sechs wichtigsten Annahmen

1. **Nichts ist physikalisch** – Punktmasse ohne Trägheit, framerate-abhängige Zeit (A1, A2).
2. **Alle „m²"/Koordinaten sind modellhaft** – fixe Pixel-Umrechnung, festes Flächenverhältnis pro Nazca-Form, Deko-GPS (A3, A4, B4).
3. **Die Nazca-Zone wird nicht wirklich ungemäht gelassen** – sie wird nur aus den British-Wegpunkten (und Smart-Zielen) ausgeschlossen; im Random-Modus wird durch sie hindurch gemäht (gelb markiert) (C3, D1, D2). ⚠️ Direkte mower-Lücke zum Biodiversitäts-Ziel.
4. **Recovery ist deterministische Programmlogik**, kein Sensorverhalten: Skip ist garantiert, Escape ist eine Zufallsdrehung mit Progress-Trigger (E1–E3).
5. **„Smart" ist ein Score, kein Planer** (D2).
6. **Energie und Dock sind Deko** – linearer Verbrauch, kein Laden, Dockanfahrt ohne Hindernisprüfung (F1, F2).
