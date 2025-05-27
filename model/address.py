from datetime import date

class Address:
    #Konstruktor zur Initialisierung einer Adresse mit Validierung
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):
        
        #address_id ist zwingend und darf nur eine ganze Zahl sein
        if not address_id:
            raise ValueError("address_id is required")
        if not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        
        #Strasse muss angegeben sein und ein String sein
        if not street:
            raise ValueError("street is required")
        if not isinstance(street, str):
            raise ValueError("street must be a string")

        #Stadt muss angegeben sein
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be a string")

        #PLZ muss angegeben sein
        if not zip_code:
            raise ValueError("zip code is required")
        if not isinstance(zip_code, str):
            raise ValueError("zip code must be a string")

        # Zuweisung zu privaten Attributen
        self.__address_id: int = address_id
        self.__street: str = street          
        self.__city: str = city              
        self.__zip_code: str = zip_code      

    # ID → bleibt fix, daher nur Getter 
    @property
    def address_id(self):
        return self.__address_id

    # Getter & Setter für street, city & zip_code
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
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        if not value:
            raise ValueError("zip code is required")
        if not isinstance(value, str):
            raise ValueError("zip code must be a string")
        self.__zip_code = value

    # Gibt die vollständige Adresse als formatierten String zurück,
    # z. B. für Ausgaben in Hotel- oder Gästedetails.
    def get_full_address(self):
        return f"{self.__street}, {self.__zip_code} {self.__city}"
        
 