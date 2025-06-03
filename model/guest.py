from model.address import Address

#Klasse erstellen
class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address: Address):
   
        if guest_id is None: #None-Check statt "if not guest_id (0 könnte auch eine guest ID sein)"
            raise ValueError("guest_id is required") #Sicherstellen, dass eine guest_id übergeben wurde
        if not isinstance(guest_id, int): #Sicherstellen das guest_id wirklich eine ganze Zahl ist
            raise ValueError("guest_id must be an integer")
        
        if not first_name: #Sicherstellen das first_name auch ein Name übergeben worden ist
            raise ValueError("first name is required")
        if not isinstance(first_name, str): #Sicherstellen das first_name wirklich ein String ist
            raise ValueError("first name must be a string")
        
        if not last_name: #Sicherstellen das last_name auch ein Name übergeben worden ist
            raise ValueError("last name is required")
        if not isinstance(last_name, str): #Sicherstellen das last_name wirklich ein String ist
            raise ValueError("last name must be a string")

        if not email: #Sicherstellen das email übergeben worden ist
            raise ValueError("email is required")
        if not isinstance(email, str): #Sicherstellen das email wirklich ein String ist
            raise ValueError("email must be a string")
        if "@" not in email or "." not in email:
            raise ValueError("email must contain '@' and '.'")


        #Private Attribute speichern
        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__address: Address = address


    #Getter & Setter
    @property
    def guest_id(self):
        return self.__guest_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("first name is required")
        if not isinstance(value, str):
            raise ValueError("first name must be a string")
        self.__first_name = value
        
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("last name is required")
        if not isinstance(value, str):
            raise ValueError("last name must be a string")
        self.__last_name = value

    @property
    def email(self):
        return self.__email
    
    @email.setter 
    def email(self, value):
        if not value:
            raise ValueError("email is required")
        if not isinstance(value, str):
            raise ValueError("email must be a string")
        if "@" not in value or "." not in value:
            raise ValueError("email must contain '@' and '.'")
        self.__email = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("address is required")
        if not isinstance(value, Address):
            raise ValueError("address must be an Address object")
        self.__address = value

    @property
    def guest(self):
        return self.__guest


    # Hilfsmethode: vollständiger Name
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Gibt Gastinformationen ohne Adresse zurück
    def get_guest_details(self):
        return f"Guest ID: {self.guest_id}, Firstname: {self.first_name}, Lastname: {self.last_name}, Email: {self.email}"

    # Gibt vollständige Gastinformationen inkl. Adresse zurück
    def get_guest_details_with_address(self):
        return f"Name: {self.get_full_name()}, E-Mail: {self.email}, Adresse: {self.address.get_full_address()}"
