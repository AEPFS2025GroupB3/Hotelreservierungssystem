from datetime import date
import model
from model import RoomType
from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path) 

    #Methode User Story 1.1
    def read_hotels_by_city(self, city: str) -> list[model.Hotel]: 
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
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=int(zip_code))
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
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=int(zip_code))
                )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]
        
    def read_hotels_by_city_number_of_guests(self, city: str, max_guests: int) -> list[model.Hotel]: #Methode User Story 1.3
        sql = """
        SELECT DISTINCT
        h.hotel_id, h.name, h.stars,
        a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE a.city = ? AND rt.max_guests >= ?
        """
        params = (city, max_guests)
        results = self.fetchall(sql, params)

        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=int(zip_code))
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
        ]

    #Methode User Story 1.4
    def read_available_hotels_by_city_and_date(self, city:str, check_in_date: date, check_out_date: date) -> list[model.Hotel]: 
        sql = """
        SELECT DISTINCT
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        LEFT JOIN Booking b ON r.room_id = b.room_id 
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
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=int(zip_code))
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
            ]
    
    #Methode User Story 1.5
    def read_hotels_by_criteria(self, city: str, check_in_date: date, check_out_date: date, max_guests: int, stars: int) -> list[model.Hotel]: 
        sql = """
        SELECT DISTINCT
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code,
            rt.type_id, rt.max_guests
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
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
        params = (check_in_date, check_out_date, city, stars, max_guests)
        results = self.fetchall(sql, params)

        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=int(address_id), street=street, city=city, zip_code=int(zip_code)),
                room_type=model.RoomType(type_id=int(type_id), description="", max_guests=max_guests)
            )
            for hotel_id, name, stars, address_id, street, city, zip_code, type_id, max_guests in results
            ]


    #Methode User Story 1.6
    def get_hotel_details(self) -> list[model.Hotel]: 
        sql = """
        SELECT DISTINCT
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id 
        """
        results = self.fetchall(sql)

        return [
            model.Hotel(
                hotel_id=hotel_id, name=name, stars=stars,
                address=model.Address(address_id=address_id, street=street, city=city, zip_code=int(zip_code)),
            )
            for hotel_id, name, stars, address_id, street, city, zip_code in results
            ]

    #Methode User Story 3.1
    def create_new_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel: 
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
        
        return model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address=model.Address(street=address.street, city=address.city, zip_code=address.zip_code, address_id=address_id))

    #Methode User Story 3.2
    def delete_hotel(self, hotel: model.Hotel) -> None: 
        if hotel is None:
            raise ValueError("Hotel cannot be None")
 
        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel.hotel_id,)
        last_row_id, row_count = self.execute(sql, params)
    
    #Methode User Story 3.3
    def update_hotel(self, hotel: model.Hotel) -> None: 
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

    #Methode User Story 5
    def read_hotel_by_id(self, hotel_id: int) -> model.Hotel: 
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE h.hotel_id = ?
        """
        row = self.fetchone(sql, (hotel_id,))
        if row:
            hotel_id, name, stars, address_id, street, city, zip_code = row
            address = model.Address(street, city, int(zip_code), address_id)
            return model.Hotel(hotel_id, name, stars, address)
        return None

    # Methode User Story 3.2 Methode
    def delete_hotel_by_id(self, hotel_id: int) -> bool:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        self.execute(sql, params)
        return True

        

 
    
    