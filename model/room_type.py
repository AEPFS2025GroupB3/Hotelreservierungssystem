class RoomType: #Klasse RoomType erstellen
    def __init__(self, type_id: int, max_guests: int, description: str = ""):

        if not type_id: #Kontrolliert, dass id angegeben wurde
            raise ValueError("type_id is required")
        if not isinstance(type_id, int): #Kontrolliert, dass id ein integer ist
            raise ValueError("type_id must be an integer")

        if not max_guests:
            raise ValueError("max_guests is required")
        if not isinstance(max_guests, int):
            raise ValueError("max_guests must be an integer")
        
        #if not description:
        #    raise ValueError("description is required")
        if not isinstance(description, str):
            raise ValueError("description must be a string")

        #Private Attribute zuweisen
        self.__type_id: int = type_id
        self.__max_guests: int = max_guests
        self.__description: str = description

    #Gibt die id zurück
    @property
    def type_id(self):
        return self.__type_id

    #Gibt die reine Beschreibung des Zimmertyps zurück (z. B. 'Suite'). Damit wir nacher nach bestimmten Romm Typen filtern können, mit Satz(f") nicht möglich
    @property 
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        #if not value:
        #    raise ValueError("description is required")
        if not isinstance(value, str):
            raise ValueError("description must be a string")
        self.__description = value
        
    #Gibt die maximale Anzahl an Gästen aus   
    @property
    def max_guests(self): 
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, value):
        if not value:
            raise ValueError("max_guests is required")
        if not isinstance(value, int):
            raise ValueError("max_guests must be a integer")
        self.__max_guests = value
