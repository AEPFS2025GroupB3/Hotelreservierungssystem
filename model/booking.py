from datetime import date
from model.invoice import Invoice
from model.guest import Guest
from model.room import Room


class Booking:

    # Konstruktor für ein neues Booking-Objekt mit vollständiger Verknüpfung zu Guest und Room
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, booking_status: str, guest: Guest, room: Room):

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
        self.__booking_status: str = booking_status
        self.__guest: Guest = guest
        self.__room: Room = room
        self.__invoice: Invoice | None = None #Rechnung wird meist erst später ergänzt


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
    def booking_status(self):
        return self.__booking_status

    @booking_status.setter
    def booking_status(self, value):
        if not value:
            raise ValueError("booking_status is required")
        if not isinstance(value, str):
            raise ValueError("booking_status must be a string")
        self.__booking_status = value

    
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


    # Methode zum Stornieren der Buchung. Der Buchungsstatus wird auf "canceled" gesetzt, z. B. wenn der Gast absagt.
    def cancel(self):
        self.booking_status = "canceled"
 