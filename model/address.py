class Address:
    # Konstruktor zur Initialisierung eines neuen Address-Objekts
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):
        # Hotel-ID muss vorhanden sein und kann nicht mehr verändert werden
        if not address_id:
            raise ValueError("address_id is required")
        if not isinstance(value, int):
            raise ValueError("address_id must be an integer")

        self.__address_id = address_id
        self.street = street          # nutzt den Setter
        self.city = city              # nutzt den Setter
        self.zip_code = zip_code      # nutzt den Setter

    # ID → bleibt fix, daher nur Getter (kein Setter)
    @property
    def address_id(self):
        return self.__address_id

    # Getter & Setter für street
    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        if not value:
            raise ValueError("street is required")
        if not isinstance(value, str):
            raise ValueError("street must be a string")
        self.__street = value

    # Getter & Setter für city & zip_code
    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if not value:
            raise ValueError("city is required")
        if not isinstance(value, str):
            raise ValueError("city must be a string")
        self.__city = value

    @property
    def zip_code(self):
        return self.__zip

    @zip_code.setter
    def zip_code(self, value):
        if not value:
            raise ValueError("zip code is required")
        if not isinstance(value, str):
            raise ValueError("zip code must be a string")
        self.__zip = value

    # Methode zum Zurückgeben der vollständigen Adresse als Text
    def get_full_address(self):
        return f"{self.__street}, {self.__zip} {self.__city}"
