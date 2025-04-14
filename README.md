# 🏨 Hotelreservierungssystem, Projektdokumentation

Dieses Projekt wurde im Rahmen des Moduls **Anwendungsentwicklung mit Python** an der FHNW realisiert. Es handelt sich um ein Hotelreservierungssystem, das auf einem objektorientierten Ansatz basiert. Ziel war es, definierte User Stories umzusetzen und ein funktionsfähiges System zu entwickeln, das Hotels, Zimmer, Buchungen, Rechnungen und Bewertungen verwaltet.

## Projektteam & Rollenverteilung

Unser Team hat die Aufgaben in zwei Bereichen aufgeteilt:

1. **Fachliche Rollen**: welche technischen Teile des Projekts hat jedes Mitglied umgesetzt 
2. **Projektrollen**: wer ist für Qualität, Dokumentation, Codepflege und GitHub verantwortlich

---

### Sheyla  
**Fachlich:**  
- Zuständig für die Modellierung (UML, Klassendiagramm)  
- Umsetzung der Hotel- und Zimmerlogik  
- Erstellung der Projektbeschreibung in Deepnote  

**Projektrolle:**  
- *Documentation Lead*  
  → Verantwortlich für README, Kommentare und textliche Dokumentation

---

###Teammitglied A  
**Fachlich:**  
- Verantwortlich für die Datenbankanbindung (Data Access Layer)  
- Umsetzung von `guest_dal.py`, `hotel_dal.py` usw.  

**Projektrolle:**  
- *Code Stylist*  
  → Achtete auf sauberen, konsistenten Code (Formatierung, Struktur, Benennung)

---

### Teammitglied B  
**Fachlich:**  
- Verantwortlich für die Business Logic (z. B. `BookingManager`)  
- Erstellung der interaktiven Deepnote-Notebooks zur Buchung  

**Projektrolle:**  
- *Quality Manager*  
  → Testete Funktionen und überprüfte, ob alle User Stories erfüllt wurden

---

### 👩‍💻 Teammitglied C  
**Fachlich:**  
- Zuständig für Bewertungen, Preisberechnung und Rechnungen  
- Implementierung von `ReviewManager`, `Invoice`, `calculate_dynamic_price()`  

**Projektrolle:**  
- *GitHub Admin*  
  → Pflegte das Repository, organisierte die Struktur und behielt den Überblick über Änderungen

---

Diese Rollenverteilung half uns, effizient zu arbeiten und die Projektziele strukturiert zu erreichen.


---

Diese Rollen wurden zusätzlich zu den inhaltlichen Aufgaben (z. B. UML, Datenbank, Logik) vergeben, um ein professionelleres Arbeiten im Team zu ermöglichen.


## 🧱 Projektstruktur

Gemäss dem vorgegebenen Layer-Modell:
- `model/`: Enthält alle Klassen (Hotel, Room, Guest, etc.)
- `data_access/`: Zugriff auf SQLite-Datenbank (CRUD)
- `business_logic/`: Logik für Buchungen, Bewertungen, Preise
- `ui/`: Einfache Eingabevalidierung (z. B. input_helper)
- `database/`: Unsere hotel_reservation_sample.db Datei

---

# 📌 Umgesetzte User Stories

## 💼 Für Gäste

### 1. Hotels durchsuchen & filtern
- Stadt
- Sterne
- Gästeanzahl
- Verfügbarkeit (Datum)
- Kombination aller Kriterien

→ Zuständig: **Sheyla**

### 2. Details zu Zimmern sehen
- Beschreibung, Preis, max. Gäste, Ausstattung

→ Zuständig: **Teammitglied A**

### 4. Buchung erstellen
- Zimmer auswählen, Daten eingeben, Buchung bestätigen

→ Zuständig: **Teammitglied B**

### 5. Rechnung erhalten
- Rechnung wird nach Aufenthalt generiert

→ Zuständig: **Teammitglied B**

### 6. Buchung stornieren
- Buchung auf “cancelled” setzen, Invoice anpassen

→ Zuständig: **Teammitglied C**

### 7. Dynamische Preisgestaltung
- Saisonfaktor berücksichtigt Hoch- und Nebensaison

→ Zuständig: **Teammitglied C**

### ➕ Erweiterte Story: Bewertungen
- Bewertung erstellen, lesen, ändern, löschen

→ Zuständig: **Sheyla**

---

## 🛠️ Projektstruktur in GitHub & Deepnote

Siehe Repository-Struktur im README.md auf GitHub (Projektordner `Hotelreservierungssystem`) und Deepnote-Projektintegration.

---
