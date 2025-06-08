from datetime import date
from model.facility import Facility
from data_access.facility_data_access import FacilityDataAccess

import data_access


class FacilityManager:
    def __init__(self) -> None:
        self.__facility_da = FacilityDataAccess()

    #Methode User Story 10
    def create_facility(self, name: str):
        self.__facility_da.create_facility(name)

    def update_facility(self, facility_id: int, new_name: str):
        self.__facility_da.update_facility_name(facility_id, new_name)

    def facility_id_exists(self, facility_id: int) -> bool:
        facilities = self.__facility_da.get_all_facilities()
        return any(fac[0] == facility_id for fac in facilities)  # falls du eine Liste von Tupeln bekommst


    def delete_facility(self, facility_id: int):
        self.__facility_da.delete_facility(facility_id)

