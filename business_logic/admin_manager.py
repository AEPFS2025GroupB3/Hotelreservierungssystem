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
        self.__hotel_da=data_access.HotelDataAccess()
    
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
    def create_new_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        return self.__hotel_da.create_new_hotel(name, stars, address)
    
    # def create_new_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
    # return self.__hotel_da.create_new_hotel(name, stars, address)
    #Die oberen zwei Kommentare sind extra so um mit der Gruppe zu besprechen


    #Methode User Story 3.2 
    def delete_hotel(hotel_id: int) -> bool:
        return hotel_da.delete_hotel(hotel_id)
    
    #def delete_hotel(self, hotel_id: int) -> bool:
    #return self.__hotel_da.delete_hotel(hotel_id)    
    #Die oberen zwei Kommentare sind extra so um mit der Gruppe zu besprechen

    #Methode User Story 3.3 
    def update_hotel(self, hotel: model.Hotel) -> None:
        return hotel_da.update_hotel(hotel)
    #def update_hotel(self, hotel: model.Hotel) -> None:
        return self.__hotel_da.update_hotel(hotel)
    
    # def update_hotel(self, hotel: model.Hotel) -> None:
    #return self.__hotel_da.update_hotel(hotel)
    # Die oberen zwei Kommentare sind extra so um mit der Gruppe zu besprechen
    # Sollten für die USerstorys 3.1,3.2 und 3.3 ein self verwendet werden? sonst haben wir eine inkonsistenz,
    # es geht ja um genau ein bestimmtes hotel

    # ---- Für USerstory 3.2 + 3.3
    #def get_hotel_by_id(self, hotel_id: int):
    #return self.__hotel_da.read_hotel_by_id(hotel_id)

