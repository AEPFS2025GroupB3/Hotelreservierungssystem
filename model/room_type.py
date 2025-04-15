class RoomType: #Klasse RoomType erstellen
    def __init__(self, room_type_id: int, description: str, max_guests: int):

        if not room_type_id: #Kontrolliert, dass id angegeben wurde
            raise ValueError("room_type_id is required")
        if not isinstance(room_type_id, int): #Kontrolliert, dass id ein integer ist
            raise ValueError("album_id must be an integer")

        if not description:
            raise ValueError("description is required")
        if not isinstance(description, str):
            raise ValueError("description must be a string")

        if not max_guests:
            raise ValueError("max_guests is required")
        if not isinstance(max_guests, int):
            raise ValueError("max_guests must be an integer")

        #Private Attribute zuweisen
        self.__room_type_id: int = room_type_id
        self.__description: str = description
        self.__max_guests: int = max_guests

    #Gibt die reine Beschreibung des Zimmertyps zurück (z. B. 'Suite'). Damit wir nacher nach bestimmten Romm Typen filtern können, mit Satz(f") nicht möglich
    @property 
    def description(self):
        return self.__description
        
    @property
    def max_guests(self): #Wollen wir hier noch ein Setter, d.h. wollen wir die Anzahl Gäste später anpassen können
        return self.__max_guests
