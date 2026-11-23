# Keine Waypoint-Dauerschleife

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

