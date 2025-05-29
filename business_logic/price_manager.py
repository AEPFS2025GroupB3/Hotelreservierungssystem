from datetime import date
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice
import data_access #Importiert data_access

class PriceManager:
    def __init__(self): #Evtl. highseason, lowseason etc. ergänzen
        self.__room_da = data_access.RoomDataAccess()
        #Evtl. highseason, lowseason etc. ergänzen

    def get_seasonal_factor(self, check_in_date: date) -> float: #Methode User Story 7
        # Hochsaison: Juli & August
        if check_in_date.month in [7, 8]:
            return 1.2
        # Nebensaison: Januar, Februar, November
        elif check_in_date.month in [1, 2, 11]:
            return 0.8
        # Normale Saison
        else:
            return 1.0

    #Methode User Story 7
    #def calculate_dynamic_price(self, price_per_night: float, seasonal_factor: float):