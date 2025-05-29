import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice
from model.room import Room
#from model.facility import Facility
from model.room_type import RoomType

import data_access #Importiert data_access

class AdminManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()
        #self.__facility_da = data_access.FacilityDataAccess()
        self.__roomtype_da = data_access.RoomTypeDataAccess()
    
    # --- Facility ---
    def create_facility(self, name: str):
        return self.__facility_da.create_facility(name)

    def update_facility_name(self, facility_id: int, new_name: str):
        return self.__facility_da.update_facility_name(facility_id, new_name)

    def delete_facility(self, facility_id: int):
        return self.__facility_da.delete_facility(facility_id)
    
    # --- RoomType ---
    def create_room_type(self, description: str, max_guests: int):
        return self.__roomtype_da.create_room_type(description, max_guests)

    def update_room_type(self, room_type_id: int, new_description: str, new_max_guests: int):
        return self.__roomtype_da.update_room_type(room_type_id, new_description, new_max_guests)

    def delete_room_type(self, room_type_id: int):
        return self.__roomtype_da.delete_room_type(room_type_id)
    
    # --- Room ---
    def update_room_price(self, room_id: int, new_price: float):
        return self.__room_da.update_room_price(room_id, new_price)

    def update_seasonal_factor(self, room_id: int, new_factor: float):
        return self.__room_da.update_seasonal_factor(room_id, new_factor)

    # --- Hotel ---
    #Methode User Story 3.1 
    def create_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        return self.__hotel_da.create_hotel(name, stars, address)
        
    #Methode User Story 3.2 
    def delete_hotel(hotel_id: int) -> bool:
        return hotel_da.delete_hotel(hotel_id)
        
    #Methode User Story 3.3 
    def update_hotel(self, hotel: model.Hotel) -> None:
        return hotel_da.update_hotel(hotel)