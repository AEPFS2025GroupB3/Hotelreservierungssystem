from datetime import date
import model #Klassen importieren
import data_access #Importiert data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    
 