# Editor (Waise: implementiert und getestet, aber nicht als Anforderung)

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
