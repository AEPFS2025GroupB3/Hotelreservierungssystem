import model #Klassen importieren
import data_access #Importiert data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    #Methode User Story 1.1
    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city(city) #Delegiert an DataAccess Objekt, das SQL Abfrage ausführt

    #Methode User Story 1.2
    def read_hotels_by_city_and_stars(self, city: str, min_stars: int) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city_and_stars(city, min_stars)

