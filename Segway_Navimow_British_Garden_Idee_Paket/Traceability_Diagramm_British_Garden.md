# Traceability-Diagramm – British Garden Mode

**Zweck:** Beleg der drei Risikoaussagen aus der Traceability-Analyse (Testanleitung `Version_korrigiert_1_4_1_british_recovery` vs. Anforderungsdokument `Segway_Idee_British_Garden_Nazca_Navimow`).

**Legende der Farbcodes (Testabdeckung je Funktionsschritt):**

| Farbe | Bedeutung |
|---|---|
| 🟩 / grüne Klasse | **vollständig** – Testfall prüft den Schritt tatsächlich |
| 🟨 / gelbe Klasse | **teilweise** – Schritt wird berührt, aber nicht vollständig geprüft |
| 🟧 / orange Klasse | **unklar** – nur subjektive Beobachtung, kein messbares Kriterium |
| 🟥 / rote Klasse | **keine** – kein Testfall prüft diesen Schritt |

---

## 1. Funktionsfluss British Garden Mode mit Testabdeckungs-Layer

Jeder Knoten zeigt den Code der zugehörigen Anforderung (A1–A12) und die Testfälle, die ihn abdecken (T1–T8).

```mermaid
flowchart TD
    START([Simulation starten<br/>T1]):::tested
    MODE{Modus wählen:<br/>Random / Smart / British<br/>A1 — T2·T3·T4}:::partial

    %% --- Random / Vergleich ---
    MODE -->|Random| RND[Zufallsbewegung fahren<br/>A10-Vergleichsbasis — T2]:::tested

    %% --- Smart ---
    MODE -->|Smart| SMART1[Smart-Ziel in ungemähtem<br/>Bereich setzen — T3]:::unclear
    SMART1 --> SMART2[Orientierung zu offenen<br/>Flächen stärker — A10, T3<br/>keine Metrik!]:::unclear
    SMART2 --> STUCKS{Anti-Stuck? — T3}:::partial

    %% --- British Garden ---
    MODE -->|British| PARAM[Linien-Parameter setzen:<br/>Winkel A3 — T5·T8<br/>Abstand A4 — nur 34px, T4]:::partial
    PARAM --> NAZCA{Nazca-Zone<br/>aktiv? — T6}:::partial
    NAZCA -->|ja| CUT[Zone bei Linienplanung<br/>aussparen — A6, T6A<br/>nur Augenschein]:::unclear
    NAZCA -->|nein| FULL[Linien laufen durch<br/>den Bereich — T6B]:::tested
    CUT --> PLAN
    FULL --> PLAN
    PLAN[Paralleles Bahnenraster<br/>berechnen — A2, T4]:::tested
    PLAN --> FOLLOW[Mower folgt Bahnen,<br/>Anzeige Fortschritt — A2, T4]:::tested
    FOLLOW --> BLOCK{Rand- /<br/>Corner-Lock? — T5·T7}:::tested
    BLOCK -->|ja| RECOV[British Recovery:<br/>Skip n / Escape n,<br/>kritische Waypoints überspringen<br/>A7 — T5·T7·T8]:::tested
    BLOCK -->|nein| MOW
    RECOV -->|neuer Anlauf| FOLLOW
    RECOV -->|Endlosschleife<br/>möglich?| LOOP[Kein endloses Anfahren<br/>desselben Waypoints — A11<br/>kein Zeit-/Zählerkriterium]:::partial
    MOW[Fläche mähen,<br/>Coverage aktualisieren — A8, T1·T4]:::partial
    MOW --> ZONE{Nazca-Fläche<br/>ungemäht geblieben? — A12<br/>KEIN Test!}:::none

    %% --- Editor ---
    EDIT[Fläche per Editor ziehen,<br/>Plan neu berechnen — T7<br/>keine Anforderung = Waise]:::partial
    MODE -.-> EDIT
    EDIT -.-> PARAM

    %% --- Export (Separatfunktion) ---
    EXPORT[Konfiguration als<br/>JSON exportieren — A9<br/>KEIN Test!]:::none
    PARAM -.-> EXPORT

    %% --- Stilklassen ---
    classDef tested fill:#c8e6c9,stroke:#2e7d32,color:#000
    classDef partial fill:#fff9c4,stroke:#f9a825,color:#000
    classDef unclear fill:#ffe0b2,stroke:#ef6c00,color:#000
    classDef none fill:#ffcdd2,stroke:#c62828,color:#000
```

