from datetime import date
import model 
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class HotelDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def read_hotels_by_city(self, city: str) -> list[model.Hotel]: #Methode User Story 1.1
        #Holt die Hotel- und zugehörigen Adressdaten via JOIN
        sql = """
        SELECT 
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id 
        WHERE a.city = ?
        """
        params = (city,) #Übergabeparameter für SQL Statement als Tuple
        results = self.fetchall(sql, params) #führt SQL Statement aus & gibt Liste an Tupels zurück

        #Verarbeitet jede Ergebniszeile -> wandelt in Hotel-Objekt um
        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars, 
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
                )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]
    
    def read_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]: #Methode User Story 1.2
       sql = """
        SELECT 
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id 
        WHERE a.city = ? AND h.stars >= ?
        """
       params = (city, stars,) #Übergabeparameter für SQL Statement als Tuple
       results = self.fetchall(sql, params) #führt SQL Statement aus & gibt Liste an Tupels zurück

        #Verarbeitet jede Ergebniszeile -> wandelt in Hotel-Objekt um
       return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars, 
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
                )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]
        
    def read_hotels_by_city_and_max_guests(self, city: str, max_guests: int) -> list[model.Hotel]: #Methode User Story 1.3
        sql = """
        SELECT DISTINCT
        h.hotel_id, h.name, h.stars,
        a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN RoomType rt ON r.room_type_id = rt.room_type_id
        WHERE a.city = ? AND rt.max_guests >= ?
        """
        params = (city, max_guests)
        results = self.fetchall(sql, params)

        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]

    def read_available_hotels_by_city_and_date(self, city:str, check_in_date: date, check_out_date: date) -> list[model.Hotel]: #Methode 1.4
        sql = """
        SELECT DISTINCT
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN RoomType rt ON r.type_id = rt.type_id
        LEFT JOIN Booking b ON r.room_id = b.room_id #Damit Zimmer ohne Buchungen angezeigt werden
            AND NOT (
                b.check_out_date <= ? OR
                b.check_in_date >= ?
            )
        WHERE a.city = ? AND b.booking_id IS NULL
        """
        params = (check_in_date, check_out_date, city)
        results = self.fetchall(sql, params)
 
        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
            ]
        
    def read_hotels_by_criteria(self, city:str, check_in_date: date, check_out_date: date, max_guests: int, stars: int) -> list[model.Hotel]: #Methode 1.5
        sql = """
        SELECT DISTINCT
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN RoomType rt ON r.room_type_id = rt.room_type_id
        LEFT JOIN Booking b ON r.room_id = b.room_id
            AND NOT (
                b.check_out_date <= ? OR
                b.check_in_date >= ?
            )
        WHERE 
            a.city = ?
            AND h.stars >= ?
            AND rt.max_guests >= ?
            AND b.booking_id IS NULL
        """
        params = (check_in_date, check_out_date, city, min_stars, guests)
        results = self.fetchall(sql, params)

        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]

    
    def read_hotels_information(self) -> list[model.Hotel]: #Methode User Story 1.6
        sql = """
        SELECT 
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id 
        """
        results = self.fetchall(sql)

        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]

    def create_new_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel: #Methode User Story 3.1
        address_sql = """
        INSERT INTO Address (street, zip_code, city)
        VALUES (?, ?, ?)
        """
        address_params = (address.street, address.zip_code, address.city)
        address_id, _ = self.execute(address_sql, address_params)

        hotel_sql = """
        INSERT INTO Hotel (name, stars, address_id)
        VALUES (?, ?, ?)
        """
        hotel_params = (name, stars, address_id)
        hotel_id, _ = self.execute(hotel_sql, hotel_params)

        last_row_id, row_count = self.execute(sql, params)
        return model.Hotel(last_row_id, address)

    def delete_hotel(self, hotel: model.Hotel) -> None: #Methode User Story 3.2
        if hotel is None:
            raise ValueError("Hotel cannot be None")
 
        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = (h.hotel_id,)
        last_row_id, row_count = self.execute(sql, params)
    
    def update_hotel(self, hotel: model.Hotel) -> None: #Methode User Story 3.3
        if hotel is None:
            raise ValueError("Hotel cannot be None")
 
        # Hotel aktualisieren
        hotel_sql = """
        UPDATE Hotel SET name = ?, stars = ? WHERE hotel_id = ?
        """
        hotel_params = (hotel.name, hotel.stars, hotel.hotel_id)
        self.execute(hotel_sql, hotel_params)

        # Adresse aktualisieren
        address_sql = """
        UPDATE Address SET street = ?, zip_code = ?, city = ? WHERE address_id = ?
        """
        address = hotel.address
        address_params = (address.street, address.zip_code, address.city, address.address_id)
        self.execute(address_sql, address_params)

 
    
       