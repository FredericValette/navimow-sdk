# Tester-Tickets – British Garden Mode (A1–A12)

Format: „Als Tester im Segway British-Garden-Prototyp möchte ich …, damit …" mit messbaren Akzeptanzkriterien.
Basis: `Segway_Idee_British_Garden_Nazca_Navimow.md` (Anforderungen A1–A12), `Traceability_Diagramm_British_Garden.md` (Testabdeckung), `Designannahmen_HTML_Simulation.md` (bekannte Lücken C3, D1, E1–E4, F3).

---

## Ticket A1 – Umschaltbare Navigation

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass ich jederzeit zwischen den Navigationsarten Random, Smart und British Garden umschalten kann,
damit ich die Modi unter identischen Bedingungen vergleichbar testen kann.

**Akzeptanzkriterien:**
- Alle drei Modi sind über Bedienelemente (Button „Random" / „Smart" / „British Garden") während des laufenden Betriebs umschaltbar.
- Ein Moduswechsel verursacht keine JavaScript-Fehler und keinen Neustart der Simulation.
- Nach dem Wechsel setzt der neue Modus ohne manuellen Reset mit der Mahd fort (Position und gemähte Karte bleiben erhalten).
- Der aktive Modus ist in der Oberfläche eindeutig erkennbar (z. B. aktiver Button hervorgehoben).
- Moduswechsel im laufenden British-Plan (mitten im Plan) führen zu definiertem Verhalten: British-Recovery-Zähler werden zurückgesetzt und der Plan startet wieder vorn (Designannahme D4).

---

## Ticket A2 – Parallele Linien

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass der Mäher im British-Garden-Modus in sauberen, parallelen Bahnen fährt und die Bahnen sichtbar angezeigt werden,
damit das gewünschte gepflegte Streifenbild entsteht und ich die Linienführung prüfen kann.

**Akzeptanzkriterien:**
- Nach Aktivierung von British Garden werden blaue, gestrichelte, parallele Bahnen angezeigt (Test 4).
- Der Mäher folgt den Bahnen in Zickzack-Fahrt ohne eigenständige Zufallsbewegung.
- Die Fortschrittsanzeige „British" zeigt z. B. `1/40` und erhöht sich mit bearbeiteten Segmenten.
- Kein Bahnen-Segment liegt außerhalb des Rasenpolygons.

---

## Ticket A3 – Linienwinkel einstellbar

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass ich den British-Linienwinkel einstellen kann (getestet: 0°, 45°, 90°, 135°),
damit saisonale diagonale Muster möglich sind und ich Rand-/Corner-Verhalten aller Winkel prüfen kann.

**Akzeptanzkriterien:**
- Geänderter Winkel führt zu sofortigem Neuaufbau des Linienplans mit korrekter Ausrichtung.
- Für jeden getesteten Winkel (0°, 45°, 90°, 135°) verlaufen die Bahnen tatsächlich parallel in dieser Richtung (messbar prüfbar, nicht nur Augenschein).
- Winkel 135° (Stress-Test, Testmatrix Zeile F, bisher Erwartungsspalte leer) erhält ein definiertes erwartetes Verhalten inkl. Recovery-Antwort.
- Pro Winkel und Randbereich höchstens eine British-Recovery-Auslösung ohne Festfahren im Endzustand.

---

## Ticket A4 – Linienabstand einstellbar

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass ich den British-Linienabstand einstellen kann,
damit Überlappungen oder ungemähte Lücken zwischen den Bahnen messbar ausgeschlossen werden können.

**Akzeptanzkriterien:**
- Geänderter Abstand führt zu sofortigem Neuaufbau des Linienplans mit korrektem Bahnenversatz.
- Der tatsächliche Versatz der angezeigten Bahnen entspricht dem eingestellten Abstand (bislang nur Abstand 34 px getestet – Abdeckung „unklar", Designannahme D1: Abtastschritt = `max(10, Abstand/2)`).
- Bei jedem getesteten Abstand bleibt die gesamt gemähte Fläche ohne dauerhafte Streifenlücken (Restlücken nur an Nazca-Zone und Hindernis-Puffer).

---

## Ticket A5 – Nazca-Zone optional

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die Nazca-Linie als High-Grass-Zone optional ein- und ausschaltbar bleibt,
damit ich sowohl mit als auch ohne Zonenausschluss testen kann.

**Akzeptanzkriterien:**
- Die Zone ist per Schalter aktivier-/deaktivierbar ohne Neustart der Simulation.
- Bei sichtbarer Zone wird die Zone gelb angezeigt; bei nicht sichtbarer Zone verschwindet die Aussparung aus dem British-Plan (Variante A/B von Test 6).
- Ein- und Ausschalten löst jeweils eine Neuberechnung des British-Plans aus.

---

## Ticket A6 – Aussparung bei der Linienplanung + Sicherheitsabstand am Zonenrand

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die Nazca-Zone (High-Grass-Bereich) im British-Modus
nicht gemäht wird und der Mäher am Rand mit Sicherheitsabstand
um die Zone herumläuft,
damit das Gras in der Zone stehen bleibt und kein Geräteschaden entsteht.

**Akzeptanzkriterien:**
- British-Linienplan schließt Nazca-Zone aus (Zonenausschluss).
- Sicherheitsabstand am Zonenrand einhaltbar.
- Recovery/Corner-Escape darf nicht in die Zone führen.
- Coverage-Zähler zählt Zone nicht als gemäht.

---

## Ticket A7 – British Recovery / Anti-Stuck-Logik

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass British Recovery bei Rand- und Corner-Locks die kritischen Waypoints überspringt,
damit der Mäher nicht festgefahren bleibt und den Plan zuverlässig fertig fährt.

**Akzeptanzkriterien:**
- Bei blockierter Bewegung springt die Anzeige „British Recovery" von `OK` auf `Skip n` bzw. `Escape n` (Test 5, n mit fortlaufender Nummer).
- Der Mäher wiederholt niemals denselben Waypoint endlos: Skip überspringt den Waypoint inkl. Folge-Waypoints (Designannahme E2/E3, Skip +3).
- Waypoints mit Randabstand < Sicherheitsgrenze werden präventiv übersprungen (Designannahme E3: < 21 px).
- Skip- und Escape-Zähler sind im Activity Log nachvollziehbar.

---

## Ticket A8 – Coverage dauerhaft sichtbar

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die bereits gemähte Fläche dauerhaft und lückenlos sichtbar bleibt,
damit ich die Abdeckung über die gesamte Session prüfen kann.

**Akzeptanzkriterien:**
- Bereits gemähte Zellen bleiben sichtbar, bis „Fläche löschen" aktiviert wird (Designannahme C2: 10 × 10-px-Raster über Rasen).
- Die Coverage-Prozentanzeige berechnet sich aus gemähten Zellen / Rasenfläche und liegt nie über 100 %.
- „Fläche löschen" resettet Coverage, während der British-Plan erhalten bleibt (Designannahme C4) – Verhalten dokumentiert und reproduzierbar.
- Neuberechnung des Plans im Editor verfälscht bereits dargestellte Coverage-Markierungen nicht.

---

## Ticket A9 – JSON-Export der Konfiguration

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die vollständige Konfiguration als JSON exportierbar ist und der Inhalt geprüft werden kann,
damit ich die getestete Konfiguration reproduzierbar dokumentieren kann.
*(Risikoaussage 1 aus dem Traceability-Diagramm: Export implementiert (F3), aber von keinem Testfall abgedeckt.)*

**Akzeptanzkriterien:**
- Export erzeugt ein vollständiges JSON mit: Grenzpolygon, Winkel-/Abstandseinstellungen, Wegpunkt-Indizes, Randabstand, Recovery-Zähler (Designannahme F3).
- Export per Download und LocalStorage funktioniert ohne JavaScript-Fehler.
- Das exportierte JSON ist zugleich eine ausreichende Beschreibung der Testkonfiguration (Session mit unterschiedlicher Konfiguration → unterschiedliche JSON-Inhalte).
- Exporthandling ist in einer Testanleitung Schritt für Schritt beschrieben (Lücke schließen).

---

## Ticket A10 – Smart-Navigation zieldirekt

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die Smart-Navigation verlässlich Ziele in ungemähten Bereichen setzt und Wand-/Hindernisnähe meidet,
damit ich die Stärke von Smart gegen Random messbar belegen kann.
*(Risikoaussage 3: „bedient, nicht verifiziert" – Smart-Zielsuche ohne Metrik.)*

**Akzeptanzkriterien:**
- Smart-Ziel erscheint blau und liegt immer in einem ungemähten Bereich (Test 3).
- Ziele in Wandnähe (Schwellwert 34 px, Designannahme D2) und in gemiedenen Zonen (70-px-Radius, z. B. Nazca bei Sichtbarkeit) werden nicht ausgewählt.
- Zielwechsel nur bei: Ziel erreicht, Ziel gemäht oder Weg entfallen.
- Vergleichsmetrik definiert und gemessen (z. B. Zeit bis X % Coverage: Smart vs. Random/Durchschnitt) – Verbesserung zahlenmäßig belegt.

---

## Ticket A11 – Keine Waypoint-Dauerschleife

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass Recovery-Logik garantiert nicht endlos denselben Waypoint anfährt,
damit ich die Stabilität einer langen Session prüfen kann.
*(Traceability-Status A11: „teilweise" – bislang kein Zeit- oder Zählerkriterium.)*

**Akzeptanzkriterien:**
- Kein Waypoint wird in einer Session unmittelbar nacheinander erneut angefahren (Skip greift, Designannahme E2).
- Recovery wird durch ein messbares Progress-Kriterium ausgelöst (Designannahme E1, im Ticket dokumentiert statt nur beobachtet).
- Langläufer-Test: keine festhängende Dauerschleife im Verlauf von X Minuten / Y Recovery-Ereignissen.
- Testmatrix-Zeile F (135°) läuft ohne Dauerschleife durch.

---

## Ticket A12 – High-Grass-Zone bleibt ungemäht

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die Nazca/High-Grass-Zone physisch nicht gemäht wird und der Coverage-Zähler sie nicht als gemäht zählt,
damit ich das Biodiversitätsversprechen „High-Grass bleibt stehen" belegen kann.
*(Traceability-Status A12: „unklar" – Designannahme C3: aktuell wird in der Zone mit höherer Schnitthöhe gemäht und als gemäht gezählt = kritische Lücke zum Kernversprechen.)*

**Akzeptanzkriterien:**
- Nach vollständigem British-Lauf ist kein Bereich der Nazca-Zone als gemäht markiert (Zellprüfung statt Augenschein).
- Random-Modus: der bekannte Konflikt aus Designannahme C3 (Random mäht durch die Zone und markiert sie gelb als „hoch") ist in der Anforderung explizit festgelegt und per Testfall abgedeckt.
- Coverage-Zähler inkludiert die Nazca-Fläche nicht in der Prozentangabe der gemähten Fläche.
- Activity-Log hält jeden Versuch des Mähers fest, die Zone zu betreten (inkl. Recovery-Escape, der sonst in die Zone führen könnte).

---

## Ergänzungsticket E01 – Editor (Waise: implementiert und getestet, aber nicht als Anforderung)

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass das Ziehen der Rasen-Eckpunkte im Editor den British-Plan sofort neu berechnet,
damit ich Rand- und Eckverhalten für beliebig geformte Flächen testen kann.
*(Traceability-Waise: Editor wird getestet (T7), existiert aber im Anforderungsdokument nicht – Anforderung sollte als „implementierte, undokumentierte Anforderung" ergänzt werden, vgl. G1/G2.)*

**Akzeptanzkriterien:**
- Editor-Modus pausiert die Simulation während der Bearbeitung (Designannahme D5).
- Nach dem Loselassen eines Eckpunkts ist der neu berechnete Plan sofort sichtbar.
- Traförmige Flächen (spitze Ecken, L-Formen) lösen kein Plan-Versagen aus; Recovery greift bei Corner-Locks.

---

## Matrix: Ticket ↔ Risikoausage aus dem Traceability-Diagramm

| Risikoaussage | Abgedeckt durch Ticket |
|---|---|
| 1. JSON-Export ungetestet | A9 |
| 2. Biodiversität/„High-Grass bleibt stehen" ungeschützt | A6, A12 (kritisches Ticket) |
| 3. Winkel/Abstand/Smart „bedient, nicht verifiziert" | A3, A4, A10 (messbare Kriterien ergänzt) |
| Waypoint-Dauerschleife ohne Kriterium | A11 |
| Waise Editor | E01 |
