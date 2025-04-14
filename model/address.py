class Address:
    # Konstruktor zur Initialisierung eines neuen Address-Objekts
    def __init__(self, address_id, street, city, zip_code):
        # Prüfen, ob eine Adresse-ID übergeben wurde
        if not address_id:
            raise ValueError("address_id is required")

        # Prüfen, ob Strasse, Stadt und PLZ vorhanden sind
        if not street:
            raise ValueError("street is required")
        if not city:
            raise ValueError("city is required")
        if not zip_code:
            raise ValueError("zip is required")

        # Attribute speichern (mit doppeltem Unterstrich = privat)
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip = zip_code

    # Methode zum Zurückgeben der vollständigen Adresse als Text
    def get_full_address(self):
        return f"{self.__street}, {self.__zip} {self.__city}"

    # Methode zum Aktualisieren der Adresse
    def update_address(self, street, city, zip_code):
        self.__street = street
        self.__city = city
        self.__zip = zip_code
