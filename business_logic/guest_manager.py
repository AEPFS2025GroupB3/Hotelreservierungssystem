from datetime import date
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice

import data_access #Importiert data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.GuestDataAccess()

     #Validierungsmethoden
    def _validate_name(self, name: str, field="Name"):
        if not name or not name.strip():
            raise ValueError(f"{field} darf nicht leer sein.")
        if name.strip().isdigit():
            raise ValueError(f"{field} darf keine reine Zahl sein.")

    def _validate_email(self, email: str):
        if not email or "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Ungültige E-Mail-Adresse.")

    def _validate_city(self, city: str):
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")
        if city.strip().isdigit():
            raise ValueError("Stadt darf keine reine Zahl sein.")

    def _validate_zip(self, zip_code: str):
        if not zip_code or not zip_code.strip().isdigit():
            raise ValueError("Postleitzahl muss eine Zahl sein.")

    def _validate_street(self, street: str):
        if not street or not street.strip():
            raise ValueError("Straße darf nicht leer sein.")

    def _validate_id(self, id_value: int, name="ID"):
        if id_value < 1:
            raise ValueError(f"{name} muss eine positive Ganzzahl sein.")

    def create_guest(self, first_name, last_name, email, steet, city, zip_code) -> list[model.Guest]: #Methode User Story 4
        self._validate_name(first_name, "Vorname")
        self._validate_name(last_name, "Nachname")
        self._validate_email(email)
        self._validate_street(street)
        self._validate_city(city)
        self._validate_zip(zip_code)
        return self.__guest_da.create_guest(first_name, last_name, email, street, city, zip_code)

    def get_guest_by_email(self, email): #Methode User Story 4
        self._validate_email(email)
        return self.__guest_da.get_guest_by_email(email)
    
    def get_guest(self, guest_id: int) -> Guest: #Methode User Story 5
        self._validate_id(guest_id, "Gast-ID")

        
