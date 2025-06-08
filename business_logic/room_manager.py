from datetime import date
import model
from model.hotel import Hotel
from model.facility import Facility 
import data_access #Importiert data_access

class RoomManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()

    def is_room_available(self, room_id, check_in_date, check_out_date): #Methode User Story 4
        self.__room_da = data_access.RoomDataAccess

#Methode User Story 9(Room Manager)
    def read_room_with_facilities(self) -> list:
        return self.__room_da.read_room_with_facilities() 