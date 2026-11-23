# Linienabstand einstellbar

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass ich den British-Linienabstand einstellen kann,
damit Überlappungen oder ungemähte Lücken zwischen den Bahnen messbar ausgeschlossen werden können.

**Akzeptanzkriterien:**
- Geänderter Abstand führt zu sofortigem Neuaufbau des Linienplans mit korrektem Bahnenversatz.
- Der tatsächliche Versatz der angezeigten Bahnen entspricht dem eingestellten Abstand (bislang nur Abstand 34 px getestet – Abdeckung „unklar", Designannahme D1: Abtastschritt = `max(10, Abstand/2)`).
- Bei jedem getesteten Abstand bleibt die gesamt gemähte Fläche ohne dauerhafte Streifenlücken (Restlücken nur an Nazca-Zone und Hindernis-Puffer).

---

