from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import RoomType
    from model.facility import Facility
    from model.booking import Booking

class Room: #Klasse Room erstellen
    def __init__(self, room_id: int, room_no: str, price_per_night: float, seasonal_factor: float, hotel: Hotel, room_type: RoomType):

        #Alle Werte kontrollieren, bevor sie gespeichert werden
        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")

        if not room_no:
            raise ValueError("room_no is required")
        if not isinstance(room_no, str):
            raise ValueError("room_no must be a string")

        if not price_per_night:
            raise ValueError("price_per_night is required")
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night must be a float")

        if not seasonal_factor:
            raise ValueError("seasonal_factor is required")
        if not isinstance(seasonal_factor, float):
            raise ValueError("seasonal_factor must be a float")

        if not hotel:
            raise ValueError("hotel is required")
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel must be a Hotel object")

        if not room_type:
            raise ValueError("room_type is required")
        if not isinstance(room_type, RoomType):
            raise ValueError("room_type must be a RoomType Object")

        self.__room_id: int = room_id
        self.__room_no: str = room_no
        self.__price_per_night: float = float(price_per_night)
        self.__seasonal_factor: float = seasonal_factor
        self.__hotel: Hotel = hotel
        self.__room_type: RoomType = room_type

        self.__bookings: list[Booking] = [] #Aggregation: Liste von Bookings
        self.__facilities: list[Facility] = []  # Assoziation: Liste von Facility-Objekten
    
    #Gibt die Room id zurück
    @property
    def room_id(self):
        return self.__room_id

    #Gibt die Zimmernummer zurück
    @property
    def room_no(self):
        return self.__room_no
        
    @room_no.setter
    def room_no(self, value):
        if not value:
            raise ValueError("room_no is required")
        if not isinstance(value, str):
            raise ValueError("room_no must be a string")
        self.__room_no = value

    #Gibt Preis pro Nacht zurück
    @property
    def price_per_night(self):
        return self.__price_per_night

    #Damit der Preis nur geändert werden kann, wenn er grösser als 0 ist 
    @price_per_night.setter
    def price_per_night(self, value):
        if value is None:
            raise ValueError("price_per_night is required")
        if not isinstance(value, (float, int)):
            raise ValueError("price_per_night must be a number")
        if value <= 0:
            raise ValueError("price_per_night must be positive")
        self.__price_per_night = float(value)


    #Gibt den aktuellen Faktor zurück
    @property
    def seasonal_factor(self):
        return self.__seasonal_factor

    #Damit der Faktor nur geändert werden kann, wenn er grösser als 0 ist
    @seasonal_factor.setter
    def seasonal_factor(self, value):
        if value is None:
            raise ValueError("seasonal_factor is required")
        if not isinstance(value, (float, int)):
            raise ValueError("seasonal_factor must be a number")
        if value <= 0:
            raise ValueError("seasonal_factor must be positive")
        self.__seasonal_factor = float(value)


    @property
    def hotel(self):
        return self.__hotel

    @property
    def room_type(self):
        return self.__room_type

    
    #gibt die liste aller facilities zurück
    def get_facilities(self):
        return self.__facilities 
    
    #gibt die Liste aller Buchungen zurück
    def get_bookings(self):
        return self.__bookings

    
    #Methode, um Preis mit Faktor zu berechnen
    def calculate_dynamic_price(self) -> float:
        return round(self.__price_per_night * self.__seasonal_factor, 2)

    #Methode, um Zimmernummer und Preis gelichzeitig zu ändern
    def update_room_details(self, new_room_no: str, new_price: float):
        self.room_no = new_room_no
        self.price_per_night = new_price 

    #Gibt die Beschreibung des Zimmers zurück
    def get_room_details(self):
        return f"Das Zimmer hat die Nummer {self.__room_no}, kostet {self.__price_per_night: .2f} CHF pro Nacht, hat den Typ: {self.__room_type.description}."

    #um eine Facility zu ergänzen
    def add_facility(self, facility):
        if not isinstance(facility, Facility):
            raise ValueError("Must be a Facility object")
        self.__facilities.append(facility)

    #um eine Buchung zu ergänzen
    def add_booking(self, booking):
        if not isinstance(booking, Booking):
            raise ValueError("Must be a Booking object")
        self.__bookings.append(booking)

