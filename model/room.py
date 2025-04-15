class Room: #Klasse Room erstellen
    def __init__(self, room_id: int, room_no: string, price_per_night: float, room_type: Room[], seasonal_factor: float, booking: Booking[]):
        self.room_id = room_id
        self.room_no = room_no
        self.price_per_night = price_per_night
        self.room_type = room_type
        self.seasonal_factor = seasonal_factor
        self.booking = booking

    def get_room_no(self):
        return self.room_no

    def get_price(self):
        return self.price_per_night

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