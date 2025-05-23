# Hotelreservierungssystem, Projektdokumentation

Dieses Projekt wurde im Rahmen des Moduls **Anwendungsentwicklung mit Python** an der FHNW realisiert.

Es handelt sich um ein Hotelreservierungssystem, das auf einem objektorientierten Ansatz basiert.

Ziel war es, definierte User Stories umzusetzen und ein funktionsfähiges System zu entwickeln, das Hotels, Zimmer, Buchungen, Rechnungen und Bewertungen verwaltet.

## Projektteam & Rollenverteilung

Unser Team hat die Aufgaben in zwei Bereichen aufgeteilt:

1. **Fachliche Rollen**: Welche technischen Teile des Projekts hat jedes Mitglied umgesetzt 
2. **Projektrollen**: Wer ist für Qualität, Dokumentation, Codepflege und GitHub verantwortlich

---Ja

### Kerstin Culjak
**Fachlich:**  
→ Zuständig für die Klassen `Guest` und `Review`  
→ Fokus: Gästemanagement und Bewertungen

**Projektrolle:**  
→ Quality Manager: Prüft alle Komponenten auf Korrektheit, Qualität und Einhaltung der Anforderungen. Achtet auf konsistente Datenstrukturen und logische Beziehungen.  
→ Review Checker: Verantwortlich für Code-Reviews und finale Durchsicht vor der Abgabe.

---

### Lisa Wüest 
**Fachlich:**  
→ Zuständig für die Klassen `Room`, `Facility` und `RoomType`  
→ Fokus: Zimmerverwaltung, Zimmertypen und Ausstattung

**Projektrolle:**  
→ Code Stylist: Achtet auf eine konsistente Code-Formatierung, klare Struktur, sprechende Methodenbezeichner und einheitlichen Stil im gesamten Team.  
→ Notebook Coordinator: Verantwortlich für die logische Anordnung und den Aufbau der Deepnote-Blöcke (z.B. Kapitelstruktur, Inputs/Outputs, Visualisierung).

---

### Sheyla Sampietro  
**Fachlich:**  
→ Zuständig für die Klassen `Address` und `Hotel`  
→ Fokus: Adressverwaltung und Hoteldaten inkl. Bewertungen & Zimmer

**Projektrolle:**  
→ Documentation Lead: Sorgt dafür, dass alle relevanten Informationen im Deepnote-Notebook dokumentiert und sauber erklärt sind. Achtet auf vollständige Einleitung, User Stories, Reflexion und saubere Formatierung.  
→ User Story Coordinator: Verknüpft die User Stories mit der technischen Umsetzung und achtet darauf, dass alle Stories nachvollziehbar umgesetzt werden.

---

### Andrea Petretta 
**Fachlich:**  
→ Zuständig für die Klassen `Booking` und `Invoice`  
→ Fokus: Buchungsabläufe und Rechnungsstellung

**Projektrolle:**  
→ Milestone Planner: Achtet auf die Einhaltung von Abgabeterminen, hilft bei der Aufteilung von Teilzielen und erinnert das Team an nächste Schritte.  
→ Feature Integrator: Sorgt dafür, dass Buchung, Rechnung, Gäste und Zimmer sauber zusammenspielen (inkl. Übergabe an Business Logic und Notebook).

---

Diese Rollenverteilung half uns, effizient zu arbeiten und die Projektziele strukturiert zu erreichen.


## Projektstruktur

Gemäss dem vorgegebenen Layer-Modell:
- `business_logic/`: Logik für Buchungen, Bewertungen, Preise
- `data_access/`: Zugriff auf SQLite-Datenbank (CRUD)
- `database/`: Unsere hotel_reservation_sample.db Datei
- `model/`: Enthält alle Klassen (Hotel, Room, Guest, etc.)
- `ui/`: Einfache Eingabevalidierung (z.B. input_helper)

---

# Umgesetzte User Stories

## Für Gäste

### 1. Hotels durchsuchen & filtern
- Stadt
- Sterne
- Gästeanzahl
- Verfügbarkeit (Datum)
- Kombination aller Kriterien

→ Zuständig: **Sheyla**

### 2. Details zu Zimmern sehen
- Beschreibung, Preis, max. Gäste, Ausstattung

→ Zuständig: **Lisa**

### 4. Buchung erstellen
- Zimmer auswählen, Daten eingeben, Buchung bestätigen

→ Zuständig: **Andrea** (mit Unterstützung von Kerstin)

### 5. Rechnung erhalten
- Rechnung wird nach Aufenthalt generiert

→ Zuständig: **Andrea**

### 6. Buchung stornieren
- Buchung auf “cancelled” setzen, Invoice anpassen

→ Zuständig: **Andrea**

### 7. Dynamische Preisgestaltung
- Saisonfaktor berücksichtigt Hoch- und Nebensaison

→ Zuständig: **Lisa**

### Erweiterte Story: Bewertungen
- Bewertung erstellen, lesen, ändern, löschen

→ Zuständig: **Kerstin**

---

## Projektstruktur in GitHub & Deepnote

Siehe Repository-Struktur im README.md auf GitHub (Projektordner `Hotelreservierungssystem`) und Deepnote-Projektintegration.

---

 Reflexion & Methodik

Wir haben uns zu Beginn mit der Referenzstruktur vertraut gemacht und diese dann schrittweise mit eigenen Inhalten gefüllt.
Die Aufteilung in Fach- und Projektrollen hat sich als sehr effizient erwiesen. Jedes Teammitglied konnte seine Stärken einbringen.
Der Fokus lag auf funktionierender Logik, sauberem Code, verständlichen Notebooks und strukturierter Dokumentation.

---
