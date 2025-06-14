from datetime import date
import model
from model.room_type import RoomType
from model.address import Address
from model.room import Room
 

import data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()
        self.__room_da = data_access.RoomDataAccess()

    def _validate_city(self, city: str):
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if city.strip().isdigit():
            raise ValueError("Stadt darf keine Zahl sein.")

    def _validate_stars(self, stars: int):
        if stars < 1 or stars > 5:
            raise ValueError("Sterne müssen zwischen 1 und 5 liegen.")

    def _validate_guests(self, max_guests: int):
        if max_guests < 1:
            raise ValueError("Anzahl Gäste muss mindestens 1 sein.")


    def _validate_date_range(self, check_in: date, check_out: date):
        if check_in >= check_out:
            raise ValueError("Check-out-Datum muss nach dem Check-in-Datum liegen.")

    def _validate_id(self, id_value: int, name="ID"):
        if id_value < 1:
            raise ValueError(f"{name} muss eine positive Ganzzahl sein.")


    #Methode User Story 1.1
    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        self._validate_city(city) #
        return self.__hotel_da.read_hotels_by_city(city) #Delegiert an DataAccess Objekt, das SQL Abfrage ausführt

    #Methode User Story 1.2
    def read_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        self._validate_city(city)
        self._validate_stars(stars)
        return self.__hotel_da.read_hotels_by_city_and_stars(city, stars)
 
    #Methode User Story 1.3
    def read_hotels_by_city_number_of_guests(self, city: str, max_guests: int ) -> list[model.Hotel]:
        self._validate_guests(max_guests)
        return self.__hotel_da.read_hotels_by_city_number_of_guests(city, max_guests)

    #Methode User Story 1.4 / Methode User Story 4
    def read_available_hotels_by_city_and_date(self, city: str, check_in_date: date, check_out_date: date) -> list[model.Hotel]:
        self._validate_city(city) 
        self._validate_date_range(check_in_date, check_out_date) 
        return self.__hotel_da.read_available_hotels_by_city_and_date(city, check_in_date, check_out_date)

    #Methode User Story 1.5
    def read_hotels_by_criteria(self, city:str, check_in_date: date, check_out_date: date, max_guests: int, stars: int) -> list[model.Hotel]:
        self._validate_city(city) 
        self._validate_date_range(check_in_date, check_out_date) 
        self._validate_guests(max_guests) 
        self._validate_stars(stars) 
        return self.__hotel_da.read_hotels_by_criteria(city, check_in_date, check_out_date, max_guests, stars)

    #Methode User Story 1.6
    def get_hotel_details(self) ->list[model.Hotel]:
        return self.__hotel_da.get_hotel_details()
            
    #Methode User Story 2
    def get_room_details_by_hotel(self, hotel_id: int) -> list[model.Room]:
        self._validate_id(hotel_id, "Hotel-ID") 
        return self.__room_da.read_rooms_by_hotel(hotel_id)

    #Methode User Story 2.1
    def get_detailed_rooms_by_hotel(self, hotel_id: int) -> list[model.Room]:
        self._validate_id(hotel_id, "Hotel-ID") 
        return self.__room_da.read_rooms_with_facilities_by_hotel(hotel_id)

    #Methode User Story 2.2
    def read_rooms_with_facilities_by_hotel_and_date(self, hotel_id: int, check_in_date: date, check_out_date: date) -> list[model.Room]:
        self._validate_id(hotel_id, "Hotel-ID")
        self._validate_date_range(check_in_date, check_out_date) 
        return self.__room_da.read_rooms_with_facilities_by_hotel_and_date(hotel_id, check_in_date, check_out_date)


    #Methode User Story 3.3
    def update_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_da.update_hotel(hotel)

    #Methode User Story 5
    def get_hotel(self, hotel_id: int) -> list[model.Hotel]:
        self._validate_id(hotel_id, "Hotel-ID") 
        return self.__hotel_da.read_hotel_by_id(hotel_id)
