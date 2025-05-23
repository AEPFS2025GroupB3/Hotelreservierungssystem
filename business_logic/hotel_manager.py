from datetime import date
import model
from model import RoomType #Klassen importieren
import data_access #Importiert data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()


    #Methode User Story 1.1
    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city(city) #Delegiert an DataAccess Objekt, das SQL Abfrage ausführt

    #Methode User Story 1.2
    def read_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city_and_stars(city, stars)
 
    #Methode User Story 1.3
    def read_hotels_by_city_number_of_guests(self, city: str, max_guests: int ) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city_number_of_guests(city, max_guests)

    #Methode User Story 1.4
    def read_available_hotels_by_city_and_date(self, city: str, check_in_date: date, check_out_date: date) -> list[model.hotel]:
        return self.__hotel_da.read_available_hotels_by_city_and_date(city, check_in_date, check_out_date)

    #Methode User Story 1.5
    def read_hotels_by_criteria(self, city:str, check_in_date: date, check_out_date: date, max_guests: int, stars: int) -> list[model.hotel]:
        return self.__hotel_da.read_hotels_by_criteria(city, check_in_date, check_out_date, max_guests, stars)

    #Methode User Story 1.6
    def read_hotels_information(self) ->list[model.Hotel]:
        return self.__hotel_da.read_hotels_information(self)

    #Methode User Story 3.1 (Hotelmanager)
    def create_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        return self.__hotel_da.create_hotel(name, stars, address)
        
    #Methode User Story 3.2 (Hotelmanager)
    def delete_hotel(hotel_id: int) -> bool:
        return hotel_da.delete_hotel(hotel_id)
        
    #Methode User Story 3.3 (Hotelmanager)
    def update_hotel(self, hotel: model.Hotel) -> None:
        return hotel_da.update_hotel(hotel)