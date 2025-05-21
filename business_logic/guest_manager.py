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
        
    #Methode User Story 2.2
    def read_room_details_by_hotel(hotel_id: int, check_in_date: date, check_out_date: date) -> list[dict]:
    rooms = room_da.read_available_rooms_by_hotel(hotel_id, check_in_date, check_out_date)
    nights = (check_out_date - check_in_date).days
    result = [] #Zimmerdaten als Dictionary ablegen
 
    for room in rooms:
        result.append({
            "room_no": room.room_no,
            "room_type": room.room_type.description,
            "max_guests": room.room_type.max_guests,
            "facilities": [f.facility_name for f in room.get_facilities()],
            "price_per_night": room.price_per_night,
            "total_price": round(room.calculate_dynamic_price() * nights, 2),
            "description": room.get_room_details()
        })
 
    return result
    