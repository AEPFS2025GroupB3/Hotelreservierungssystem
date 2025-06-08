import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice
from model.room import Room
from model.facility import Facility
#from model.room_type import RoomTyp
from data_access.facility_data_access import FacilityDataAccess

import data_access #Importiert data_access

class AdminManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()
        self.__facility_da = FacilityDataAccess()
        self.__roomtype_da = data_access.RoomTypeDataAccess()
        self.__hotel_da = data_access.HotelDataAccess()
    
    # --- Facility ---
    def create_facility(self, name: str):
        return self.__facility_da.create_facility(name)

    def update_facility(self, facility_id: int, new_name: str):
        return self.__facility_da.update_facility_name(facility_id, new_name)

    def delete_facility(self, facility_id: int):
        return self.__facility_da.delete_facility(facility_id)
    
    def facility_id_exists(self, facility_id: int) -> bool:
        return any(fac.facility_id == facility_id for fac in self.__facility_da.get_all_facilities())

    def facility_name_exists(self, name: str) -> bool:
        return any(fac.facility_name.lower() == name.lower() for fac in self.__facility_da.get_all_facilities())

    def get_facility_name_by_id(self, facility_id: int) -> str:
        facilities = self.__facility_da.get_all_facilities()
        for fac in facilities:
            if fac.facility_id == facility_id:
                return fac.facility_name


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
    #ursprünglich def delete_hotel(hotel_id: int) -> bool:
        #ursprünglich return hotel_da.delete_hotel(hotel_id)
    
    def get_all_hotels(self):
        return self.__hotel_da.get_hotel_details()


    def delete_hotel(self, hotel_id: int) -> bool: 
        return self.__hotel_da.delete_hotel_by_id(hotel_id)
    #neu, da in 3.2 das hotel durch hotel_id geholt wird und nicht durch hotel

    #alt def delete_hotel(self, hotel_id: int) -> bool:
    #    return self.__hotel_da.delete_hotel(hotel_id)
    
     

    #Die oberen zwei Kommentare sind extra so um mit der Gruppe zu besprechen

    #Methode User Story 3.3 
    # ursprünglich def update_hotel(self, hotel: model.Hotel) -> None:
        #ursprünglich return hotel_da.update_hotel(hotel)

    def update_hotel(self, hotel: model.Hotel) -> None:
        return self.__hotel_da.update_hotel(hotel)
    
    # Die oberen zwei Kommentare sind extra so um mit der Gruppe zu besprechen
    # Sollten für die Userstorys 3.1,3.2 und 3.3 ein self verwendet werden? sonst haben wir eine inkonsistenz,
    # es geht ja um genau ein bestimmtes hotel
    #Alles was zu adminmanager gehört muss mit self abgerufen werden oder? sonst weiss Python nicht, woher es das Objekt nehmen soll
    #Frage an Charuta: Müssen wir im AdminManager bei Methoden wie delete_hotel immer self.__hotel_da verwenden – oder geht auch einfach hotel_da im return?

    # ---- Für Userstory 3.2 + 3.3

    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel:
        return self.__hotel_da.read_hotel_by_id(hotel_id)
