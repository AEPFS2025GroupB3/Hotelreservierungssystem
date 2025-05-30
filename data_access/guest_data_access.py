from datetime import date
import model
from model import Guest
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class GuestDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def create_guest(self, first_name: str, last_name: str, email: str, address: str) -> model.Guest: #Methode User Story 4
        sql = """
        INSERT INTO Guest (first_name, last_name, email, address)
        VALUES (?, ?, ?, ?, )
        """
        params = (first_name, last_name, email, address)
        last_row_id, _ = self.execute(sql, params)

        return model.Guest(
            guest_id=last_row_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address
        )
            