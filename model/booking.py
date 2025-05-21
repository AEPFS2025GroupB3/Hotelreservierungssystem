from datetime import date

class Booking:

    # Konstruktor für ein neues Booking-Objekt
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, booking_status: str, guest_id: int, room_id: int):

        if not booking_id: #Sicherstellen das eine Booking ID übergeben worden ist
            raise ValueError("booking_id is required")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")
        
        if not check_in_date or not check_out_date: #Sicherstellen das eine check_in_date übergeben worden ist
            raise ValueError("check_in_date and check_out_date are required")
        if not isinstance (check_in_date, date) or not isinstance(check_out_date, date):
            raise ValueError("check_in_date and check_out_date must be date objects")
        
        if not booking_status: #Sicherstellen das eine booking_status übergeben worden ist
            raise ValueError("booking_status is required")
        if not isinstance (booking_status, str):
            raise ValueError("booking_status must be a string")
        
        if not guest_id: #Sicherstellen das eine Guest ID übergeben worden ist
            raise ValueError("guest_id is required")
        if not isinstance(guest_id, int):
            raise ValueError("guest_id must be an integer")

        if not room_id: #Sicherstellen das eine Guest ID übergeben worden ist
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")

        self.__booking_id: int = booking_id
        self.__check_in_date: date = check_in_date
        self.__check_out_date: date = check_out_date
        self.__booking_status: str = booking_status
        self.__invoice = None
        self.__guest_id: int = guest_id
        self.__room_id : int = room_id

    # Getter für booking_id
    @property
    def booking_id(self):
        return self.__booking_id

    # Getter & Setter für check_in_date
    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        if not value:
            raise ValueError("check-in-date is reuqired")
        if not isinstance(value,date):
            raise ValueError("check-in-date must be a date YYYY/MM/DD")
        self.__check_in_date = value

    # Getter & Setter für check_out_date
    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if not value:
            raise ValueError("check-ou-date is reuqired")
        if not isinstance(value,date):
            raise ValueError("check-ou-date must be a date YYYY/MM/DD")
        self.__check_out_date = value

    # Getter & Setter für booking_status
    @property
    def booking_status(self):
        return self.__booking_status

    @booking_status.setter
    def booking_status(self, value):
        if not value:
            raise ValueError("booking status is reuqired")
        if not isinstance(value,str):
            raise ValueError("booking Status must be a string")
        self.__booking_status = value

    #Getter für Invoice Liste (Verbindung zwischen Booking und Invoice "Composition")
    @property
    def invoice(self):
        return self.__invoice

    #Getter für guest_id
    @property
    def guest_id(self):
        return self.__guest_id
    
    #Getter für room_id
    @property
    def room_id(self):
        return self.__room_id