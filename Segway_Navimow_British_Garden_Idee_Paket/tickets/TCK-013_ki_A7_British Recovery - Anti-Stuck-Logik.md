# British Recovery / Anti-Stuck-Logik

**Als Tester im Segway British-Garden-Prototyp** möchte ich,
dass British Recovery bei Rand- und Corner-Locks die kritischen Waypoints überspringt,
damit der Mäher nicht festgefahren bleibt und den Plan zuverlässig fertig fährt.

**Akzeptanzkriterien:**
- Bei blockierter Bewegung springt die Anzeige „British Recovery" von `OK` auf `Skip n` bzw. `Escape n` (Test 5, n mit fortlaufender Nummer).
- Der Mäher wiederholt niemals denselben Waypoint endlos: Skip überspringt den Waypoint inkl. Folge-Waypoints (Designannahme E2/E3, Skip +3).
- Waypoints mit Randabstand < Sicherheitsgrenze werden präventiv übersprungen (Designannahme E3: < 21 px).
- Skip- und Escape-Zähler sind im Activity Log nachvollziehbar.

---

