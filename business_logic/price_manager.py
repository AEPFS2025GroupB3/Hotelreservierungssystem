from datetime import date

class PriceManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()

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