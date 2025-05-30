from datetime import date

import model

from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class RoomDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def read_rooms_by_hotel(self, hotel_id: int) -> list[model.Room]: #Methode User Story 2
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night,
            rt.type_id, rt.max_guests, rt.description,
            h.hotel_id, h.name, h.stars, 
            a.address_id, a.street, a.city, a.zip_code
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE h.hotel_id = ?
        """
        params = (hotel_id,) #Übergabeparameter für SQL Statement als Tuple
        results = self.fetchall(sql, params) #führt SQL Statement aus & gibt Liste an Tupels zurück

        return [
            model.Room(room_id=room_id, room_number=room_number, price_per_night=price_per_night,
            room_type=model.RoomType(type_id, max_guests, description),
            hotel=model.Hotel(hotel_id, name, stars, model.Address(address_id, street, city, zip_code))
            )
            for room_id, room_number, price_per_night, type_id, max_guests, description, hotel_id, name, stars, address_id, street, city, zip_code in results
        ]


    def read_rooms_with_facilities_by_hotel(self, hotel_id: int) -> list[model.Room]: #Methode User Story 2.1
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, 
            rt.type_id, rt.max_guests, rt.description,
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code,
            f.facility_id, f.facility_name
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        WHERE h.hotel_id = ?
        ORDER BY r.room_id
        """

        results = self.fetchall(sql, (hotel_id,)) #Übergabgeparameter als Tuple --> (hotel_id,) muss ein Tupel sein
        rooms = {} #Dictionary als Zwischenspeicher, um jedes Zimmer nur 1x zu erstellen

        for row in results: #Durch alle zurückgegebenen Zeilen iterieren
            (room_id, room_number, price_per_night, type_id, max_guests, description, hotel_id, name, stars, address_id, street, city, zip_code, facility_id, facility_name
            ) = row

            if room_id not in rooms: ## Wenn das Zimmer noch nicht im Dictionary ist, erstelle es mit allen zugehörigen Objekten
                hotel_address = model.Address(address_id, street, city, zip_code)
                hotel = model.Hotel(hotel_id, name, stars, hotel_address)
                room_type = model.RoomType(type_id, max_guests, description)
                
                room = model.Room(room_id, room_number, price_per_night, hotel, room_type)
                
                rooms[room_id] = room #Im Dict speichern, damit es später nicht doppelt erstellt wird

            if facility_id: # Wenn eine Facility vorhanden ist (LEFT JOIN → kann NULL sein), dann hinzufügen
                rooms[room_id].add_facility(model.Facility(facility_id, facility_name))

        return list(rooms.values())


    def read_rooms_with_facilities(self) -> list[model.Room]: #Methode User Story 9
        sql = """
        SELECT 
            r.room_id, r.hotel_id, r.price_per_night,
            f.facility_id, f.facility_name
        FROM Room r
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
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
            r.room_id, r.room_number, r.price_per_night, 
            rt.description, rt.max_guests,
            GROUP_CONCAT(f.facility_name, ', ') as facilities
        FROM Room r
        JOIN RoomType rt ON r.room_type_id = rt.room_type_id
        LEFT JOIN RoomFacility rf ON r.room_id = rf.room_id
        LEFT JOIN Facility f ON rf.facility_id = f.facility_id
        GROUP BY r.room_id, r.room_number, r.price_per_night, rt.description, rt.max_guests
        ORDER BY r.room_number
        """
        results = self.fetchall(sql)

        return [
            {
                "room_id": room_id,
                "room_number": room_number,
                "price_per_night": price_per_night,
                "room_type": description,
                "max_guests": max_guests,
                "facilities": facility_str.split(", ") if facility_str else []
            }
            for room_id, room_number, price_per_night, description, max_guests, facility_str in results
        ]

    def update_room_price(self, room_id: int, new_price: float): #User Story 10 Teil 3 (Rest bei Facility & RoomType)
        sql = "UPDATE Room SET price_per_night = ? WHERE room_id = ?"
        self.execute(sql, (new_price, room_id))

    def update_seasonal_factor(self, room_id: int, new_factor: float):
        sql = "UPDATE Room SET seasonal_factor = ? WHERE room_id = ?"
        self.execute(sql, (new_factor, room_id))