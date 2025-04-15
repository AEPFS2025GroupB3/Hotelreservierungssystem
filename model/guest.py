#Klasse erstellen noch nicht fertig
class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str):

        #Sicherstellen, dass eine guest_id übergeben wurde
        if not guest_id:
            raise ValueError("guest_id is required")
        if not isinstance(guest_id, int): #Sicherstellen das guest_id wirklich eine ganze Zahl ist
            raise ValueError("guest_id must be an integer")

        #Sicherstellen das first_name auch ein Name übergeben worden ist
        if not first_name:
            raise ValueError("first name is required")
        if not isinstance(first_name, str): #Sicherstellen das first_name wirklich ein String ist
            raise ValueError("first name must be a string")

        #Sicherstellen das last_name auch ein Name übergeben worden ist
        if not last_name:
            raise ValueError("last name is required")
        if not isinstance(last_name, str): #Sicherstellen das last_name wirklich ein String ist
            raise ValueError("last name must be a string")

        #Sicherstellen das email übergeben worden ist
        if not email:
            raise ValueError("email is required")
        if not isinstance(email, str): #Sicherstellen das email wirklich ein String ist
            raise ValueError("email must be a string")


        #Private Attribute speichern
        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email

    #Methoden erstellen
    def get_full_name(self):
        return f"Firstname: {self.__first_name}, Lastname: {self.__last_name}"

    def get_email(self):
        return f"Email: {self.__email}"

    #sind mit Buchungdetails diese vom Gast gemeint? Unklare Beschreibung Methode
    def get_booking_details(self):
        return f"Guest ID: {self.__guest_id}, Firstname: {self.__first_name}, Lastname: {self.__last_name}, Email: {self.__email}"