# Hotelreservierungssystem - Projektdokumentation


## Projektübersicht

Dieses Projekt wurde im Rahmen des Moduls „Anwendungsentwicklung mit Python“ an der FHNW im Frühlingssemester 2025 entwickelt. Ziel war die schrittweise
Umsetzung eines funktionalen Hotelreservierungssystems anhand vordefinierter und erweiterter User Stories.
Der Fokus lag auf objektorientierter Programmierung (OOP), Datenbankzugriff, Modularisierung und agiler Entwicklung.

Das System erlaubt es Gästen, Hotels und Zimmer zu suchen und zu buchen, Rechnungen zu generieren sowie Admin-Funktionalitäten für Hotelverwaltung bereitzustellen.


## Projektteam & Rollenverteilung

Unser Team hat die Aufgaben in zwei Bereichen aufgeteilt:

Fachliche Rollen: Welche technischen Teile des Projekts hat jedes Mitglied umgesetzt

Projektrollen: Wer ist für Qualität, Dokumentation, Codepflege und GitHub verantwortlich

**Kerstin Culjak**

Fachlich:

- Zuständig für die Klassen Guest und Review
- Fokus: Gästemanagement und Bewertungen

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

**Andrea Petretta*

Fachlich:

- Zuständig für die Klassen Booking und Invoice
- Fokus: Buchungsabläufe und Rechnungsstellung

Projektrolle:

- Milestone Planner: Achtet auf die Einhaltung von Abgabeterminen, hilft bei der Aufteilung von Teilzielen und erinnert das Team an nächste Schritte.
- Feature Integrator: Sorgt dafür, dass Buchung, Rechnung, Gäste und Zimmer sauber zusammenspielen (inkl. Übergabe an Business Logic und Notebook).

Diese Rollenverteilung half uns, effizient zu arbeiten und die Projektziele strukturiert zu erreichen.

## Projektstruktur

Unser Projekt folgt einer modularen Architektur, bei der jede Schicht eine klar definierte Verantwortung übernimmt.
Die Kommunikation erfolgt über Python-Importezwischen den Modulen.

Hotelreservierungssystem/
│
├── database/          # SQLite-Datenbankdatei (hotel_reservation_sample.db)
├── model/             # Klassen für Datenmodelle wie Hotel, Room, Booking etc.
├── data_access/       # Data Access Layer: SQL-Zugriff (CRUD)
├── business_logic/    # Geschäftslogik: Preisberechnung, Buchung, Rechnung usw.
├── ui/                # Eingabevalidierung & User Interaction via Notebooks
└── notebooks/         # Deepnote-Notebooks zur Ausführung der Use Cases

## Verwendete Technologien

Python 3.10+

SQLite als relationale Datenbank

Deepnote für interaktive Entwicklung und Visualisierung

Git / GitHub für Versionierung, Branching und Dokumentation

Objektorientierte Programmierung (OOP)

Visual Paradigm zur Modellierung des Klassendiagramms

## Getting Started

Projekt klonen:

git clone https://github.com/AEPFS2025GroupB3/Hotelreservierungssystem.git

Deepnote-Projekt öffnen (alternativ lokal mit PyCharm starten)
Arbeitsverzeichnis in Deepnote setzen:
Rechtsklick auf das Notebook → Set Working Directory → /Hotelreservierungssystem
Notebook öffnen:
Hotelreservierungssystem.ipynb im Ordner deepnote/GroupB3/
Hinweis: Die verwendete SQLite-Datenbank befindet sich im Ordner database/. Die Originaldatei heisst hotel_reservation_sample.db.
Für die Arbeit im Notebook empfehlen wir, eine Kopie mit dem Namen working_db.db zu verwenden, damit die Ausgangsdatenbank nicht verändert wird.

## Umgesetzte User Stories

**Technolige hiner den User Stories**

Im Folgenden beschreiben wir die User Stories 1 bis 10 detailliert: Ziel, Funktionsweise und Nutzung im Notebook.

** User Story 1.1 - Hotels nach Stadt filtern **

- Ziel:
Der Gast möchte alle Hotels in einer bestimmten Stadt durchsuchen, um seinen bevorzugten Standort auszuwählen.

- Umsetzung im Code:
Die Logik befindet sich in hotel_data_access.py und hotel_manager.py. Mithilfe eines SQL-Statements wird die Hotel-Tabelle nach dem Stadt-Feld gefiltert.

- Nutzung im Notebook:
Notebook öffnen: 01_Suche_und_Filterung.ipynb XXXXXXXXX ANSCHAUEN XXXXXXXXXXX

Stadtname (z.B. "Zürich") eingeben 

Ausgabe: Liste der Hotels in dieser Stadt

** User Story 1.2 - Filterung nach Sternebewertung **

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

-Ziel:
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

**User Story 3.2 - Hotel entfernen*

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

**User Story 4 - Buchung erstellen**

- Ziel:
Der Gast möchte ein Zimmer buchen und seine Daten erfassen, um die Reservierung abzuschliessen.

- Umsetzung im Code:
Die Buchungsdaten werden über die booking_manager.py verarbeitet, validiert und an booking_data_access.py zur Speicherung in die Datenbank übergeben.
Zusätzlich wird geprüft, ob das gewählte Zimmer verfügbar ist.

- Nutzung im Notebook:
Eingabe: Gästeinformationen, Zimmer-ID, Check-in/out-Daten

Ausgabe: Bestätigung mit Buchungsnummer

**User Story 5 - Rechnung generieren**

