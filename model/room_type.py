class RoomType: #Klasse RoomType erstellen
    def __init__(self, room_type_id: int, description: string, max_guests: int):
        self.room_type_id = room_type_id
        self.description = description
        self.max_guests = max_guests

    def get_description(self):
        return f"Das Zimmer ist vom Typ: {self.description} und kann eina maximale Anzahl von {self.max_guests} empfangen."
        
    def get_max_guests(self):
        return f" Die maximale Anzahl Gäste ist {self.max_guests}"
