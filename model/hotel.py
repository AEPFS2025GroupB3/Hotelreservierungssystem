class Hotel:
    # Konstruktor zur Initialisierung eines neuen Hotels
    def __init__(self, hotel_id: int, name: str, stars: int):
        # Hotel-ID prüfen (ID bleibt fix, keine Setter nötig)
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")

        self.__hotel_id = hotel_id #privates Attribut, nicht veränderbar
        self.name = name           # ohne __, da Setter aufgerufen wird
        self.stars = stars         # ohne __, da Setter aufgerufen wird

        # Listen für Rooms und Reviews
        self.__rooms = []
        self.__reviews = []

    # Getter für hotel_id (fix, kein Setter)
    @property
    def hotel_id(self):
        return self.__hotel_id

    # Getter und Setter für Name & Sterne
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name is required")
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self.__name = value

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        if not isinstance(value, int):
            raise ValueError("stars must be an integer")
        if value < 1 or value > 5:
            raise ValueError("stars must be between 1 and 5")
        self.__stars = value

    # Hotel-Details zurückgeben (z. B. für Ausgabe oder Test)
    def get_hotel_details(self):
        return f"Hotel ID: {self.__hotel_id}, Name: {self.__name}, Stars: {self.__stars}"

    # Räume verwalten (Rooms hinzufügen und entfernen)
    def add_room(self, room):
        if room not in self.__rooms:
            self.__rooms.append(room)
        else:
            print("Room already exists in this hotel.")

    def remove_room(self, room):
        if room in self.__rooms:
            self.__rooms.remove(room)
        else:
            print("Room not found in this hotel.")

    # Bewertungen zurückgeben
    def get_reviews(self):
        return self.__reviews
