from datetime import date
import model #Klassen importieren
from model import Booking, Guest, Hotel, Invoice
import data_access #Importiert data_access

class RoomManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()

#Methode User Story 9(Room Manager)
    def read_room_with_facilities(self) -> list:
        return self.__room_da.read_room_with_facilities() 