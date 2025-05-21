from datetime import date
import model 
#from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class RoomDataAccess: #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def read_available_rooms_by_hotel(self, hotel_id: int, check_in_date: date, check_out_date: date) -> list[model.Room]: #Methode User Story 2.1
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
        params = (hotel_id, check_in_date, check_out_date)
        results = self.fetchall(sql, params)
    
    # Erzeuge Room-Objekte mit verknüpftem RoomType


    def read_rooms_with_facilities(self) -> list[model.Room]: #Methode User Story 9
        sql = """
        SELECT 
            r.room_id,
            r.hotel_id,
            r.price_per_night,
            f.facility_id,
            f.facility_name
        FROM Room r
        LEFT JOIN RoomFacility rf ON r.room_id = rf.room_id
        LEFT JOIN Facility f ON rf.facility_id = f.facility_id
        ORDER BY r.room_id
        """
        rows = self.fetchall(sql)
        rooms = {}
        for room_id, hotel_id, price, facility_id, facility_name in rows:
            if room_id not in rooms:
                rooms[room_id] = model.Room(room_id=room_id, hotel_id=hotel_id, price_per_night=price)
            if facility_id:
                facility = model.Facility(facility_id=facility_id, name=facility_name)
                rooms[room_id].add_facility(facility)
        return list(rooms.values())

    def read_room_with_facilities(self) -> list[dict]:
        sql = """
        SELECT 
            r.room_id,
            r.room_no,
            r.price_per_night,
            rt.description,
            rt.max_guests,
            GROUP_CONCAT(f.facility_name, ', ') as facilities
        FROM Room r
        JOIN RoomType rt ON r.room_type_id = rt.room_type_id
        LEFT JOIN RoomFacility rf ON r.room_id = rf.room_id
        LEFT JOIN Facility f ON rf.facility_id = f.facility_id
        GROUP BY r.room_id, r.room_no, r.price_per_night, rt.description, rt.max_guests
        ORDER BY r.room_no
        """
        results = self.fetchall(sql)

        return [
            {
                "room_id": row[0],
                "room_no": row[1],
                "price_per_night": row[2],
                "room_type": row[3],
                "max_guests": row[4],
                "facilities": row[5].split(", ") if row[5] else []  # falls keine Ausstattung → leere Liste
            }
            for row in results
        ]

 