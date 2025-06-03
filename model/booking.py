from datetime import date
from model.invoice import Invoice
from model.guest import Guest
from model.room import Room
from model.hotel import Hotel


class Booking:

    # Konstruktor für ein neues Booking-Objekt mit vollständiger Verknüpfung zu Guest und Room
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest: Guest, room: Room, hotel = None):

        if not booking_id: #Sicherstellen das eine Booking ID übergeben worden ist
            raise ValueError("booking_id is required")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")
        
        if not check_in_date or not check_out_date: #Sicherstellen das eine check_in_date übergeben worden ist
            raise ValueError("check_in_date and check_out_date are required")
        if not isinstance (check_in_date, date) or not isinstance(check_out_date, date):
            raise ValueError("check_in_date and check_out_date must be date objects")
        
        if is_cancelled is None: #Sicherstellen das eine booking_status übergeben worden ist
            raise ValueError("is_cancelled is required")
        if not isinstance (is_cancelled, bool):
            raise ValueError("is_cancelled must be a boolean")

        if total_amount is None: #Sicherstellen das eine booking_status übergeben worden ist
            raise ValueError("total_amount is required")
        if not isinstance (total_amount, (float, int)):
            raise ValueError("total_amount must be a float")
        
        # Guest- und Room-Objekte sind Pflicht, da ohne diese keine gültige Buchung möglich ist
        if not guest:
            raise ValueError("guest is required")
        if not isinstance(guest, Guest):
            raise ValueError("guest must be a Guest object")

        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be a Room object")

        #Attributzuweisung
        self.__booking_id: int = booking_id
        self.__check_in_date: date = check_in_date
        self.__check_out_date: date = check_out_date
        self.__is_cancelled: bool = is_cancelled
        self.__total_amount: float = total_amount
        self.__guest: Guest = guest
        self.__room: Room = room
        self.__invoice: Invoice | None = None #Rechnung wird meist erst später ergänzt
        self.__hotel = hotel
        self.guest = guest


    # Getter und Setter
    @property
    def booking_id(self):
        return self.__booking_id #Nur Getter, da booking_id unveränderbar

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        if not value:
            raise ValueError("check_in_date is required")
        if not isinstance(value, date):
            raise ValueError("check_in_date must be a date")
        self.__check_in_date = value

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if not value:
            raise ValueError("check_out_date is required")
        if not isinstance(value, date):
            raise ValueError("check_out_date must be a date")
        self.__check_out_date = value

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value):
        if value is None:
            raise ValueError("is_cancelled is required")
        if not isinstance(value, bool):
            raise ValueError("is_cancelled must be a boolean")
        self.__is_cancelled = value

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        if value is None:
            raise ValueError("total_amount is required")
        if not isinstance(value, (float, int)):
            raise ValueError("total_amount must be a number")
        if value < 0:
            raise ValueError("total_amount cannot be negative")
        self.__total_amount = value
    

    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, value):
        # Falls z. B. ein Gast storniert und ersetzt wird (z. B. bei Gruppen)
        if not value:
            raise ValueError("guest is required")
        if not isinstance(value, Guest):
            raise ValueError("guest must be a Guest object")
        self.__guest = value

    @property
    def room(self):
        return self.__room

    @property
    def hotel(self):
        return self.__hotel

    @room.setter
    def room(self, value):
        # Ermöglicht z. B. Zimmerwechsel bei Upgrade
        if not value:
            raise ValueError("room is required")
        if not isinstance(value, Room):
            raise ValueError("room must be a Room object")
        self.__room = value

    @property
    def invoice(self):
        return self.__invoice

    @invoice.setter
    def invoice(self, value):
        # Eine Rechnung darf nachträglich gesetzt werden, ist aber nicht zwingend
        if not isinstance(value, Invoice):
            raise ValueError("invoice must be an Invoice object")
        self.__invoice = value

    @property
    def guest_id(self):
        return self.__guest.guest_id


    # Methode zum Stornieren der Buchung. Der Buchungsstatus wird auf "canceled" gesetzt, z. B. wenn der Gast absagt.
    def cancel(self):
        self.__is_cancelled = True #True wegen Bool
 