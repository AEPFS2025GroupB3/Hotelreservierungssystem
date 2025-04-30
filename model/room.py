class Room: #Klasse Room erstellen
    def __init__(self, room_id: int, hotel_id: int, room_no: str, price_per_night: float, room_type: RoomType, seasonal_factor: float):

        #Alle Werte kontrollieren, bevor sie gespeichert werden
        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")

        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")

        if not room_no:
            raise ValueError("room _no is required")
        if not isinstance(room_no, str):
            raise ValueError("room_no must be a string")

        if not price_per_night:
            raise ValueError("price_per_night is required")
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night must be a float")

        if not room_type:
            raise ValueError("room_type is required")
        if not isinstance(room_type, RoomType):
            raise ValueError("room_type must be a RoomType object")

        if not seasonal_factor:
            raise ValueError("seasonal_factor is required")
        if not isinstance(seasonal_factor, float):
            raise ValueError("seasonal_factor must be a float")

        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, list[Booking]):
            raise ValueError("booking must be a list")

        self.__room_id: int = room_id
        self.__hotel_id: int = hotel_id
        self.__room_no: str = room_no
        self.__price_per_night: float = price_per_night
        self.__room_type = []
        self.__seasonal_factor: float = seasonal_factor
        self.__booking = [] #Hier unsicher wie das mit der Liste ist!!
    
    #Gibt die Room id zurück
    @property
    def room_id(self):
        return self.__room_id
    
    #Gibt die Hotel id zurück
    @property
    def hotel_id(self):
        return self.__hotel_id

    #Gibt die Zimmernummer zurück
    @property
    def room_no(self):
        return self.__room_no

    #Gibt Preis pro Nacht zurück
    @property
    def price_per_night(self):
        return self.__price_per_night

    #Damit der Preis nur geändert werden kann, wenn er grösser als 0 ist 
    @price_per_night.setter
    def price_per_night(self, new_price: float):
        if new_price > 0:
            self.__price_per_night = new_price
        else:
            print("Price per night can't be below zero.")

    #Gibt die Liste mit allen room types zurück
    @property
    def room_type(self):
        return self.__room_type

    #Gibt den aktuellen Faktor zurück
    @property
    def seasonal_factor(self):
        return self.__seasonal_factor

    #Damit der Faktor nur geändert werden kann, wenn er grösser als 0 ist
    @seasonal_factor.setter #Hier müssen wir noch die Fakotren bestimmen, damit der Setter angepasst werden kann
    def seasonal_factor(self, new_factor):
        if new_factor > 0:
            self.__seasonal_factor = new_factor
        else:
            print("Seasonal Factor needs to be above zero.")

    @property
    def booking(self):
        return self.__booking

    #Berechnet Preis mit Faktor
    def calculate_dynamic_price(self):
        return self.__price_per_night * self.__seasonal_factor

    #Methode, um Zimmernummer und Preis gelichzeitig zu ändern
    def update_room_details(self, new_room_no: str, new_price_per_night: float):
        self.__room_no = new_room_no
        self.__price_per_night = new_price_per_night 

    #Gibt die Beschreibung des Zimmers zurück
    def get_room_details(self):
        return f"Das Zimmer hat die Nummer {self.__room_no}, kostet {self.__price_per_night: .2f} CHF pro Nacht, hat den Typ: {self.__room_type.name}."


