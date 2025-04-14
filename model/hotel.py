class Hotel:
    # Konstruktor zur Initialisierung eines neuen Hotels
    def __init__(self, hotel_id, name, stars):
        # Hotel-ID muss vorhanden sein
        if not hotel_id:
            raise ValueError("hotel_id is required")

        # Hotelname muss vorhanden sein
        if not name:
            raise ValueError("name is required")

        # Sternezahl muss zwischen 1 und 5 liegen
        if stars < 1 or stars > 5:
            raise ValueError("stars must be between 1 and 5")

        # Attribute speichern
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars

        # Leere Listen für Zimmer und Bewertungen initialisieren
        self.__rooms = []
        self.__review = []

    # Gibt den Namen des Hotels zurück
    def get_name(self):
        return self.__name

    # Gibt die Anzahl Sterne zurück
    def get_stars(self):
        return self.__stars

    # Fügt dem Hotel ein Zimmer hinzu
    def add_new_hotel(self, room):
        self.__rooms.append(room)

    # Entfernt ein Zimmer, falls es existiert
    def remove_hotel(self, room):
        if room in self.__rooms:
            self.__rooms.remove(room)

    # Gibt die Hotelinformationen als Text zurück
    def get_hotel_details(self):
        return f"Hotel ID: {self.__hotel_id}, Name: {self.__name}, Stars: {self.__stars}"

    # Gibt die Liste aller Bewertungen zurück
    def get_reviews(self):
        return self.__review
