class Room: #Klasse Room erstellen
    def __init__(self, room_id: int, room_no: str, price_per_night: float, room_type: Room[], seasonal_factor: float, booking: Booking[]):

        if not room_id:
            raise ValueError("room_id is required")
        if not instance(room_id, int):
            raise ValueError("room_id must be an integer")

        if not room_no:
            raise ValueError("room _no is required")
        if not instance(room_no, str):
            raise ValueError("room_no must be a string")

        if not price_per_night:
            raise ValueError("price_per_night is required")
        if not instance(price_per_night, float):
            raise ValueError("price_per_night must be a float")

        if not room_type:
            raise ValueError("room_type is required")
        if not instance(room_type, list[Room]):
            raise ValueError("room_type must be a list")

        if not seasonal_factor:
            raise ValueError("seasonal_factor is required")
        if not instance(seasonal_factor, float):
            raise ValueError("seasonal_factor must be a float")

        if not booking:
            raise ValueError("booking is required")
        if not instance(booking, list[Booking]):
            raise ValueError("booking must be a list")

        self.__room_id: int = room_id
        self.__room_no: str = room_no
        self.__price_per_night: float = price_per_night
        self.__room_type: list[Room] = room_type
        self.__seasonal_factor: float = seasonal_factor
        self.__booking: list[Booking] = booking
    
    @property
    def get_room_no(self):
        return self.room_no

    @property
    def get_price(self):
        return self.price_per_night

    @get_price.setter
    def get_price(self, new_price):
        

    def get_room_details(self):
        return f"Das Zimmer hat die Nummer {self.room_no}, kostet {self.price_per_night: .2f} CHF pro Nacht, hat den Typ: {self.room_type}."
    
    def add_room(self):  #Diese Methode gehört zur Klasse Hotel

    def remove_room(self): #Diese Methode gehört zur Klasse Hotel

    def set_seasonal_factor(self, factor):
        self.set_seasonal_factor = factor

    def calculate_dynamic_price(self):
        return total_price = self.price_per_night * self.seasonal_factor

    def update_room_details(self, new_room_no: str, new_price_per_night: float):
        self.room_no = new_room_no
        self.price_per_night = new_price_per_night 