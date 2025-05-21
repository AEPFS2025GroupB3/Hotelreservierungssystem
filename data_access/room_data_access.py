
import model 
#from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class RoomDataAccess: #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def read_available_rooms_by_hotel(self, hotel_id: int, check_in_date: date, check_out_date: date) -> list[model.Room]:
    sql = """
    SELECT 
        r.room_id, r.hotel_id, r.room_no, r.price_per_night,
        rt.room_type_id, rt.description, rt.max_guests
    FROM Room r
    JOIN RoomType rt ON r.type_id = rt.type_id
    LEFT JOIN Booking b ON r.room_id = b.room_id
        AND NOT (
            b.check_out_date <= ? OR
            b.check_in_date >= ?
        )
    WHERE r.hotel_id = ? AND b.booking_id IS NULL
    """
    params = (check_in_date, check_out_date, hotel_id)
    results = self.fetchall(sql, params)
 
    # Erzeuge Room-Objekte mit verknüpftem RoomType
    rooms