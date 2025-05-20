import model #Klassen importieren
import data_access #Importiert data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.GuestDataAccess()

    #Methode User Story 2.1
    def read_room_type_details(self,)