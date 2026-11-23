# Umschaltbare Navigation

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

