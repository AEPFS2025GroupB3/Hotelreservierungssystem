from datetime import date
import model
from model import Guest
from data_access.base_data_access import BaseDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    #Methode User Story 4
    def create_guest(self, first_name: str, last_name: str, email: str, street: str, city: str, zip_code: str) -> model.Guest: 
        sql_address = """
        INSERT INTO Address (street, city, zip_code)
        VALUES(?,?,?)
        """
        address_params = (street, city, zip_code)
        address_id, _ = self.execute(sql_address, address_params)

        sql_guest = """
        INSERT INTO Guest (first_name, last_name, email, address_id)
        VALUES (?, ?, ?, ?)
        """
        guest_params = (first_name, last_name, email, address_id)
        guest_id, _ = self.execute(sql_guest, guest_params)

        address = model.Address(
            address_id=address_id,
            street=street,
            city=city,
            zip_code=zip_code
        )

        return model.Guest(
            guest_id=guest_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address
        )

    #Methode User Story 4
    def get_guest_by_email(self, email: str) -> Guest | None: 
        sql = """
        SELECT * FROM Guest
        WHERE email = ? 
        """
        row = self.fetchone(sql, (email,))
        return Guest(*row) if row else None #Wenn es kein Gast gibt, dann None
     
        
    #Methode User Story 5
    def read_guest_by_id(self, guest_id: int) -> model.Guest: 
        sql = """
            SELECT g.guest_id, g.first_name, g.last_name, g.email, 
                    a.address_id, a.street, a.city, a.zip_code
            FROM Guest g
            JOIN Address a ON g.address_id = a.address_id
            WHERE g.guest_id = ?
        """
        row = self.fetchone(sql, (guest_id,))
        
        if row:
            guest_id, first_name, last_name, email, address_id, street, city, zip_code = row

            if not isinstance(street, str):
                street = str(street) if street is not None else ""

            address = model.Address(
                street=street,
                city=city,
                zip_code=int(zip_code),
                address_id=address_id
            )
            return model.Guest(guest_id, first_name, last_name, email, address)

        return None
