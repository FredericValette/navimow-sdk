# Linienwinkel einstellbar

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass ich den British-Linienwinkel einstellen kann (getestet: 0°, 45°, 90°, 135°),
damit saisonale diagonale Muster möglich sind und ich Rand-/Corner-Verhalten aller Winkel prüfen kann.

**Akzeptanzkriterien:**
- Geänderter Winkel führt zu sofortigem Neuaufbau des Linienplans mit korrekter Ausrichtung.
- Für jeden getesteten Winkel (0°, 45°, 90°, 135°) verlaufen die Bahnen tatsächlich parallel in dieser Richtung (messbar prüfbar, nicht nur Augenschein).
- Winkel 135° (Stress-Test, Testmatrix Zeile F, bisher Erwartungsspalte leer) erhält ein definiertes erwartetes Verhalten inkl. Recovery-Antwort.
- Pro Winkel und Randbereich höchstens eine British-Recovery-Auslösung ohne Festfahren im Endzustand.

---

