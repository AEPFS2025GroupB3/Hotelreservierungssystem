from datetime import date  #Importiert den Typ "date" für das Review-Datum
from model.address import Address 
from model.room_type import RoomType
from model.room import Room
from model.review import Review

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address):
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
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        if stars < 1 or stars > 5:
            raise ValueError("stars must be between 1 and 5")
        
        #Die Adresse muss ein Objekt der Klasse Address sein
        if not isinstance(address, Address):
            raise ValueError("address must be an Address object")

        #Private Attribute mit doppeltem Unterstrich für Kapselung
        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address: Address = address

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

    @name.setter
    def name(self, value):
        #Sicherstellen, dass der neue Name ein nicht-leerer String ist
        if not value or not isinstance(value, str):
            raise ValueError("name must be a non-empty string")
        self.__name = value

    # Getter und Setter für Sternebewertung
    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        #Sterne dürfen nur zwischen 1 und 5 liegen
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("stars must be an integer between 1 and 5")
        self.__stars = value
    
    #Getter für die Adresse (keine Setter, da die Adresse meist fix bleibt)
    @property
    def address(self):
        return self.__address
    
    #Methode für strukturierte Ausgabe von Hoteldetails
    def get_hotel_details(self):
        return f"Hotel ID: {self.__hotel_id}, Name: {self.__name}, Address: {self.__address.get_full_address()}, Stars: {self.__stars}"

    #Damit print(hotel) direkt get_hotel_details() zurückgibt
    def __str__(self):
        return self.get_hotel_details()

    # Room-Verwaltung

    #Raum hinzufügen
    def add_room(self, room_no: str, price_per_night: float, room_type: RoomType, seasonal_factor: float):
        new_id = len(self.__rooms) + 1 #Room_id wird automatisch vergeben, aktueller Listenstand +1
        room = Room(room_id=new_id,
                hotel_id=self.__hotel_id, #hotel_id wird direkt vom aktuellen Hotel übernommen
                room_no=room_no,
                price_per_night=price_per_night,
                room_type=room_type,
                seasonal_factor=seasonal_factor)
    #Room wird zur internen Liste hinzugefügt
        self.__rooms.append(room)

    #Raum aus dem Hotel entfernen, wenn er existiert
    def remove_room(self, room):
        if room in self.__rooms:
            self.__rooms.remove(room)
        else:
            print("Room not found in this hotel.")

    #Zugriff auf die Raumliste --> .copy gibt eine Kopie zurück, damit niemand das Original verändern kann
    @property
    def rooms(self):
        return self.__rooms.copy()

    # Review-Verwaltung 

    #Fügt eine Bewertung hinzu und vergibt automatisch eine eindeutige ID
    def add_review(self, rating: int, comment: str, review_date: date):
        new_id = len(self.__reviews) + 1 #Review_id ist laufend
        review = Review(review_id=new_id, rating=rating, comment=comment, review_date=review_date) #Neues Review-Objekt wird erzeugt
        self.__reviews.append(review) #Review wird zur internen Liste hinzugefügt

    #Gibt eine Liste aller Bewertungen zurück. Aber nur als Kopie (zum Schutz vor Manipulation)
    def get_reviews(self):
        return self.__reviews.copy()