import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice
from model.room import Room
from model.facility import Facility
from data_access.facility_data_access import FacilityDataAccess

import data_access

class AdminManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()
        self.__facility_da = FacilityDataAccess()
        self.__roomtype_da = data_access.RoomTypeDataAccess()
        self.__hotel_da = data_access.HotelDataAccess()

    #Validierungsmethoden
    def _validate_id(self, id_value: int, name="ID"):
        if id_value < 1:
            raise ValueError(f"{name} muss eine positive Ganzzahl sein.")

    def _validate_name(self, name: str, field="Name"):
        if not name or not name.strip():
            raise ValueError(f"{field} darf nicht leer sein.")
        if name.strip().isdigit():
            raise ValueError(f"{field} darf keine Zahl sein.")

    def _validate_guests(self, max_guests: int):
        if max_guests < 1:
            raise ValueError("Anzahl Gäste muss mindestens 1 sein.")

    def _validate_price_or_factor(self, value: float, name="Wert"):
        if value < 0:
            raise ValueError(f"{name} darf nicht negativ sein.")

    def _validate_stars(self, stars: int):
        if stars < 1 or stars > 5:
            raise ValueError("Sterne müssen zwischen 1 und 5 liegen.")

    
    #Facility Methode User Story 10
    def create_facility(self, facility_name: str):
        self._validate_name(facility_name, "Facility-Name")
        return self.__facility_da.create_facility(facility_name)

    def update_facility(self, facility_id: int, new_name: str):
        self._validate_id(facility_id, "Facility-ID")
        self._validate_name(new_name, "Neuer Facility-Name")
        return self.__facility_da.update_facility_name(facility_id, new_name)

    def delete_facility(self, facility_id: int):
        self._validate_id(facility_id, "Facility-ID")
        return self.__facility_da.delete_facility(facility_id)
    
    def facility_id_exists(self, facility_id: int) -> bool:
        self._validate_id(facility_id, "Facility-ID")
        return any(fac.facility_id == facility_id for fac in self.__facility_da.get_all_facilities())

    def facility_name_exists(self, name: str) -> bool:
        self._validate_name(name, "Facility-Name")
        return any(fac.facility_name.lower() == name.lower() for fac in self.__facility_da.get_all_facilities())

    def get_facility_name_by_id(self, facility_id: int) -> str:
        self._validate_id(facility_id, "Facility-ID")
        facilities = self.__facility_da.get_all_facilities()
        for fac in facilities:
            if fac.facility_id == facility_id:
                return fac.facility_name


    #Methode User Story 10
    def create_room_type(self, description: str, max_guests: int):
        self._validate_name(description, "RoomType-Beschreibung")
        self._validate_guests(max_guests)
        return self.__roomtype_da.create_room_type(description, max_guests)

    def update_room_type(self, room_type_id: int, new_description: str, new_max_guests: int):
        self._validate_id(room_type_id, "RoomType-ID")
        self._validate_name(new_description, "Neue Beschreibung")
        self._validate_guests(new_max_guests)
        return self.__roomtype_da.update_room_type(room_type_id, new_description, new_max_guests)

    def delete_room_type(self, room_type_id: int):
        self._validate_id(room_type_id, "RoomType-ID")
        return self.__roomtype_da.delete_room_type(room_type_id)
    
    #Room
    def update_room_price(self, room_id: int, new_price: float):
        self._validate_id(room_id, "Room-ID")
        self._validate_price_or_factor(new_price, "Preis")
        return self.__room_da.update_room_price(room_id, new_price)

    def update_seasonal_factor(self, room_id: int, new_factor: float):
        self._validate_id(room_id, "Room-ID")
        self._validate_price_or_factor(new_factor, "Saisonfaktor")
        return self.__room_da.update_seasonal_factor(room_id, new_factor)


    #Methode User Story 3.1 
    def create_new_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        self._validate_name(name, "Hotelname")
        self._validate_stars(stars)
        return self.__hotel_da.create_new_hotel(name, stars, address)
    

    #Methode User Story 3.2 
    def get_all_hotels(self):
        return self.__hotel_da.get_hotel_details()


    def delete_hotel(self, hotel_id: int) -> bool: 
        self._validate_id(hotel_id, "Hotel-ID")
        return self.__hotel_da.delete_hotel_by_id(hotel_id)


    #Methode User Story 3.3 
    def update_hotel(self, hotel: model.Hotel) -> None:
        self._validate_id(hotel.hotel_id, "Hotel-ID")
        self._validate_name(hotel.name, "Hotelname")
        self._validate_stars(hotel.stars)
        return self.__hotel_da.update_hotel(hotel)
    
    #Methode Userstory 3.2 + 3.3
    def get_hotel_by_id(self, hotel_id: int) -> model.Hotel:
        self._validate_id(hotel_id, "Hotel-ID")
        return self.__hotel_da.read_hotel_by_id(hotel_id)
