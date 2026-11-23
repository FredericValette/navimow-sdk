# Editor (Waise: implementiert und getestet, aber nicht als Anforderung)

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass das Ziehen der Rasen-Eckpunkte im Editor den British-Plan sofort neu berechnet,
damit ich Rand- und Eckverhalten für beliebig geformte Flächen testen kann.
*(Traceability-Waise: Editor wird getestet (T7), existiert aber im Anforderungsdokument nicht – Anforderung sollte als „implementierte, undokumentierte Anforderung" ergänzt werden, vgl. G1/G2.)*

**Akzeptanzkriterien:**
- Editor-Modus pausiert die Simulation während der Bearbeitung (Designannahme D5).
- Nach dem Loselassen eines Eckpunkts ist der neu berechnete Plan sofort sichtbar.
- Spitzwinklige Flächen (spitze Ecken, L-Formen) lösen kein Plan-Versagen aus; Recovery greift bei Corner-Locks.

---
