XXXXXXXXXXXXX LÖSCHEN VOR ABGABE XXXXXXXXXXXXX

Das README.md-File sollte Folgendes enthalten:

1. Name und Vorname der Teammitglieder, die am Projekt mitgearbeitet haben
2. Eine kurze Übersicht, wer zu welchen Projekt-Themen beigetragen hat (also z. B. zu welchen User-Stories, Files, Projektphasen, Rollen innerhalb des Teams etc.).
   Themen, die durch mehrere Teammitglieder bearbeitet wurden, dürft ihr bei allen jeweiligen Teammitgliedern aufführen.
3. Instruktion für uns, wie eure Applikation benutzt werden muss (Schritt-für-Schritt-Anleitung, insb. welche Notebooks oder Files ausgeführt werden müssen).
4. Annahmen und Interpretationen, falls welche vorhanden sind.
x
x
x
x
x
x
x
x


# Hotelreservierungssystem - Projektdokumentation
**DeepNote Link:** [Projekt in Deepnote öffnen](https://deepnote.com/workspace/Kculjak-a051eb87-a3df-411f-b9a2-009e7412)


## Projektübersicht

Dieses Projekt wurde im Rahmen des Moduls „Anwendungsentwicklung mit Python“ an der FHNW im Frühlingssemester 2025 entwickelt. Ziel war die schrittweise
Umsetzung eines funktionalen Hotelreservierungssystems anhand vordefinierter und erweiterter User Stories.
Der Fokus lag auf objektorientierter Programmierung (OOP), Datenbankzugriff, Modularisierung und agiler Entwicklung.

Das System erlaubt es Gästen, Hotels und Zimmer zu suchen und zu buchen. Rechnungen können generiert werden, zudem stehen Admin-Funktionalitäten 
für Hotelverwaltung zur verfügung.


## Projektteam & Rollenverteilung

Unser Team hat die Aufgaben in zwei Bereichen aufgeteilt:

Fachliche Rollen: Welche technischen Teile des Projekts hat jedes Mitglied umgesetzt ?

Projektrollen: Wer ist für Qualität, Dokumentation, Codepflege und GitHub verantwortlich ?

**Kerstin Culjak**

Fachlich:

- Zuständig für die Klassen Guest und Review
- Fokus: Gästemanagement und Bewertungen
- Video Koordinatorin

Projektrolle:

- Quality Manager: Prüft alle Komponenten auf Korrektheit, Qualität und Einhaltung der Anforderungen.
- Achtet auf konsistente Datenstrukturen und logische Beziehungen.
- Review Checker: Verantwortlich für Code-Reviews und finale Durchsicht vor der Abgabe.

**Lisa Wüest**

Fachlich:

- Zuständig für die Klassen Room, Facility und RoomType
- Fokus: Zimmerverwaltung, Zimmertypen und Ausstattung

Projektrolle:

- Code Stylist: Achtet auf eine konsistente Code-Formatierung, klare Struktur, sprechende Methodenbezeichner und einheitlichen Stil im gesamten Team.
- Notebook Coordinator: Verantwortlich für die logische Anordnung und den Aufbau der Deepnote-Blöcke (z.B. Kapitelstruktur, Inputs/Outputs, Visualisierung).

**Sheyla Sampietro**

Fachlich:

- Zuständig für die Klassen Address und Hotel
- Fokus: Adressverwaltung und Hoteldaten inkl. Bewertungen & Zimmer

Projektrolle:

- Documentation Lead: Sorgt dafür, dass alle relevanten Informationen im Deepnote-Notebook dokumentiert und sauber erklärt sind.
- Achtet auf vollständige Einleitung, User Stories, Reflexion und saubere Formatierung.
- User Story Coordinator: Verknüpft die User Stories mit der technischen Umsetzung und achtet darauf, dass alle Stories nachvollziehbar umgesetzt werden.

**Andrea Petretta**

Fachlich:

- Zuständig für die Klassen Booking und Invoice
- Fokus: Buchungsabläufe und Rechnungsstellung
- Visual Paradigm Master

Projektrolle:

- Milestone Planner: Achtet auf die Einhaltung von Abgabeterminen, hilft bei der Aufteilung von Teilzielen und erinnert das Team an nächste Schritte.
- Feature Integrator: Sorgt dafür, dass Buchung, Rechnung, Gäste und Zimmer sauber zusammenspielen (inkl. Übergabe an Business Logic und Notebook).

Diese Rollenverteilung half uns, effizient zu arbeiten und die Projektziele strukturiert zu erreichen.

## Projektstruktur

Unser Projekt folgt einer modularen Architektur, bei der jede Schicht eine klar definierte Verantwortung übernimmt.
Die Kommunikation erfolgt über Python-Importe zwischen den Modulen.


| Verzeichnis       | Beschreibung                                            |
| ----------------- | ------------------------------------------------------- |
| `database/`       | SQLite-Datenbankdatei (`hotel_reservation_sample.db`)   |
| `model/`          | Klassen für Datenmodelle wie Hotel, Room, Booking etc.  |
| `data_access/`    | Data Access Layer: SQL-Zugriff (CRUD)                   |
| `business_logic/` | Geschäftslogik: Preisberechnung, Buchung, Rechnung usw. |
| `ui/`             | Eingabevalidierung & User Interaction via Notebooks     |
| `notebooks/`      | Deepnote-Notebooks zur Ausführung der Use Cases         |

## Verwendete Technologien

Wir haben die folgenden Technologien verwendet:

- Python 3.10+

- SQLite als relationale Datenbank

- Deepnote für interaktive Entwicklung und Visualisierung

- Git / GitHub für Versionierung, Branching und Dokumentation

- Objektorientierte Programmierung (OOP)

- Visual Paradigm zur Modellierung des Klassendiagramms

## Getting Started

Projekt klonen:

git clone https://github.com/AEPFS2025GroupB3/Hotelreservierungssystem.git

1. Deepnote-Projekt öffnen (alternativ lokal mit PyCharm starten)
2. Arbeitsverzeichnis in Deepnote setzen:
3. Rechtsklick auf das Notebook → Set Working Directory → /Hotelreservierungssystem
4. Notebook öffnen:
→  Hotelreservierungssystem.ipynb im Ordner deepnote/GroupB3/

Hinweis: Die verwendete SQLite-Datenbank befindet sich im Ordner database/. Die Originaldatei heisst hotel_reservation_sample.db.
Für die Arbeit im Notebook empfehlen wir, eine Kopie mit dem Namen working_db.db zu verwenden, damit die Ausgangsdatenbank nicht verändert wird.

## Umgesetzte User Stories

**Technologe hinter den User Stories**

Im Folgenden beschreiben wir die User Stories 1 bis 10 detailliert: Ziel, Funktionsweise und Nutzung im Notebook.

**User Story 1.1 - Hotels nach Stadt filtern**

- Ziel:
Der Gast möchte alle Hotels in einer bestimmten Stadt durchsuchen, um seinen bevorzugten Standort auszuwählen.

- Umsetzung im Code:
Die Logik befindet sich in hotel_data_access.py und hotel_manager.py. Mithilfe eines SQL-Statements wird die Hotel-Tabelle nach dem Stadt-Feld gefiltert.

- Nutzung im Notebook:
Notebook öffnen: 01_Suche_und_Filterung.ipynb XXXXXXXXX ANSCHAUEN XXXXXXXXXXX

Stadtname (z.B. "Zürich") eingeben 

Ausgabe: Liste der Hotels in dieser Stadt

**User Story 1.2 - Filterung nach Sternebewertung**

- Ziel:
Der Gast möchte nur Hotels mit mindestens X Sternen angezeigt bekommen.

- Umsetzung im Code:
In hotel_data_access.py wird die SQL-Abfrage erweitert um WHERE rating >= x. Der Filter kann mit der Stadtabfrage kombiniert werden.

- Nutzung im Notebook:
Stadt und Mindestanzahl Sterne eingeben (z.B. "Zürich", min. 4 Sterne)

Rückgabe: Liste gefilterter Hotels mit entsprechender Bewertung

**User Story 1.3 Filterung nach Gästeanzahl**

- Ziel:
Der Gast möchte Hotels finden, deren Zimmer zur Gästeanzahl passen (z.B. 3 Personen).

- Umsetzung im Code:
Die Filterung erfolgt über die room-Tabelle, wo max_guests mit der Eingabe verglichen wird. Es wird geprüft, ob mindestens ein Zimmer im Hotel
die gewünschte Gästeanzahl aufnehmen kann.

- Nutzung im Notebook:
Stadt, Sterne und Gästeanzahl eingeben

Ausgabe: Hotels mit passenden Zimmern

**User Story 1.4 - Verfügbarkeit nach Datum filtern**

- Ziel:
Der Gast möchte nur Hotels sehen, die im gewählten Zeitraum freie Zimmer anbieten.

- Umsetzung im Code:
Die Logik prüft in booking_data_access.py, ob Zimmer bereits im gewünschten Zeitraum gebucht wurden. SQL-Abfragen nutzen Datumsvergleiche (check-in/out).
Frei ist ein Zimmer nur, wenn es in diesem Zeitraum nicht in einer Buchung vorkommt.

- Nutzung im Notebook:
Stadt, Daten (Check-in und Check-out) eingeben

Ausgabe: Nur Hotels mit freien Zimmern in dieser Zeit

**User Story 1.5 - Kombination aller Filterkriterien**

- Ziel:
Der Gast möchte alle Kriterien kombinieren können (z.B. Stadt + Sterne + Gästeanzahl + Zeitraum), um gezielt zu suchen.

- Umsetzung im Code:
Die Business-Logik in hotel_manager.py kombiniert Filtermethoden und übergibt Parameter an die Abfragefunktionen der Data Access-Schicht. 
Die Filter werden im SQL zusammengesetzt.

- Nutzung im Notebook:
Alle Parameter angeben: Stadt, Sterne, Gäste, Datum

Ausgabe: Nur Hotels, die allen Bedingungen entsprechen

**User Story 1.6 - Anzeige von Hotelinfos**

- Ziel:
Der Gast möchte zu jedem gefundenen Hotel folgende Infos sehen: Name, Adresse, Sternebewertung.

- Umsetzung im Code:
hotel_data_access.py stellt diese Infos in der Hauptabfrage bereit. Die Ausgabe ist reduziert auf relevante Felder (name, address, rating).

- Nutzung im Notebook:
Ausgabe nach Filterung zeigt die gewünschten Felder in einer tabellarischen Übersicht

**User Story 2.1 - Zimmerdetails anzeigen**

- Ziel:
Der Gast möchte Details zu den verfügbaren Zimmern sehen: Typ, Beschreibung, max. Gäste, Preis, Ausstattung.

- Umsetzung im Code:
Zimmerinformationen werden über room_data_access.py geladen. Die Business-Logik in room_manager.py kümmert sich um Formatierung und Präsentation.

- Nutzung im Notebook:
Nach Auswahl eines Hotels werden alle zugehörigen Zimmer mit ihren Eigenschaften angezeigt.

Felder: room_type, description, max_guests, price, facilities

**User Story 2.2 - Nur verfügbare Zimmer anzeigen**

- Ziel:
Der Gast möchte nur Zimmer angezeigt bekommen, die im gewählten Zeitraum verfügbar sind.

- Umsetzung im Code:
Buchungszeiträume werden in booking_data_access.py überprüft. Die Methode filtert Zimmer aus, die bereits belegt sind.

- Nutzung im Notebook:
Eingabe von Check-in und Check-out Datum

Ausgabe: Liste der freien Zimmer im gewählten Hotel

**User Story 3.1 - Hotel hinzufügen**

- Ziel:
Der Admin möchte neue Hotels zum System hinzufügen.

- Umsetzung im Code:
Neue Hotelobjekte werden über hotel_manager.py erstellt. Die Eingabe wird validiert, dann in hotel_data_access.py in die Datenbank geschrieben.

- Nutzung im Notebook:
Admin gibt Hotelinformationen ein (Name, Adresse, Rating)

Neues Hotel erscheint in der Übersicht

**User Story 3.2 - Hotel entfernen**

- Ziel:
Der Admin möchte ein Hotel aus dem System löschen.

- Umsetzung im Code:
Die Methode delete_hotel() in hotel_data_access.py nutzt die Hotel-ID, um den Datensatz zu löschen. Validierung erfolgt vor Ausführung.

- Nutzung im Notebook:
Hotel-ID eingeben → Hotel wird aus der Datenbank entfernt

**User Story 3.3 - Hotelinformationen aktualisieren**

- Ziel:
Der Admin möchte bestehende Hoteldaten bearbeiten (z.B. Name, Rating, Adresse).

- Umsetzung im Code:
In hotel_data_access.py gibt es eine Update-Funktion, die gezielt einzelne Felder aktualisiert. Änderungen werden im Manager geprüft.

- Nutzung im Notebook:
Hotel-ID auswählen, Felder bearbeiten

Nach dem Update wird das Hotel mit aktualisierten Daten neu angezeigt
___
### User Story 4 - Buchung erstellen

- **Ziel:**
Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.

- **Umsetzung im Code:**
Diese Umsetzung erfolgt durch Zusammenarbeit mehrerer Komponenten:

**1. HotelManager**
Die Methode `read_available_hotels_by_city_and_date(city, check_in_date, check_out_date)` wird verwendet, um alle verfügbaren Hotels in einer gewünschten Stadt für einen bestimmten Zeitraum zu laden. Diese Methode fragt die Datenbank nach Hotels ab, die im angegebenen Zeitraum freie Zimmer haben.

**2. GuestManager**
Über `get_guest_by_email(email)` wrd geprüft, ob der Gast mit der eingegebenen E-Mail bereits in der Datenbank existiert. Wir haben uns hier bewusst für die E-Mail entschieden, da sie am eindeutigsten ist. Nur registrierte Gäste können eine Buchung hinzufügen.

**3. BookingManager**
Die Methode `create_booking(…)` erstellt schliesslich die Buchung mit den übergebenen Daten wie Guest-ID, Zimmer-ID, Check-in / out Datum, Gesamtpreis und Stornierungsstatus. Im Hintergrund wird ein neuer Eintrag in die Buchungstabelle der Datenbank eingefügt, und ein Buchungsobjekt wird übergeben.

**4. BookingDataAccess**
Die Methode `create_booking(...)` führt das Einfügen in die Datenbank mit `self.execute(...)` aus. Zusätzlich werden das zugehörige Gast- und Zimmerobjekt geladen, um ein vollständiges Booking-Objekt zurückzugeben.

**Nutzung im Notebook:**
1.	Benutzer gibt gewünschte Stadt sowie Check-in und Check-out Datum ein.
2.	Die verfügbaren Hotels werden aufgelistet.
3.	Der Benutzer gibt seine E-Mail-Adresse ein.
4.	Ist der Benutzer registriert, kann er buchen.
5.	Nach Bestätigung wir die Buchung erstellt
6.	Die erfolgreiche Buchung wird mit der booking_id bestätigt.

___

### User Story 5 - Rechnung generieren

- **Ziel:**
Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

- **Umsetzung im Code:**
Umsetzung im Code: Die Implementierung dieser User Story erfolgt durch die Zusammenarbeit von BookingManager, GuestManager, HotelManager und InvoiceManager.

**1.	BookingManager**
Die Methode `get_all_bookings()` lädt alle vorhandenen Buchungen, damit der Benutzer eine davon auswählen kann. Zusätzlich stellt `get_booking(booking_id)` ein einzelnes Booking-Objekt für die Rechnungsstellung bereit.

**2.	GuestManager**
Über `get_guest(guest_id)` werden die persönlichen Informationen des Gastes geladen, die auch der Rechnung erscheinen sollen.

**3.	HotelManager**
Die Methode `get_hotel(hotel_id)` ruft die Hotelinformationen für die Buchung ab.

**4.	InvoiceManager**
Ist die zentrale Methode `create_invoice(booking, guest, hotel)` zur Umsetzung der User Story 5. 
-	Erstellt das Rechnungsdatum `(issue_date) mit date.today()`
-	Berechnet den Gesamtbetrag `calculate_total_price(..)`
-	Erstellt neuen Eintrag in der Invoice mithilfe von `InvoiceDataAccess.create_invoice(…)`

**5.	InvoiceDataAccess**
De Methode `create_invoice(….)` fürht ein SQL-Insert in die Invoice-Tabelle aus und gibt ein Invoice-Objekt zurück, das alle relevanten Informationen enthält (Buchung, Gast, Hotel, Zimmer, Betrag, Stornierungsstatus).

**Nutzung im Notebook:**
Nach erfolgreicher Buchung: Rechnung wird direkt angezeigt oder exportiert
1.	Der Benutzer gibt die Buchungs-ID ein, für die eine Rechnung generiert werden soll.
2.	Das System lädt die zugehörigen Daten (Guest, Hotel, Buchung, Betrag).
3.	Die Rechnung wird mit Datum und Betrag erstellt
4.	Falls die Buchung storniert wurde, beträgt der Rechnungsbetrag 0 CHF.
5.	Die Rechnung wird mit Mehrwertsteuer (3.8%) angezeigt:
- Nettobetrag (ohne MwSt)
- MwSt-Betrag
- = Gesamtbetrag

___
### User Story 6 - Buchung stornieren

- **Ziel:**
Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hinweis: Sorgt dafür, dass auch die zugehörige Rechnung entsprechend aktualisiert wird.

- **Umsetzung im Code:**
Die Umsetzung dieser User Story erfolgt durch die Zusammenarbeit von BookingManager, BookingDataAccess und InvoiceDataAccess.

**1.	BookingManager**
Die Methode `cancel_booking(booking_id)` übernimmt die Hauptlogik für die Stornierung:
-	Sie ruft intern `update_booking_status(...)` auf, um den Stornierungsstatus der Buchung auf True zu setzen.
-	Anschliessend wird geprüft, ob eine Rechnung zur Buchung existiert.
-	Falls eine Rechnung vorhanden ist, wird der Rechnungsstatus über `update_invoice_status(...)` auf „canceled“ gesetzt.

**2.	BookingDataAccess**
Die Methode `update_booking_status(booking_id, is_cancelled)` führt ein SQL-Update durch, das die Buchung als storniert kennzeichnet `(is_cancelled = 1)`.
Die Methode `read_booking_by_id(...)` wird verwendet, um die Buchung zu laden.


**Nutzung im Notebook:**
1.	Der Benutzer gibt eine Buchungs-ID ein.
2.	Das System prüft mit `read_booking_by_id(...)`, ob die Buchung existiert.
3.	Wenn keine Buchung gefunden wird, erscheint eine Fehlermeldung.
4.	Wenn die Buchung bereits storniert ist, erhält der Nutzer einen Hinweis.
5.	Andernfalls wird die Methode `cancel_booking(...)` aufgerufen.
6.	Die Buchung wird in der Datenbank als storniert markiert.
7.	Falls eine zugehörige Rechnung existiert, wird diese ebenfalls storniert.
8.	Der Benutzer erhält eine Bestätigung über die erfolgreiche Stornierung.

___
**User Story 7 - Saisonale Preisgestaltung**

- Ziel:
Der Gast soll je nach Saison (Hoch-/Nebensaison) unterschiedliche Preise sehen.

- Umsetzung im Code:
Ein saisonaler Multiplikator (seasonal_factor) wird in booking_manager.py automatisch berechnet basierend auf dem Check-in-Datum. Der Preis wird dynamisch
angepasst und in der Rechnung berücksichtigt.

- Nutzung im Notebook:
Datum in der Hochsaison eingeben → höherer Preis sichtbar im Zimmerangebot und auf der Rechnung

**User Story 8 - Alle Buchungen anzeigen**

- Ziel:
Als Admin möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht über alle bestehenden Buchungen erhalten.

- Umsetzung im Code:
Wir haben eine Methode mit dem Namen read_bookings_by_hotel im Booking_Manager definiert, die den Parameter hote_id verlangt. 
In der Booking Data Access Layer wird mit Hilfe eines SQL-Queries eine Abfrage auf folgenden Tabellen durchgeführt: Booking, Room, Room_Type, Hotel, Address und Guest.

Die JOINS erfolgen über die gemeinsamen IDs:
- room_id = um die Verbindung zwischen Booking und Room herzustellen
- type_id = um die Verbidung zwischen Room und Room_Type herzustellen
- hotel_id = um die Verbidung zwischen Room und Hotel herzustellen
- address_id = um die jeweilige Adresse von Gast und Hotel zu ermitteln
- guest_id = um die Verbindung zwischen Gast und Booking herzustellen

Mit WHERE wird dann die hotel_id abgefragt, damit nur die Buchungen für das gewünschte Hotel angezeigt werden. 

Mit fetchall werden alle passenden Ergebnisse aus der DB geladen. Für jede Zeile der Abfrage wird ein Booking-Objekt erzeugt, dass die Objekte Hotel(mit Adresse), Guest(mit Adresse) und Room(mit Room Type und Hotel) enthält. 

- Nutzung im Notebook:
Die User Story erfordert die Eingabe der hotel_id. Wir haben es gezielt so umgesetzt, dass der Admin die hotel_ID des Hotels eingeben muss, für welches er die bereits erfassten Bookings anschauen möchte.
Dies bezwecket, dass eine übersichtliche Liste generiert wird und die nur für das jeweilige Hotel relevanten Bookings angezeigt werden.

**User Story 9 - Zimmerliste mit Ausstattung anzeigen**

- Ziel:
Der Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.

- Umsetzung im Code:
Im Room_Manager haben wir die Methode read_room_with_facilities erstellt. Die Methode ruft in der Room Data Access die gleichnamige Methode auf.
Dort wird mit Hilfe eines SQL-Statements eine Abfrage auf folgenden Tabellen ausgeführt: Room, Room_Type, Room_Facilities, Facilities.

Die JOINS erfolgen über die Ids:
- room_id = um die Verbindung zwischen Room und Room_Facilities herzustellen
- type_id = um die Verbidung zwischen Room und Room_Type herzustellen
- facility_id = Verbindung zwischen Room_Facilities und Facilities

Wir haben LEFT JOINS verwendet, um sicherzustellen, dass auch Zimmer ohne Ausstattung im Ergebnis enthalten sind. Dadurch gehen keine Rooms verloren.
Zudem verwenden wir GROUP_CONCAT um alle Facilities pro Room (können mehrere sein) in einen kommagetrennten String zusammenzufassen. Dadurch gibt es pro Room nur eine Zeile im Resultat.
Mit fetchall werden alle Ergebnisse abgerufen. Für jede Zeile wird anschliessend ein Dictionary pro Room erstellt. Bei Facilities wird durch Split aus dem GROUP-CONCAT-String eine Liste von Strings gemacht.
Falls keine Facilities vorhanden sind, wird eine leere Liste zurückgegeben. 

- Nutzung im Notebook:
Die Methode wird aufgerufen und liefert eine Liste von Dictionaries. In der for loop wird für jedes Room-Dictionary Zimmernummer, Zimmertyp, maximale Gästeanzahl und preis pro Nacht ausgegeben. 
Wenn Facilities vorhanden sind, die Liste wird als kommaseparierte Liste ausgegeben. Ansonsten wird ausgegeben, dass keine Facilities vorhanden sind.

___
### User Story 10 - Stammdaten verwalten

- **Ziel:**
Als Admin möchte ich in der Lage sein, Stammdaten wie Zimmertypen, Einrichtungen und Preise in Echtzeit zu aktualisieren, damit das System jederzeit mit aktuellen Informationen arbeitet.

- **Umsetzung im Code:**
Die Umsetzung dieser User Story erfolgt durch die Zusammenarbeit von AdminManager, RoomTypeDataAccess, FacilityDataAccess und RoomDataAccess.

**1. AdminManager**
Der AdminManager bildet die zentrale Schicht zur Verwaltung vonStammdaten. Er bietet Methoden an für:

- Einrichtung (Facility):
`create_facility(name)`: Fügt eine neue Ausstattung hinzu.
`update_facility(facility_id, new_name)`: Benennt eine bestehende Ausstattung um.
`delete_facility(facility_id)`: Löscht eine Ausstattung aus dem System.
Hilfsmethoden wie `facility_name_exists(...)` und `get_facility_name_by_id(...)` sorgen für Validierung.

- Zimmertyp (RoomType):
`create_room_type(description, max_guests)`: Erstellt einen neuen Zimmertyp.
`update_room_type(...)`: Aktualisiert Beschreibung und maximale Gästezahl eines bestehenden Typs.
`delete_room_type(...)`: Löscht einen Zimmertyp.

- Zimmerpreis (Room):
`update_room_price(room_id, new_price)`: Ändert den Preis eines Zimmers.

**2.	FacilityDataAccess**
Diese Klasse ist für den direkten Zugriff auf die Facilities-Tabelle zuständig:
-	`create_facility(...)`: Führt ein SQL-Insert aus.
-	`update_facility_name(...)``: Aktualisiert den Namen einer Ausstattung.
-	`delete_facility(...)`: Entfernt eine Ausstattung aus der Datenbank.
-	`get_all_facilities()`: Lädt alle existierenden Ausstattungen zur Anzeige oder Validierung.

**3.	RoomDataAccess**
Wird verwendet, um den Preis einzelner Zimmer zu aktualisieren:
`update_room_price(room_id, new_price)`: SQL-Update für den Zimmerpreis.

**Nutzung im Notebook:**
1.	Das Admin-Menü bietet folgende Optionen:
   - Neue Ausstattung erstellen oder bestehende umbenennen/löschen
   - Neue Raum Typ anlegen oder bearbeiten
   - Raumpreise aktualisieren
   - Saisonale Faktoren einsehen (Lesefunktion)
2.	Je nach Auswahl werden die entsprechenden Eingaben abgefragt (z. B. Name, ID, Beschreibung, Preis).
3.	Der AdminManager ruft intern die passenden Methoden in den DataAccess-Klassen auf.
4.	Erfolgreiche Änderungen werden direkt bestätigt.

___
## User Stories mit DB-Schemaänderung

Diese User Storys erfordern eine Erweiterung des bestehenden Datenbankschemas, die nach der Umsetzung der minimalen User Storys umgesetzt wurde. 
Wir haben uns für die User Storys entschieden, die eine weitere Klasse Reviews erfordern. Dazu haben wir eine Tabelle Review mit Hilfe von SQLite Online ergänzt und um die Codes zu testen, zusätzlich auch noch ein Beispieldatensatz hinzugefügt.

**User Story 3**

- Ziel:
Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.

- Umsetzung im Code:
Im ReviewManager haben wir die Methode add_review definiert. Diese Methode erwartet die Parameter guest_id, hotel_id, rating, comment und review_date. 
Mit Hilfe eines SQL-Insert-Statements ergänzen wir die Werte in die Datenbank. Das Einfügen der Daten wird anschliessend mit self.execute ausgeführt.

- Nutzung im Notebook:
Diese User Story verlangt die Eingabe der guest_id und hotel_id, einer Bewertung zwischen 1 bis 5, eines Kommentars sowie des Datums. Die Eingabe der guest_id und hotel_id scheint auf den ersten Blick für den Gast unmöglich und komisch.
Diese Informationen sind aber notwendig und werden auf der Rechnung ausgewiesen. Sie verhindern, dass das Hotel Bewertungen von Kunden erhält die nicht im Hotel waren. 

**User Story 4**

- Ziel:
Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

- Umsetzung im Code:
Im Review Manager haben wir eine Methode get_reviews_by_hotel erstellt, die den Hotelnamen als Parameter verlangt. Diese Methode ruft in der Data Access Layer die gleichnamige Methode in der ReviewDataAccess Klasse auf.
Dort wird mit Hilfe eines SQL-Queries eine Abfrage auf folgenden Tabellen durchgeführt: Review, Guest, Address und Hotel

Die JOINS erfolgen über die gemeinsamen IDs:
- guest_id = um die Verbindung zwischen Review und Guest herzustellen
- address_id = um die jeweilige Addresse von Gast und Hotel zu ermitteln 
- hotel_id = um die Verbindung zwischen Review und Hotel herzustellen

Mit WHERE wird der Hotelname abgefragt(case-insensitive). 
Mit fetchall werden alle passenden Ergebnisse der SQL-Abfrage aus der Datenbank geladen. Daraus wird für jede Zeiel ein Review-Objekt erzeugt, das zusätzlich Informationen zum Gast und Hotel enthält. 
Die Objekte werden in einer Liste gesammelt und über return zurückgegeben.

- Nutzung im Notebook:
Die User Story verlangt eine Eingabe des Namens des Hotels, wessen Bewertung der Gast lesen möchte. 


## Klassendiagramm

Das Klassendiagramm wurde mit Visual Paradigm modelliert und bildet die Beziehungen zwischen den zentralen Entitäten wie Hotel, Room, Booking, Invoice und Guest ab.

Siehe model/ und beigefügtes Visual Paradigm-Diagramm im Projekt-Ordner.

## GitHub-Arbeitsweise

Wir haben regelmässige Commits durchgeführt und in klar getrennten Branches gearbeitet.Der main-Branch enthält stets eine lauffähige, getestete Version.
Die Zusammenarbeit erfolgte kollaborativ über Pull Requests und Reviews.

## Projektmeilensteine

15.03.2025: Erste Strukturierung & Setup

xx.xx.2025: Implementierung Hotel- und Zimmerfilterung

xx.xx.2025: Buchung & Invoice mit Geschäftslogik

08.06.2025: Erweiterte User Stories

xx.xx.2025: Finalisierung, Tests und Videoaufzeichnung

## Dokumentation & Projektmanagement

Unsere Dokumentation besteht aus:

- README.md (GitHub) mit Projektüberblick, Struktur, Team, User Stories, Reflexion

- Deepnote-Notebooks zur Umsetzung und Präsentation der User Stories mit erläuternden Kommentaren

- Visual Paradigm-Diagramm zur Modellierung der Klassenbeziehungen

- Projektorganisation über GitHub mit Branches, Commits, Pull Requests

Die Koordination erfolgte intern über eine geteilte To-do-Liste und regelmässige Live-Sessions, in denen wir gemeinsam am Code gearbeitet und getestet haben.
Die Dokumentation wurde in Zusammenarbeit gepflegt, wobei Sheyla die finale Formatierung sicherstellte.

Wir haben darauf geachtet, dass die Notebooks die Umsetzung der User Stories transparent und interaktiv zeigen. Jede Story wurde in einer eigenen Notebook-Sektion
implementiert, kommentiert und mit Inputs/Outputs getestet.

## Reflexion

Wir haben einige Zeit gebraucht, bis uns klar war, was genau von uns erwartet wird und wie das Projekt strukturiert sein sollte. Keines der Gruppenmitglieder hatte
einen IT-Hintergrund, weshalb wir uns zuerst ein solides Fundament in Python erarbeiten mussten. Dabei lag der Fokus auf den Grundlagen der objektorientierten
Programmierung, der Strukturierung von Modulen sowie der Datenbankintegration mit SQLite.

Durch die hilfsbereite Unterstützung der Coaches Philip und Charuta, insbesondere in einzelnen Coachings ausserhalb des Unterrichts, konnten wir unser Wissen
konsolidieren und auf die Projektanforderungen anwenden - an dieser Stelle ein grosses Dankeschön!

Darüber hinaus haben wir regelmässig externe Quellen genutzt, um unser Verständnis zu vertiefen. Besonders hilfreich waren dabei:

- Stack Overflow (https://stackoverflow.com)

- Python Tutor (https://pythontutor.com)

Ein weiteres Hilfsmittel war ChatGPT, das wir insbesondere genutzt haben, um Fehlermeldungen und Tracebacks zu analysieren, wie sie z.B. bei der Implementierung
von User Stories auftraten (z.B. AttributeError: 'NoneType' object has no attribute 'first_name'). Die Erklärungen der Ursachen solcher Fehler haben uns geholfen,
tieferes Verständnis für Codefluss, Datenfluss und Objekthandhabung in Python zu entwickeln.

Gleichzeitig hatten wir über das gesamte Projekt hinweg das Gefühl, dass die Nutzung von ChatGPT zur Codegenerierung unserer Umsetzung dem Stil und der
Struktur unseres selbst aufgebauten Codes eher geschadet hätte. Wir hatten ein klares Konzept, wie die Komponenten zusammenspielen sollten, und befürchteten,
dass generierter Code ohne Rücksicht auf unsere Architektur das Projekt unbrauchbar machen könnte. Daher haben wir ChatGPT gezielt als Fehleranalysehilfe
eingesetzt - nicht als generative Codemaschine.

Die meiste Entwicklungsarbeit fand vor Ort im Team statt. Ein Gruppenmitglied hat sich jeweils mit dem Beamer verbunden und wir haben gemeinsam an den Codezeilen
gearbeitet.

Die Umsetzung der User Stories haben wir aufgeteilt, die Tests und Validierungen jedoch wieder im Team zusammen vorgenommen. Dadurch konnten wir voneinander
lernen und direkt Feedback geben. Diese Arbeitsweise hat sich als besonders produktiv erwiesen und zu einem starken Lernerfolg beigetragen.

Ein kleiner, aber wirkungsvoller Bestandteil unserer Methodik war die Nutzung der Kommentarfunktion (#) innerhalb des Codes:
Immer wenn jemand beim Implementieren unsicher war, wurde die entsprechende Codezeile mit einem kurzen Kommentar versehen, der die Frage oder Unsicherheit markierte.
Diese Stellen haben wir dann im nächsten Teamtreffen oder Coaching gezielt aufgegriffen und gemeinsam geklärt. Diese einfache Praxis hatte einen grossen Effekt:
Sie half uns, Fragen systematisch zu sammeln, kollaborativ zu lösen und unser Verständnis nachhaltig zu stärken.

Präsentationsvideo

Entweder als Video hochladen oder mit OneDrive link? wie machen?

Vielen Dank für Ihre Aufmerksamkeit!

Gruppe B3 - Hotelreservierungssystem FHNW
