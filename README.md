# Hotelreservierungssystem - Projektdokumentation
**DeepNote Link:** [Projekt in Deepnote öffnen](https://deepnote.com/workspace/Kculjak-a051eb87-a3df-411f-b9a2-009e74128bf0/project/Hotelreservierungssystem-73ffaea6-43a7-44af-99fc-6c4a6452ebdc/notebook/3b645311dbb84339b0114fa20330d754)


## Projektübersicht

Dieses Projekt wurde im Rahmen des Moduls „Anwendungsentwicklung mit Python“ an der FHNW im Frühlingssemester 2025 entwickelt. Ziel war die schrittweise
Umsetzung eines funktionalen Hotelreservierungssystems anhand vordefinierter und erweiterter User Stories.
Der Fokus lag auf objektorientierter Programmierung (OOP), Datenbankzugriff, Modularisierung und agiler Entwicklung.

Das System erlaubt es Gästen, Hotels und Zimmer zu suchen und zu buchen. Rechnungen können generiert werden, zudem stehen Admin-Funktionalitäten 
für Hotelverwaltung zur verfügung.

Für die Planung und Organisation unseres Projekts haben wir das GitHub-Issues-System und ein Scrum Board verwendet. Dabei wurden alle Aufgaben als Issues erstellt, priorisiert und im Projektboard den Spalten "Todo", "In Progress" und "Done" zugeordnet, um den Fortschritt im Team transparent zu halten.

Die Aufgabenverteilung und kurzfristige Absprachen erfolgten regelmässig über WhatsApp, um schnelle Kommunikation zu ermöglichen und den Entwicklungsprozess effizient zu gestalten.

Zusätzlich wurden Kommentare im Code genutzt, um technische Entscheidungen zu diskutieren oder offene Fragen im Team zu klären. Dies hat uns geholfen, den Entwicklungsprozess effizient zu gestalten und unser Verständnis zu vertiefen.

Des weiteren haben wir eine physische ToDo-Liste geführt, welche wir am Schluss in GitHub für die Visualisierung übertragen haben.

- **Link zu unserem Projekt Board**: [Projekt Board öffnen](https://github.com/AEPFS2025GroupB3/Hotelreservierungssystem/issues?q=is%3Aissue%20state%3Aclosed)
- **Link zu unserem Scrum Board**: [Scrum Board öffnen](https://github.com/orgs/AEPFS2025GroupB3/projects/1)

## Präsentationsvideo

Zum Video gelangt Ihr über das Linkverzeichnis (PDF), welches wir im Moodle abgegeben haben.

## Klassendiagramm

Das Klassendiagramm wurde mit Visual Paradigm modelliert und bildet die Beziehungen zwischen den zentralen Entitäten wie Hotel, Room, Booking, Invoice Guest und Review ab.

![](/pictures/Klassendiagramm.png)

## Projektteam & Rollenverteilung

Unser Team hat die Aufgaben in zwei Bereichen aufgeteilt:

- **Fachliche Rollen:** Welche technischen Teile des Projekts hat jedes Mitglied umgesetzt ?
- **Projektrollen:** Wer ist für Qualität, Dokumentation, Codepflege und GitHub verantwortlich ?

---

#### Kerstin Culjak

**Fachlich:**
- Zuständig für die Klassen Guest und Review
- Fokus: Gästemanagement und Bewertungen
- Video Koordinatorin

**Projektrolle:**
- Quality Manager: Prüft alle Komponenten auf Korrektheit, Qualität und Einhaltung der Anforderungen.
- Achtet auf konsistente Datenstrukturen und logische Beziehungen.
- Review Checker: Verantwortlich für Code-Reviews und finale Durchsicht vor der Abgabe.
- Verantwortlich für die Umsetzung der User Stories 4, 5, 6 und 10

---

#### Lisa Wüest

**Fachlich:**
- Zuständig für die Klassen Room, Facility und RoomType
- Fokus: Zimmerverwaltung, Zimmertypen und Ausstattung

**Projektrolle:**
- Code Stylist: Achtet auf eine konsistente Code-Formatierung, klare Struktur, sprechende Methodenbezeichner und einheitlichen Stil im gesamten Team.
- Notebook Coordinator: Verantwortlich für die logische Anordnung und den Aufbau der Deepnote-Blöcke (z.B. Kapitelstruktur, Inputs/Outputs, Visualisierung).
- Verantwortlich für die Umsetzung der User Stories 8, 9 und zusätzliche Userstories Review

---

#### Sheyla Sampietro

**Fachlich:**
- Zuständig für die Klassen Address und Hotel
- Fokus: Adressverwaltung und Hoteldaten inkl. Bewertungen & Zimmer

**Projektrolle:**
- Documentation Lead: Sorgt dafür, dass alle relevanten Informationen im Deepnote-Notebook dokumentiert und sauber erklärt sind.
- Achtet auf vollständige Einleitung, User Stories, Reflexion und saubere Formatierung.
- User Story Coordinator: Verknüpft die User Stories mit der technischen Umsetzung und achtet darauf, dass alle Stories nachvollziehbar umgesetzt werden.
- Verantwortlich für die Umsetzung der User Stories 1.1 bis 1.6 und 2 bis 2.2

---

#### Andrea Petretta

**Fachlich:**
- Zuständig für die Klassen Booking und Invoice
- Fokus: Buchungsabläufe und Rechnungsstellung
- Visual Paradigm Master

**Projektrolle:**
- Milestone Planner: Achtet auf die Einhaltung von Abgabeterminen, hilft bei der Aufteilung von Teilzielen und erinnert das Team an nächste Schritte.
- Feature Integrator: Sorgt dafür, dass Buchung, Rechnung, Gäste und Zimmer sauber zusammenspielen (inkl. Übergabe an Business Logic und Notebook).
- Verantwortlich für die Umsetzung der User Stories 3.1 bis 3.3 und 7

---

Diese Rollenverteilung half uns, effizient zu arbeiten und die Projektziele strukturiert zu erreichen. Obwohl die Rollenverteilung klar definiert war, haben wir im Team stets flexibel zusammengearbeitet. Alle Teammitglieder haben sich gegenseitig unterstützt und bei Bedarf in anderen Bereichen mitgeholfen. Der regelmässige Austausch, sowohl fachlich als auch organisatorisch, war ein zentraler Bestandteil unserer Zusammenarbeit und hat wesentlich zum Projekterfolg beigetragen.

**Hinweis**:  

Im GitHub wird im Abschnitt "Contributors" eine Statistik über die Anzahl Comits & Pushes, sowie über die Anzahl geschriebener und gelöschter Zeilen geführt.
Beim Vergleich der GitHub-Aktivitäten innerhalb unseres Teams ist uns aufgefallen, dass bei der Nutzerin lisawueest nur sehr wenige Commits verzeichnet sind (8 Commits, kaum Codeänderungen).
Wir vermuten, dass hier ein technisches Problem bei der Synchronisierung mit GitHub vorliegt.

Wir möchten ausdrücklich klarstellen, dass alle Teammitglieder, inklusive Lisa , aktiv, engagiert und kontinuierlich an der Umsetzung der Projektaufgaben beteiligt waren.

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

## Umgesetzte User Stories

**Technologie hinter den User Stories**

Im folgenden Abschnitt beschreiben wir die User Stories 1 bis 10 sowie die Zusatz-User-Stories mit DB-Schemaänderung detailliert:  
Ziel, Umsetzung im Code und Nutzung im Notebook.

---

### User Story 1.1 - Hotels nach Stadt filtern

**Ziel:**  
Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort auswählen kann.

**Umsetzung im Code:**  
In dieser User Story wird eine einfache Textsuche nach Städten umgesetzt:
- **HotelManager:** Die Methode `read_hotels_by_city(city)` wird aufgerufen, um alle Hotels zu finden, deren zugehörige Adresse in der gesuchten Stadt liegt.
- Der Code nutzt die `input_valid_string(...)`-Funktion aus dem `input_helper`, um einen sauberen Städte-Input vom Benutzer entgegenzunehmen.
- Das Resultat wird durch eine SQL-Abfrage in der Datenbank erzeugt (JOIN Hotel & Address).  
- Rückgabewert ist eine Liste von `Hotel`-Objekten mit Name, Sternen und Stadt.

**Nutzung im Notebook:**  
Die Stadt wird als Input eingegeben, alle Hotels mit passender Stadt werden ausgegeben.

---

### User Story 1.2 - Filterung nach Sternebewertung

**Ziel:**  
Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.

**Umsetzung im Code:**  
- Die Methode `read_hotels_by_city_and_min_stars(city, min_stars)` in `HotelManager` filtert zusätzlich nach dem Feld `Hotel.stars`.
- Im `HotelDataAccess` wird SQL mit `WHERE stars >= ?` ergänzt, um Hotels mit mindestens der gewünschten Sternewertung zu laden.
- Die Logik basiert wieder auf einem `JOIN` zwischen Hotel- und Adresstabelle.

**Nutzung im Notebook:**  
Stadt und Mindestanzahl Sterne werden eingegeben, danach werden nur Hotels mit ≥ x Sternen in der Stadt angezeigt.

---

### User Story 1.3 - Filterung nach Gästeanzahl

**Ziel:**  
Ich möchte nur Hotels sehen, die Zimmer für meine gewünschte Gästezahl anbieten.

**Umsetzung im Code:**  
- Neben dem Stadtnamen wird die Gästeanzahl abgefragt.
- Die Methode `read_hotels_by_city_number_of_guests(city, guests)` prüft, ob die maximal erlaubte Gästeanzahl (`room_type.max_guests`) ≥ Eingabe ist.
- Die JOINs verknüpfen Hotel → Room → RoomType.

**Nutzung im Notebook:**  
User gibt Stadt und Anzahl Gäste ein, angezeigt werden nur Hotels mit mindestens einem geeigneten Zimmer.

---

### User Story 1.4 - Verfügbarkeit nach Datum filtern

**Ziel:**  
Ich möchte nur Hotels angezeigt bekommen, die in meinem gewünschten Zeitraum (Check-in / Check-out) tatsächlich noch freie Zimmer haben.

**Umsetzung im Code:**  
- Abfrage nach Stadt, Check-in- und Check-out-Datum.
- Die Methode `read_available_hotels_by_city_and_date(city, check_in, check_out)` prüft:
    - Gibt es Zimmer, die nicht gebucht sind im gewählten Zeitraum?
    - SQL mit Zeitvergleich (Overlap prüfen).
- Es erfolgt ein `LEFT JOIN` mit der Booking-Tabelle. In der `WHERE`-Klausel wird geprüft, dass entweder kein Konflikt besteht oder keine Buchung vorliegt.
- `NOT (booking.check_out_date > check_in AND booking.check_in_date < check_out)` verhindert sich überschneidende Buchungen.

**Nutzung im Notebook:**  
Nach Eingabe von Stadt, Check-in- und Check-out-Datum werden nur Hotels mit verfügbaren Zimmern angezeigt.

---

### User Story 1.5 - Kombinierte Filter anwenden

**Ziel:**  
Ich möchte mehrere Kriterien kombinieren können (z.B. Gästeanzahl, Hotelsterne, Verfügbarkeit), um gezielt zu suchen.

**Umsetzung im Code:**  
- Die Methode `read_hotels_by_criteria(city, check_in_date, check_out_date, max_guests, stars)` kombiniert alle Filterbedingungen aus 1.2 - 1.4.
- Die SQL-Abfrage kombiniert die Bedingungen:
    - Stadt = city
    - Sterne ≥ mind_stars
    - Zimmerkapazität ≥ max_guests
    - Zimmer nicht gebucht im Zeitraum (Check-In bis Check-Out)
- JOINs auf Hotel, Address, Room, RoomType, Booking

**Nutzung im Notebook:**  
Alle Filter (Stadt, Zeitraum, Mindeststerne, Gästeanzahl) können gleichzeitig eingegeben werden. Das Ergebnis ist eine gezielte Auswahl passender Hotels.

---

### User Story 1.6 - Anzeige von Hotelinfos

**Ziel:**  
Ich möchte mir zu jedem Hotel die wichtigsten Informationen anzeigen lassen: Name, Adresse, Sterne.

**Umsetzung im Code:**  
- Die Methode `get_hotel_details()` im HotelManager gibt alle Hotels zurück, inklusive verknüpfter Adresse.
- Ausgabeformat:
    Name    : ...
    Adresse : ...
    Sterne  : ...

**Nutzung im Notebook:**  
Einfacher `for`-Loop über alle Hotels mit `print(...)`, um die Infos zu zeigen.

---

### User Story 2 - Zimmerdetails anzeigen

**Ziel:**  
Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen. Dazu gehören die maximale Anzahl von Gästen, die Beschreibung, der Preis und die Ausstattung, um eine fundierte Entscheidung zu treffen.

**Umsetzung im Code:**  
- Die Methode `read_rooms_with_facilities_by_hotel_and_date(hotel_id, check_in_date, check_out_date)` aus dem `HotelManager` überprüft, welche Zimmer in einem bestimmten Zeitraum in einem Hotel noch frei sind.
- In dieser Methode wird `RoomDataAccess.read_available_rooms_with_facilities(...)` aufgerufen, um die verfügbaren Räume zu lesen.
- Die Methode führt JOINs mit den Tabellen `Room`, `RoomType` und `Facility` aus, um alle Informationen über ein Zimmer samt Typ und Ausstattung zu laden.
- Pro Raum wird ein `Room`-Objekt erstellt, das ein `RoomType`-Objekt (mit Beschreibung und max. Anzahl Gäste) sowie eine Liste von `Facility`-Objekten enthält.

**Nutzung im Notebook:**  
Nach Auswahl eines Hotels werden alle zugehörigen Zimmer mit ihren Eigenschaften angezeigt.

---

### User Story 2.1 - Zimmerdetails anzeigen

**Ziel:**  
Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis (berechnet anhand der Aufenthaltsdauer).

**Umsetzung im Code:**  
Die Details pro Zimmer werden über die Daten aus der Datenbank geladen:
- `Room`-Objekte enthalten `price_per_night`, `room_number` und die Beziehung zu `RoomType` und `Facility`.
- Der `RoomType` enthält die Beschreibung und die max. Gästezahl.
- Die Ausstattung wird über eine Many-to-Many-Verknüpfung zwischen Room und Facility geladen.
- Pro Raum wird ein `Room`-Objekt erstellt, das ein `RoomType`-Objekt (mit Beschreibung und max. Anzahl Gäste) sowie eine Liste von `Facility`-Objekten enthält.

**Nutzung im Notebook:**  
Nach Auswahl eines Hotels werden alle zugehörigen Zimmer mit ihren Eigenschaften angezeigt. Hier werden noch zusätzlich die Facilities angezeigt.

---

### User Story 2.2 - Nur verfügbare Zimmer anzeigen

**Ziel:**  
Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von - bis) spezifiziert habe.

**Umsetzung im Code:**  
- Die Methode `read_rooms_with_facilities_by_hotel_and_date` filtert über einen SQL-Query alle Zimmer, bei denen keine überschneidende Buchung mit dem gewünschten Zeitraum existiert.
- Die Logik prüft via `NOT EXISTS`, ob für ein Zimmer in der `Booking`-Tabelle ein überschneidender Zeitraum existiert.
- Die Aufenthaltsdauer wird berechnet aus dem Check-in und Check-out Datum und zur Berechnung des Gesamtpreises verwendet (duration * price_per_night).

**Nutzung im Notebook:**  
Eingabe von `Hotel_ID`, `Check-in` und `Check-out` Datum. Nur Zimmer, die nicht gebucht sind in diesem Zeitraum, werden angezeigt. Ausserdem wird hier zusätzlich der Gesamtpreis für die Dauer (Check-Out - Check-In) berechnet. Die Auswahl wird dadurch übersichtlich und relevant für die Buchung.

---

### User Story 3.1 - Hotel hinzufügen

**Ziel:**  
Als Admin möchte ich neue Hotels zum System hinzufügen.

**Umsetzung im Code:**  
Im `AdminManager` wurde die Methode `create_new_hotel(...)` hinzugefügt, die drei Parameter `name`, `stars` und ein `Address`-Objekt verlangt. 
In der `HotelDataAccess` erfolg die Speicherung in der Datenbank. Es wird ein SQL-Insert Statement auf die Adresse ausgeführt, um die Adresse des Hotels in der Datenbank zu speichern.
Die Datenbank liefert die `address_id` der neu generierten Adresse zurück. Danach wird ein weiteres SQL-Insert Statement auf das Hotel ausgeführt, wobei der Hotelname, die Sterne und die address_id gespeichert werden.
Auch hier gibt die Datenbank die `hotel_id` des neu generierten Hotels zurück.

**Nutzung im Notebook:**  
Die User Stroy verlangt die Eingabe der Strasse, der Postleitzahl, der Stadt, sowie des Namens vom Hotel und die Anzahl Sterne.

---

### User Story 3.2 - Hotel entfernen

**Ziel:**  
Als Admin möchte ich ein Hotel aus dem System löschen.

**Umsetzung im Code:**  
Im `AdminManager` wurden zwei Methoden implementiert. Einmal `get_all_hotels(...)` um in der UI dem User eine Liste aller verfügbaren Hotels anzuzeigen und die Methode `delete_hotel(...)`. 
Die Methode `delete_hotel(...)` verlangt den Parameter `hotel_id`. Im `HotelDataAccess` wird dann die gleichnamige Methode aufgerufen und es wird ein SQL-Delete auf das Hotel ausgeführt. Die Mehthode erwartet ein `Hotel`-Objekt, daraus wir die `hotel_id` genommen, des Hotels das entfernt werden soll.
Mit `self.execute(...)` wird das Statement ausgeführt und das Hotel dauerhaft aus der Datenbank entfernt. 

**Nutzung im Notebook:**  
Es wird eine Liste alles Hotels ausgeben mit ihren Details, die momentan in der Datenbank hinterlegt sind. Danach wird der User aufgefordert, die Id des Hotels einzugeben, das gelöscht werden soll.
Nach der Eingabe der Id wird noch einmal nachgefragt, ob das Hotel XY wirklich gelöscht werden soll. Wenn der User "Y" eingibt, wird das Hotel endgültig gelöscht. 

---

### User Story 3.3 - Hotelinformationen aktualisieren

**Ziel:**  
Der Admin möchte bestehende Hoteldaten wie Name, Sterne oder Adresse aktualisieren, um das System auf dem aktuellen Stand zu halten.

**Umsetzung im Code:**
Die Methode update_hotel(hotel: Hotel) wurde in der Klasse HotelManager ergänzt und ruft intern hotel_data_access.update_hotel(...) auf.
Damit bleibt die Trennung der Schichten (UI → Business Logic → Data Access) erhalten. Die Eingaben erfolgen über die Funktion input_valid_int bzw. input_valid_string in input_helper.py.

Im Notebook wird nach Auswahl der Hotel-ID ein Menü angezeigt, in dem ausgewählt werden kann, ob der Name, die Sternebewertung oder die Adresse geändert werden soll.
Je nach Auswahl werden gezielt neue Werte abgefragt und das Objekt aktualisiert. Nach der Änderung wird die Methode update_hotel(...) aufgerufen.

**Nutzung im Notebook:**  
Hotelliste mit ID, Name, Sterne, Adresse wird angezeigt.
Admin gibt die Hotel-ID ein, die bearbeitet werden soll.

Auswahlmenü mit 3 Optionen:
- Hotelname ändern
- Sternebewertung ändern
- Adresse ändern

Neue Werte werden eingegeben.
Hotel wird aktualisiert und Erfolgsmeldung ausgegeben.
Falls die ID ungültig ist, erscheint eine entsprechende Fehlermeldung.
___

### User Story 4 - Buchung erstellen

**Ziel:**  
Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.

**Umsetzung im Code:**  
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

**Ziel:**  
Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

**Umsetzung im Code:**  
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

**Ziel:**  
Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hinweis: Sorgt dafür, dass auch die zugehörige Rechnung entsprechend aktualisiert wird.

**Umsetzung im Code:**  
Die Umsetzung dieser User Story erfolgt durch die Zusammenarbeit von BookingManager, BookingDataAccess und InvoiceDataAccess.

**1.	BookingManager**  
Die Methode `cancel_booking(booking_id)` übernimmt die Hauptlogik für die Stornierung:
-	Sie ruft intern `update_booking_status(...)` auf, um den Stornierungsstatus der Buchung auf True zu setzen.
-	Anschliessend wird geprüft, ob eine Rechnung zur Buchung existiert.
-	Falls eine Rechnung vorhanden ist, wird der Rechnungsstatus über `update_invoice_status(...)` auf „cancelled“ gesetzt.

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

---

### User Story 7 - Saisonale Preisgestaltung

**Ziel:**  
Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.

**Umsetzung im Code:**  
Für diese User Story haben wir einen `PriceManager` erstellt, mit dem Ziel, saisonale Preisanpassungen bei Hotelzimmern zu berücksichtigen.
Wir haben zunächst eine Methode `get_seasonal_factor(...)` definiert, die den Parameter `check_in_date` verlangt. Für die Hochsaison, Buchungen im Juli und August, haben wir ein Faktor von 1.2 verwendet.
Für die Nebensaison, Januar, Februar und November, haben wir den Faktor 0.8 definiert. In alles anderen Monaten bleibt der Preis unverändert, Faktor 1.0.
Die Methode `calculate_dynamic_price(...)` multipliziert den Basispreis pro Nacht mit dem `seasonal_factor`.

Zusätzlich wurde in der `RoomDataAccess` die Methode `get_all_rooms(...)` verwendet. Diese lädt Zimmerdaten inklusive der Zimmerart aus der Datenbank mit einem einfachen JOIN über `type_id`.
Für jedes Ergebnis wird ein `Room`-Objekt erstellt. Da zu diesem Zeitpunkt kein Check-in-Datum bekannt ist, wir der seasonal_factor von 1.0 gesetzt.

**Nutzung im Notebook:**  
Im Notebook wird der dynamische Zimmerpreis auf Grundlage des Check-in-Datums berechnet.
Zuerst werden alle Zimmer mit ID und Preis pro Nacht angezeigt.
Danach wählt der Nutzer ein Zimmer aus und gibt ein Check-in-Datum ein.
Je nach Monat wird ein Saisonfaktor bestimmt (z.B. 1.2 im Juli oder August).
Der Preis wird damit multipliziert und angezeigt.

___

### User Story 8 - Alle Buchungen anzeigen

**Ziel:**  
Als Admin möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht über alle bestehenden Buchungen erhalten.

**Umsetzung im Code:**  
Wir haben eine Methode mit dem Namen `read_bookings_by_hotel(...)` im Booking_Manager definiert, die den Parameter `hotel_id` verlangt. 
In der Booking Data Access Layer wird mit Hilfe eines SQL-Queries eine Abfrage auf folgenden Tabellen durchgeführt: `Booking`, `Room`, `Room_Type`, `Hotel`, `Address` und `Guest`.

Die JOINS erfolgen über die gemeinsamen IDs: 
- `room_id` = um die Verbindung zwischen `Booking` und `Room` herzustellen
- `type_id` = um die Verbidung zwischen `Room` und `Room_Type` herzustellen
- `hotel_id` = um die Verbidung zwischen `Room` und `Hotel` herzustellen
- `address_id` = um die jeweilige Adresse von `Gast` und `Hotel` zu ermitteln
- `guest_id` = um die Verbindung zwischen `Gast` und `Booking` herzustellen

Mit WHERE wird dann die `hotel_id` abgefragt, damit nur die Buchungen für das gewünschte Hotel angezeigt werden. 

Mit `fetchall` werden alle passenden Ergebnisse aus der DB geladen. Für jede Zeile der Abfrage wird ein `Booking`-Objekt erzeugt, dass die Objekte `Hotel`(mit `Address`), `Guest`(mit `Address`) und `Room`(mit `Room_Type` und `Hotel`) enthält. 

**Nutzung im Notebook:**  
Die User Story erfordert die Eingabe der hotel_id. Wir haben es gezielt so umgesetzt, dass der Admin die hotel_id des Hotels eingeben muss, für welches er die bereits erfassten Bookings anschauen möchte.
Dies bezwecket, dass eine übersichtliche Liste generiert wird und die nur für das jeweilige Hotel relevanten Bookings angezeigt werden.
___
### User Story 9 - Zimmerliste mit Ausstattung anzeigen

**Ziel:**  
Der Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.

**Umsetzung im Code:**  
Im `Room_Manager` haben wir die Methode `read_room_with_facilities(...)` erstellt. Die Methode ruft in der `RoomDataAccess` die gleichnamige Methode auf.
Dort wird mit Hilfe eines SQL-Statements eine Abfrage auf folgenden Tabellen ausgeführt: `Room`, `Room_Type`, `Room_Facilities`, `Facilities`.

Die JOINS erfolgen über die Ids:  
- `room_id` = um die Verbindung zwischen `Room` und `Room_Facilities` herzustellen
- `type_id` = um die Verbidung zwischen `Room` und `Room_Type` herzustellen
- `facility_id` = Verbindung zwischen `Room_Facilities` und `Facilities`

Wir haben LEFT JOINS verwendet, um sicherzustellen, dass auch Zimmer ohne Ausstattung im Ergebnis enthalten sind. Dadurch gehen keine Rooms verloren.
Zudem verwenden wir GROUP_CONCAT um alle Facilities pro Room (können mehrere sein) in einen kommagetrennten String zusammenzufassen. Dadurch gibt es pro Room nur eine Zeile im Resultat.
Mit `fetchall` werden alle Ergebnisse abgerufen. Für jede Zeile wird anschliessend ein Dictionary pro Room erstellt. Bei Facilities wird durch Split aus dem GROUP-CONCAT-String eine Liste von Strings gemacht.
Falls keine Facilities vorhanden sind, wird eine leere Liste zurückgegeben. 

**Nutzung im Notebook:**  
Die Methode wird aufgerufen und liefert eine Liste von Dictionaries. In der for loop wird für jedes Room-Dictionary Zimmernummer, Zimmertyp, maximale Gästeanzahl und preis pro Nacht ausgegeben. 
Wenn Facilities vorhanden sind, wird die Liste als kommaseparierte Liste ausgegeben. Ansonsten wird ausgegeben, dass keine Facilities vorhanden sind.

___
### User Story 10 - Stammdaten verwalten

**Ziel:**  
Als Admin möchte ich in der Lage sein, Stammdaten wie Zimmertypen, Einrichtungen und Preise in Echtzeit zu aktualisieren, damit das System jederzeit mit aktuellen Informationen arbeitet.

**Umsetzung im Code:**  
Die Umsetzung dieser User Story erfolgt durch die Zusammenarbeit von `AdminManager`, `RoomTypeDataAccess`, `FacilityDataAccess` und `RoomDataAccess`.


**1. AdminManager**  
Der AdminManager bildet die zentrale Schicht zur Verwaltung vonStammdaten. Er bietet Methoden an für:

**Einrichtung (Facility):**  
`create_facility(name)`: Fügt eine neue Ausstattung hinzu.
`update_facility(facility_id, new_name)`: Benennt eine bestehende Ausstattung um.
`delete_facility(facility_id)`: Löscht eine Ausstattung aus dem System.
Hilfsmethoden wie `facility_name_exists(...)` und `get_facility_name_by_id(...)` sorgen für Validierung.

**Zimmertyp (RoomType):**  
`create_room_type(description, max_guests)`: Erstellt einen neuen Zimmertyp.
`update_room_type(...)`: Aktualisiert Beschreibung und maximale Gästezahl eines bestehenden Typs.
`delete_room_type(...)`: Löscht einen Zimmertyp.

**Zimmerpreis (Room):**  
`update_room_price(room_id, new_price)`: Ändert den Preis eines Zimmers.

**2. FacilityDataAccess**  
Diese Klasse ist für den direkten Zugriff auf die Facilities-Tabelle zuständig:
- `create_facility(...)`: Führt ein SQL-Insert aus.
- `update_facility_name(...)`: Aktualisiert den Namen einer Ausstattung.
- `delete_facility(...)`: Entfernt eine Ausstattung aus der Datenbank.
- `get_all_facilities()`: Lädt alle existierenden Ausstattungen zur Anzeige oder Validierung.

**3. RoomDataAccess**
Wird verwendet, um den Preis einzelner Zimmer zu aktualisieren:
`update_room_price(room_id, new_price)`: SQL-Update für den Zimmerpreis.

**Nutzung im Notebook:**  
1. Das Admin-Menü bietet folgende Optionen:
    - Neue Ausstattung erstellen oder bestehende umbenennen/löschen
    - Neue Raum Typ anlegen oder bearbeiten
    - Raumpreise aktualisieren
    - Saisonale Faktoren einsehen (Lesefunktion)
2.	Je nach Auswahl werden die entsprechenden Eingaben abgefragt (z. B. Name, ID, Beschreibung, Preis).
3.	Der AdminManager ruft intern die passenden Methoden in den DataAccess-Klassen auf.
4.	Erfolgreiche Änderungen werden direkt bestätigt.

---

## User Stories mit DB-Schemaänderung

Diese User Storys erfordern eine Erweiterung des bestehenden Datenbankschemas, die nach der Umsetzung der minimalen User Storys umgesetzt wurde. 
Wir haben uns für die User Storys entschieden, die eine weitere Klasse Reviews erfordern. Dazu haben wir eine Tabelle Review mit Hilfe von SQLite Online ergänzt und um die Codes zu testen, zusätzlich auch noch ein Beispieldatensatz hinzugefügt.

---

### User Story 3

**Ziel:**  
Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.

**Umsetzung im Code:**  
Im `ReviewManager` haben wir die Methode `add_review(...)` definiert. Diese Methode erwartet die Parameter `guest_id`, `hotel_id`, `rating`, `comment` und `review_date`. 
Mit Hilfe eines SQL-Insert-Statements ergänzen wir die Werte in die Datenbank. Das Einfügen der Daten wird anschliessend mit self.execute ausgeführt.

**Nutzung im Notebook:**  
Diese User Story verlangt die Eingabe der `guest_id` und `hotel_id`, einer Bewertung zwischen 1 bis 5, eines Kommentars sowie des Datums. Die Eingabe der `guest_id` und `hotel_id` scheint auf den ersten Blick für den Gast unmöglich und komisch.
Diese Informationen sind aber notwendig und werden auf der Rechnung ausgewiesen. Sie verhindern, dass das Hotel Bewertungen von Kunden erhält die nicht im Hotel waren. 

___

### User Story 4

**Ziel:**  
Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

**Umsetzung im Code:**  
Im `ReviewManager` haben wir eine Methode `get_reviews_by_hotel(...)` erstellt, die den Hotelnamen als Parameter verlangt. Diese Methode ruft in der Data Access Layer die gleichnamige Methode in der `ReviewDataAccess` Klasse auf.
Dort wird mit Hilfe eines SQL-Queries eine Abfrage auf folgenden Tabellen durchgeführt: `Review`, `Guest`, `Address` und `Hotel`

Die JOINS erfolgen über die gemeinsamen IDs:  
- `guest_id` = um die Verbindung zwischen `Review` und `Guest` herzustellen
- `address_id` = um die jeweilige Addresse von `Guest` und `Hotel` zu ermitteln 
- `hotel_id` = um die Verbindung zwischen `Review` und `Hotel` herzustellen

Mit WHERE wird der Hotelname abgefragt(case-insensitive). 
Mit `fetchall` werden alle passenden Ergebnisse der SQL-Abfrage aus der Datenbank geladen. Daraus wird für jede Zeile ein `Review`-Objekt erzeugt, das zusätzlich Informationen zum Gast und Hotel enthält. 
Die Objekte werden in einer Liste gesammelt und über return zurückgegeben.

**Nutzung im Notebook:**
Die User Story verlangt eine Eingabe des Namens des Hotels, wessen Bewertung der Gast lesen möchte. 

---

## Reflexion

Wir haben einige Zeit gebraucht, bis uns klar war, was genau von uns erwartet wird und wie das Projekt strukturiert sein sollte. Keines der Gruppenmitglieder hat
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
eingesetzt und nicht als generative Codemaschine.

Die meiste Entwicklungsarbeit fand vor Ort im Team statt. Ein Gruppenmitglied hat sich jeweils mit dem Beamer verbunden und wir haben gemeinsam an den Codezeilen
gearbeitet.

Die Umsetzung der User Stories haben wir aufgeteilt, die Tests und Validierungen jedoch wieder im Team zusammen vorgenommen. Dadurch konnten wir voneinander lernen und direkt Feedback geben. Diese Arbeitsweise hat sich als besonders produktiv erwiesen und zu einem starken Lernerfolg beigetragen.

Ein kleiner, aber wirkungsvoller Bestandteil unserer Methodik war die Nutzung der Kommentarfunktion (#) innerhalb des Codes:

Immer wenn jemand beim Implementieren unsicher war, wurde die entsprechende Codezeile mit einem kurzen Kommentar versehen, der die Frage oder Unsicherheit markierte.
Diese Stellen haben wir dann im nächsten Teamtreffen oder Coaching gezielt aufgegriffen und gemeinsam geklärt. Diese einfache Praxis hatte einen grossen Effekt. Sie half uns, Fragen systematisch zu sammeln, kollaborativ zu lösen und unser Verständnis über das ganze Semester zu stärken.

Die Komemntarfunktion wurde ebenfalls genutzt, um die Gedankengänge im Codeaufbau für die Gruppenmitglieder verstädnlicher zu gestalten.

**Super, Sie sind am Ende des README angelangt! Viel Spass bei der Ausführung.**

Gruppe B3 - Hotelreservierungssystem FHNW
