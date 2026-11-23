# Coverage dauerhaft sichtbar

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass die bereits gemähte Fläche dauerhaft und lückenlos sichtbar bleibt,
damit ich die Abdeckung über die gesamte Session prüfen kann.

**Akzeptanzkriterien:**
- Bereits gemähte Zellen bleiben sichtbar, bis „Fläche löschen" aktiviert wird (Designannahme C2: 10 × 10-px-Raster über Rasen).
- Die Coverage-Prozentanzeige berechnet sich aus gemähten Zellen / Rasenfläche und liegt nie über 100 %.
- „Fläche löschen" resettet Coverage, während der British-Plan erhalten bleibt (Designannahme C4) – Verhalten dokumentiert und reproduzierbar.
- Neuberechnung des Plans im Editor verfälscht bereits dargestellte Coverage-Markierungen nicht.

---

