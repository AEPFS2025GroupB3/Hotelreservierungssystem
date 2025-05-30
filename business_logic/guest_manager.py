from datetime import date
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice

import data_access #Importiert data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.HotelDataAccess()

    def create_guest(self, first_name, last_name, email, address) -> list[model.Guest]: #Methode User Story 4
        return self.__guest_da.create_guest(first_name, last_name, email, address)
    