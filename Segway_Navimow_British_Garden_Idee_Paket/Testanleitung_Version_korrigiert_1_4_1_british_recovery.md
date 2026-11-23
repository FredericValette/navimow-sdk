# Testanleitung - Version_korrigiert_1.4.1_british_recovery

## Ziel der Version
Diese Version demonstriert eine Simulationsidee fuer einen Navimow-aehnlichen Maehroboter mit drei Navigationsarten:

1. **Random Navigation** fuer Vergleichstests.
2. **Smart Navigation** mit Zielsuche in ungemaahten Bereichen.
3. **British Garden Mode** fuer optisch saubere, parallele Maehlinien.

Zusaetzlich bleibt die **Nazca-Linie** als High-Grass-Zone optional sichtbar und wird im British Garden Mode bei der Linienplanung ausgespart.

---

## Dateien

- `Version_korrigiert_1_4_1_british_recovery.html` - komplette lauffaehige HTML-Demo.
- `Testanleitung_Version_korrigiert_1_4_1_british_recovery.md` - diese Testanleitung.
- `Segway_Idee_British_Garden_Nazca_Navimow.md` - vorbereiteter Ideentext fuer Segway/Navimow.

---

## Schnellstart

1. Die HTML-Datei lokal herunterladen.
2. Datei per Doppelklick im Browser oeffnen.
3. Empfohlen: Microsoft Edge oder Chrome verwenden.
4. Browser-Konsole optional mit `F12` oeffnen, um Fehler zu sehen.

---

## Basistest

### Test 1 - Start und Rendering

Erwartung:

- Karte wird angezeigt.
- Rasenflaeche wird gruen angezeigt.
- Nazca-Linie wird gelb angezeigt.
- Mower bewegt sich.
- Batterie, Heading und Coverage werden aktualisiert.

Pruefung:

- Keine JavaScript-Fehler in der Konsole.
- Activity Log zeigt Initialisierung.

---

## Navigationstests

### Test 2 - Random Navigation

1. Button **Random** aktivieren.
2. **Fläche löschen** klicken.
3. **Reset** klicken.
4. Einige Zeit laufen lassen.

Erwartung:

- Bewegung wirkt zufaellig.
- Coverage steigt, aber mit sichtbaren Ueberlappungen.
- Randbereiche koennen unregelmaessig bearbeitet werden.

Zweck:

- Vergleichsbasis gegen Smart und British Garden.

---

### Test 3 - Smart Navigation

1. Button **Smart** aktivieren.
2. **Fläche löschen** klicken.
3. **Reset** klicken.
4. Beobachten, ob der Mower ungemaahten Bereichen gezielter folgt.

Erwartung:

- Smart-Ziel erscheint blau.
- Mower orientiert sich staerker zu offenen Bereichen.
- Anti-Stuck zeigt bei Problemen `Warn` oder `Recovery`.

---

### Test 4 - British Garden Mode mit parallelen Linien

1. Button **British Garden** aktivieren.
2. `British Linien-Winkel` auf `0°` setzen.
3. `British Linien-Abstand` auf `34 px` setzen.
4. **Fläche löschen** klicken.
5. **Reset** klicken.

Erwartung:

- Blaue gestrichelte parallele Bahnen werden angezeigt.
- Mower folgt den Bahnen.
- Die Anzeige **British** zeigt z.B. `1/40` oder aehnlich.
- Gemaaehte Flaeche bleibt sichtbar.

---

## Rand- und Corner-Lock-Tests

### Test 5 - British Recovery am Rand

1. British Garden aktivieren.
2. Winkel `0°` testen.
3. Danach Winkel `45°` testen.
4. Danach Winkel `90°` testen.
5. Beobachten, ob der Mower an Ecken blockiert.

Erwartung:

- Bei blockierter Bewegung springt **British Recovery** von `OK` auf `Skip n` oder `Escape n`.
- Der Mower versucht nicht endlos denselben Waypoint anzufahren.
- Kritische Waypoints am Rand werden uebersprungen.

---

### Test 6 - Nazca-Linie sichtbar vs. unsichtbar

Variante A:

1. **Nazca Linie** aktiv lassen.
2. British Garden aktivieren.
3. Linienplan beobachten.

Erwartung:

- British-Linien werden um die Nazca-High-Grass-Zone herum geplant.

Variante B:

1. **Nazca Linie** deaktivieren.
2. British Garden erneut aktivieren.

Erwartung:

- Linien koennen durch den Bereich laufen, der vorher als Nazca ausgespart wurde.

---

## Editor-Test

1. **Fläche bearbeiten** aktivieren.
2. Eckpunkte der Rasenflaeche mit Maus oder Touch ziehen.
3. British Garden erneut aktivieren.

Erwartung:

- Linienplan wird neu berechnet.
- British Recovery hilft besonders bei spitzen Ecken und L-Formen.

---

## Empfohlene Testmatrix

| Testfall | Nazca | Navigation | Winkel | Erwartung |
|---|---|---|---|---|
| A | Ein | Random | n/a | Referenzverhalten |
| B | Ein | Smart | n/a | gezieltere Coverage |
| C | Ein | British | 0° | parallele Linien, Nazca ausgespart |
| D | Ein | British | 45° | diagonal, Recovery bei Randfaellen |
| E | Aus | British | 90° | Linien ohne Nazca-Aussparung |
| F | Ein | British | 135° | Stress-Test fuer Ecken |

---

## Bekannte Grenzen

- Es ist eine Browser-Simulation, kein echtes Navimow-Firmware-Modell.
- Die Flächenberechnung basiert auf Canvas-Pixeln und ist nur modellhaft.
- British Garden optimiert sichtbare Linien, nicht zwingend kuerzeste Fahrzeit.
- No-Go-Zonen und Nazca-Flächen werden geometrisch vereinfacht behandelt.

---

## Erfolgskriterien

Eine Testsession gilt als erfolgreich, wenn:

- die Simulation ohne JavaScript-Fehler startet;
- British Garden parallele Linien erzeugt;
- Nazca sichtbar optional ausgespart wird;
- gemähte Fläche dauerhaft sichtbar bleibt;
- British Recovery bei Rand-/Corner-Locks Waypoints überspringt;
- Wechsel zwischen Random, Smart und British funktioniert.
