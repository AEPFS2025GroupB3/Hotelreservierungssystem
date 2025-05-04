#Klasse erstellen
class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str):
   
        if not guest_id: #Sicherstellen, dass eine guest_id übergeben wurde
            raise ValueError("guest_id is required")
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


        #Private Attribute speichern
        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email

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
        self.__email = value


    #Methoden erstellen
    def get_guest_details(self):
        return f"Guest ID: {self.__guest_id}, Firstname: {self.__first_name}, Lastname: {self.__last_name}, Email: {self.__email}"