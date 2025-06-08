from datetime import date
import model
from model.room_type import RoomType
from model.address import Address
from model.room import Room
from model.facility import Facility
import data_access

class FacilityManager:
    def __init__(self):
        self.__facility_da = FacilityDataAccess()
        self.__room_da = data_access.RoomDataAccess()

    def create_facility(self, name: str):
        self.__facility_da.create_facility(name)

    def update_facility(self, facility_id: int, new_name: str):
        self.__facility_da.update_facility_name(facility_id, new_name)

    def delete_facility(self, facility_id: int):
        self.__facility_da.delete_facility(facility_id)