### Was der Fluss belegt

- **Risikoaussage 1 (JSON-Export ungetestet):** Der rote Knoten `EXPORT` hängt am Funktionsweg, wird aber von keinem Testpfad erreicht.
- **Risikoaussage 2 (Biodiversität ungeschützt):** Der rote Knoten `ZONE` ist der Endpunkt der Funktion – ausgerechnet dort, wo das Kernversprechen „High-Grass bleibt stehen" liegt, verläuft der Flow in eine ungetestete Sackgasse.
- **Risikoaussage 3 (Konfiguration „bedient, nicht verifiziert"):** Die Knoten `PARAM` (Abstand nur 1 Wert) und `SMART2` (subjektiv, ohne Metrik) sind orange – die Verifikation endet vor den eigentlichen Wirksamkeitsprüfungen.
- **Waisen:** Der gestrichelte `EDIT`-Zweig wird getestet (T7), existiert aber im Anforderungsdokument nicht.

---

## 2. Coverage-Heatmap: Anforderungen × Testfälle

| Anforderung | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | Summe-Status |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| A1 Umschaltbare Navigation | | 🟨 | 🟨 | 🟨 | | | | 🟨 | 🟨 teilweise |
| A2 Parallele Linien | | | | 🟩 | | | 🟨 | 🟩 | 🟩 vollständig |
| A3 Linienwinkel einstellbar | | | | 🟨 | 🟨 | | | 🟨 | 🟨 teilweise |
| A4 Linienabstand einstellbar | | | | 🟧 | | | | | 🟧 unklar |
| A5 Nazca-Zone optional | 🟨 | | | | | 🟨 | | 🟨 | 🟨 teilweise |
| A6 Aussparung bei Planung | | | | | | 🟧 | | 🟧 | 🟧 unklar |
| A7 Recovery-Logik | | | 🟨 | | 🟩 | | 🟩 | 🟩 | 🟩 vollständig |
| A8 Coverage dauerhaft sichtbar | 🟨 | | | 🟨 | | | | | 🟨 teilweise |
| A9 JSON-Export | | | | | | | | | 🟥 keine |
| A10 Smart-Zielsuche | | 🟨 | 🟧 | | | | | 🟧 | 🟧 unklar |
| A11 Keine Waypoint-Dauerschleife | | | | | 🟨 | | | 🟨 | 🟨 teilweise |
| A12 High-Grass bleibt ungemäht | | | | | | 🟧 | | | 🟧 unklar |

**Waisen (Tests ohne Anforderung):** T1 Teilaspekt Batterie/Heading/Activity-Log · T3 „Smart-Ziel blau" · T4 Anzeige „1/40" · T7 Editor-Neuberechnung · T8 Zeile F (135°, Erwartungsspalte leer).

---

## 3. Abdeckungsverteilung (Überblick)

```mermaid
pie showData title Abdeckungsstatus der 12 Anforderungen
    "vollständig" : 2
    "teilweise" : 5
    "unklar" : 4
    "keine" : 1
```

---

## 4. Direkter Bezug zu den Risikoaussagen

| Risikoaussage | Belegstelle im Diagramm |
|---|---|
| 1. JSON-Export versprochen, aber ungetestet | Roter Knoten `EXPORT` in Abschnitt 1; Zeile A9 in Abschnitt 2 |
| 2. „Biodiversität: High-Grass bleibt stehen" ungeschützt | Roter Knoten `ZONE` (Funktionsendpunkt) in Abschnitt 1; Zeile A12 in Abschnitt 2 |
| 3. Winkel/Abstand „bedient, nicht verifiziert" | Orange Knoten `PARAM` und `SMART2` in Abschnitt 1; Zeilen A3/A4/A10 in Abschnitt 2 |
