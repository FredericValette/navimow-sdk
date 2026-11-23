# JSON-Export der Konfiguration

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