- Ziel:
Der Gast möchte nach dem Aufenthalt eine korrekte Rechnung erhalten.

- Umsetzung im Code:
Die Rechnung wird automatisch nach Buchung erstellt. invoice_manager.py berechnet den Gesamtbetrag inkl. saisonalem Aufschlag und speichert das Ergebnis
via invoice_data_access.py in der Tabelle invoice.

- Nutzung im Notebook:
Nach erfolgreicher Buchung: Rechnung wird direkt angezeigt oder exportiert

**User Story 6 - Buchung stornieren**

- Ziel:
Der Gast möchte eine Buchung stornieren und keine Kosten tragen.

- Umsetzung im Code:
Die Stornierung wird in booking_manager.py verarbeitet, indem der Buchungsstatus auf „cancelled“ gesetzt wird. Gleichzeitig wird die Rechnung in invoice_data_access.py
angepasst oder gelöscht.

- Nutzung im Notebook:
Buchungsnummer eingeben → Status = „cancelled“, Rechnung wird storniert

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
Der Admin möchte eine Übersicht über alle bestehenden Buchungen erhalten.

- Umsetzung im Code:
Die Funktion get_all_bookings() in booking_data_access.py ruft alle Einträge aus der Datenbank ab. Diese werden im Notebook formatiert dargestellt.

- Nutzung im Notebook:
Ausführung der Admin-Abfrage → Tabelle mit allen Buchungen

**User Story 9 - Zimmerliste mit Ausstattung anzeigen**

- Ziel:
Der Admin möchte Zimmer nach Ausstattung sortiert sehen, um gezielte Werbung oder Managemententscheidungen zu treffen.

- Umsetzung im Code:
room_data_access.py kombiniert die room- und facility-Tabellen. Die Daten werden nach Hotel und Ausstattung gruppiert ausgegeben.

- Nutzung im Notebook:
Hotel-ID eingeben → Liste der Zimmer + zugehörige Ausstattung

**User Story 10 - Stammdaten verwalten**

- Ziel:
Der Admin möchte Zimmertypen, Ausstattungen und Preise verwalten können.

- Umsetzung im Code:
Die Stammdaten befinden sich in eigenen Tabellen (room_type, facility). Änderungen erfolgen über entsprechende Data Access Layer mit CRUD-Methoden.

- Nutzung im Notebook:
Neue Ausstattung hinzufügen oder bestehende Typen bearbeiten → Änderungen sofort in der Zimmeranzeige wirksam



## Erweiterte User Stories

Diese User Stories erfordern eine Änderung des Datenbankschemas und werdemn im weiteren Verlauf ergänzt.

**User Story 1**

- Ziel:
sdöfjlsfgsfgsfdg

- Umsetzung im Code:
sdflsjflskdjfnalsdf

- Nutzung im Notebook:
lsdkfjsdfsadflsadf

**User Story 2**

- Ziel:
sdöfjlsfgsfgsfdg

- Umsetzung im Code:
sdflsjflskdjfnalsdf

- Nutzung im Notebook:
lsdkfjsdfsadflsadf

**User Story 3**

- Ziel:
sdöfjlsfgsfgsfdg

- Umsetzung im Code:
sdflsjflskdjfnalsdf

- Nutzung im Notebook:
lsdkfjsdfsadflsadf

** Klassendiagramm

Das Klassendiagramm wurde mit Visual Paradigm modelliert und bildet die Beziehungen zwischen den zentralen Entitäten wie Hotel, Room, Booking, Invoice und Guest ab.

Siehe model/ und beigefügtes Visual Paradigm-Diagramm im Projekt-Ordner.

## GitHub-Arbeitsweise

Wir haben regelmässige Commits durchgeführt und in klar getrennten Branches gearbeitet.Der main-Branch enthält stets eine lauffähige, getestete Version.
Die Zusammenarbeit erfolgte kollaborativ über Pull Requests und Reviews.

## Projektmeilensteine

15.03.2025: Erste Strukturierung & Setup

05.04.2025: Implementierung Hotel- und Zimmerfilterung

20.04.2025: Buchung & Invoice mit Geschäftslogik

05.05.2025: Erweiterte User Stories (Bewertung, Treuepunkte)

01.06.2025: Finalisierung, Tests und Videoaufzeichnung

##Dokumentation & Projektmanagement

Unsere Dokumentation besteht aus:

- README.md (GitHub) mit Projektüberblick, Struktur, Team, User Stories, Reflexion

- Deepnote-Notebooks zur Umsetzung und Präsentation der User Stories mit erläuternden Kommentaren

- Visual Paradigm-Diagramm zur Modellierung der Klassenbeziehungen

- Projektorganisation über GitHub mit Branches, Commits, Pull Requests

Die Koordination erfolgte intern über eine geteilte To-do-Liste und regelmässige Live-Sessions, in denen wir gemeinsam am Code gearbeitet und getestet haben.
Die Dokumentation wurde in Zusammenarbeit gepflegt, wobei Sheyla die finale Formatierung sicherstellte.

Wir haben darauf geachtet, dass die Notebooks die Umsetzung der User Stories transparent und interaktiv zeigen. Jede Story wurde in einer eigenen Notebook-Sektion
implementiert, kommentiert und mit Inputs/Outputs getestet.

##Reflexion

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

Entweder als Video hochladen oder mit OneDrive link?

Vielen Dank für Ihre Aufmerksamkeit!

Gruppe B3 - Hotelreservierungssystem FHNW