import model 
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class RoomTypeDataAccess(BaseDataAccess): #User Story 10 Teil 2 (Rest bei Facility & Room)
    def create_room_type(self, description: str, max_guests: int):
        sql = "INSERT INTO RoomType (description, max_guests) VALUES (?, ?)"
        self.execute(sql, (description, max_guests))

    def update_room_type(self, room_type_id: int, new_description: str, new_max_guests: int):
        sql = "UPDATE RoomType SET description = ?, max_guests = ? WHERE room_type_id = ?"
        self.execute(sql, (new_description, new_max_guests, room_type_id))

    def delete_room_type(self, room_type_id: int):
        sql = "DELETE FROM RoomType WHERE room_type_id = ?"
        self.execute(sql, (room_type_id,))
