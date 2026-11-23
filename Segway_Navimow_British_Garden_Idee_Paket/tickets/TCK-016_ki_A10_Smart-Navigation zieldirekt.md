# Smart-Navigation zieldirekt

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

