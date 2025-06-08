import model
from model.facility import Facility
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class FacilityDataAccess(BaseDataAccess): #User Story 10 Teil 1 (Rest bei RoomType & Room)
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    #Methoden User Story 10
    def create_facility(self, facility_name: str):
        sql = "INSERT INTO Facilities (facility_name) VALUES (?)"
        self.execute(sql, (facility_name,))

    def update_facility_name(self, facility_id: int, new_name: str):
        sql = "UPDATE Facilities SET facility_name = ? WHERE facility_id = ?"
        self.execute(sql, (new_name, facility_id))

    def get_all_facilities(self) -> list[Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(facility_id=row[0], facility_name=row[1]) for row in rows]

    def delete_facility(self, facility_id: int):
        sql = "DELETE FROM Facilities WHERE facility_id = ?"
        self.execute(sql, (facility_id,))
