# High-Grass-Zone bleibt ungemäht

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

