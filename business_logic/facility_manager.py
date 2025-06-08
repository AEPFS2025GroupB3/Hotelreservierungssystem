from datetime import date
from model.facility import Facility
from data_access.facility_data_access import FacilityDataAccess

import data_access


class FacilityManager:
    def __init__(self) -> None:
        self.__facility_da = FacilityDataAccess()

    def create_facility(self, name: str):
        self.__facility_da.create_facility(name)

    def update_facility(self, facility_id: int, new_name: str):
        self.__facility_da.update_facility_name(facility_id, new_name)

    def delete_facility(self, facility_id: int):
        self.__facility_da.delete_facility(facility_id)

