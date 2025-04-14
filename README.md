# 🏨 Hotelreservierungssystem, Projektdokumentation

Dieses Projekt wurde im Rahmen des Moduls **Anwendungsentwicklung mit Python** an der FHNW realisiert. Es handelt sich um ein Hotelreservierungssystem, das auf einem objektorientierten Ansatz basiert. Ziel war es, definierte User Stories umzusetzen und ein funktionsfähiges System zu entwickeln, das Hotels, Zimmer, Buchungen, Rechnungen und Bewertungen verwaltet.

## Projektteam & Rollenverteilung

Unser Team hat die Aufgaben in zwei Bereichen aufgeteilt:

1. **Fachliche Rollen**: welche technischen Teile des Projekts hat jedes Mitglied umgesetzt 
2. **Projektrollen**: wer ist für Qualität, Dokumentation, Codepflege und GitHub verantwortlich

---

### Kerstin Culjak
**Fachlich:**  
 

**Projektrolle:**  


---

### Lisa Wüest 
**Fachlich:**  


**Projektrolle:**  


---

### Sheyla Sampietro  
**Fachlich:**  


**Projektrolle:**  


---

### Andrea Petretta 
**Fachlich:**  


**Projektrolle:**  


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

→ Zuständig: **Name**

### 2. Details zu Zimmern sehen
- Beschreibung, Preis, max. Gäste, Ausstattung

→ Zuständig: **Name**

### 4. Buchung erstellen
- Zimmer auswählen, Daten eingeben, Buchung bestätigen

→ Zuständig: **Name**

### 5. Rechnung erhalten
- Rechnung wird nach Aufenthalt generiert

→ Zuständig: **Name**

### 6. Buchung stornieren
- Buchung auf “cancelled” setzen, Invoice anpassen

→ Zuständig: **Name**

### 7. Dynamische Preisgestaltung
- Saisonfaktor berücksichtigt Hoch- und Nebensaison

→ Zuständig: **Name**

### Erweiterte Story: Bewertungen
- Bewertung erstellen, lesen, ändern, löschen

→ Zuständig: **Name**

---

## Projektstruktur in GitHub & Deepnote

Siehe Repository-Struktur im README.md auf GitHub (Projektordner `Hotelreservierungssystem`) und Deepnote-Projektintegration.

---
