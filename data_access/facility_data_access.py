import model 
from data_access.base_data_access import BaseDataAccess

class FacilityDataAccess(BaseDataAccess): #User Story 10 Teil 1 (Rest bei RoomType & Room)
    def create_facility(self, facility_name: str):
        sql = "INSERT INTO Facility (facility_name) VALUES (?)"
        self.execute(sql, (facility_name,))

    def update_facility_name(self, facility_id: int, new_name: str):
        sql = "UPDATE Facility SET facility_name = ? WHERE facility_id = ?"
        self.execute(sql, (new_name, facility_id))

    def delete_facility(self, facility_id: int):
        sql = "DELETE FROM Facility WHERE facility_id = ?"
        self.execute(sql, (facility_id,))

