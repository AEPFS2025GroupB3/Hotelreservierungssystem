from datetime import date
import model #Klassen importieren
import data_access #Importiert data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.HotelDataAccess()
    
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