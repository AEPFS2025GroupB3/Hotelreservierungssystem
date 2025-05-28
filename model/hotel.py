from __future__ import annotations

from model.address import Address

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.address import Address 
    from model.room import Room
    from model.room_type import RoomType
    from model.review import Review

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address, room_type: RoomType):
        #Validierung: ID muss existieren und eine ganze Zahl sein
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")

        #Name muss übergeben werden und ein String sein
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")

        #Sterne müssen zwischen 1 und 5 liegen
        if not stars:
            raise ValueError("stars is required")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        if not (1 <= stars <= 5):
            raise ValueError("stars must be between 1 and 5")
        
        #Die Adresse muss ein Objekt der Klasse Address sein
        if not address:
            raise ValueError("address is required")
        if not isinstance(address, Address):
            raise ValueError("address must be an Address object")

        #Private Attribute mit doppeltem Unterstrich für Kapselung
        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address: Address = address
        self.__room_type: RoomType = room_type

        self.__rooms = []     # Liste von Room-Objekten
        self.__reviews = []   # Liste von Review-Objekten

    #Hotel-ID bleibt konstant, daher nur ein Getter
    @property
    def hotel_id(self):
        return self.__hotel_id

    #Getter und Setter für Name
    @property
    def name(self):
        return self.__name

    @property
    def room_type(self):
        return self.__room_type

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name is required")
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self.__name = value

    # Getter und Setter für Sternebewertung
    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        if value is None:
            raise ValueError("stars is required")
        if not isinstance(value, int):
            raise ValueError("stars must be an integer")
        if not (1 <= value <= 5):
            raise ValueError("stars must be between 1 and 5")
        self.__stars = value
    
    #Getter für die Adresse (keine Setter, da die Adresse fix bleibt)
    @property
    def address(self):
        return self.__address
    

    #Methode für Ausgabe von Hoteldetails
    def get_hotel_details(self):
        return f"Hotel ID: {self.__hotel_id}, Name: {self.__name}, Address: {self.__address.get_full_address()}, Stars: {self.__stars}"

    #Damit print(hotel) direkt get_hotel_details() zurückgibt
    def __str__(self):
        return self.get_hotel_details()


    # Zimmerverwaltung

    #Zimmer hinzufügen V1 mit ID
    def add_room(self, room: Room): #Validierung des Parameters hinzufügen
        room._Room__hotel_id = self.__hotel_id #Wir greifen absichtlich auf gemangelte Attribute zu
        if room not in self.__rooms:
            #Room wird zur internen Liste hinzugefügt
            self.__rooms.append(room)

    #Zimmer hinzufügen V2 mit Objekt
    def add_room(self, room: Room):
        if not isinstance(room, Room):
            raise ValueError("room must be a Room object")
        self.__rooms.append(room)
        

    #Zimmer löschen
    def remove_room(self, room: Room) -> None:
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room in self.__rooms:
            self.__rooms.remove(room)
            room.hotel = None

    #Zugriff auf die Raumliste --> .copy gibt eine Kopie zurück, damit niemand das Original verändern kann
    def get_rooms(self) -> list:
        return self.__rooms.copy()


    #Bewertungen
    def add_review(self, review: Review):
        # Bewertungsobjekt (z. B. von einem Gast) hinzufügen
        if not isinstance(review, Review):
            raise ValueError("review must be a Review object")
        self.__reviews.append(review)

    def get_reviews(self) -> list:
        # Gibt alle Bewertungen zurück (z. B. für Anzeige im UI)
        return self.__reviews.copy()

    def get_average_rating(self) -> float:
        # Gibt den Durchschnitt aller Bewertungen zurück (für Sortierung, Filter etc.)
        if not self.__reviews:
            return 0.0
        total = sum(r.rating for r in self.__reviews)
        return round(total / len(self.__reviews), 2)

    # Ausgabe der Hoteldetails inkl. Bewertung

    def get_hotel_details_with_review_rating(self):
        if not self.__reviews:
            return f"{self.name}, {self.address.get_full_address()}, {self.stars}, Noch keine Bewertungen"
        return f"{self.name}, {self.address.get_full_address()}, {self.stars}, Durchschnittliche Bewertung: {round(self.get_average_rating(), 2)}/5 bei {len(self.__reviews)} Bewertungen"
        #len = Anzahl