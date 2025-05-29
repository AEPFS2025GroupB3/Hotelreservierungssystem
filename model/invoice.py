from __future__ import annotations #erlaubt Typen als Strings
from datetime import date
from model.guest import Guest
from model.hotel import Hotel
from model.room import Room

class Invoice:
    def __init__(self, invoice_id: int, issue_date: date, total_amount: float, booking: 'Booking', guest: Guest, hotel: Hotel, room: Room): #invoice_status: str,

        # === Validierungen ===
        if not invoice_id:
            raise ValueError("invoice_id is required")
        if not isinstance(invoice_id, int):
            raise ValueError("invoice_id must be an integer")

        if not issue_date:
            raise ValueError("issue_date is required")
        if not isinstance(issue_date, date):
            raise ValueError("issue_date must be a date")

        if total_amount is None:
            raise ValueError("total_amount is required")
        if not isinstance(total_amount, (float, int)):
            raise ValueError("total_amount must be a number")
        if total_amount < 0:
            raise ValueError("total_amount cannot be negative")

        #if not invoice_status:
            #raise ValueError("invoice_status is required")
        #if not isinstance(invoice_status, str):
            #raise ValueError("invoice_status must be a string")

        if not booking:
            raise ValueError("booking is required")
        #Typprüfung entfällt hier, weil booking als 'Booking' deklariert ist (Vermeidung zirkulärer Import)

        if not guest:
            raise ValueError("guest is required")
        if not isinstance(guest, Guest):
            raise ValueError("guest must be a Guest object")

        if not hotel:
            raise ValueError("hotel is required")
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel must be a Hotel object")

        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be a Room object")

        # === Attributzuweisung ===
        self.__invoice_id: int = invoice_id
        self.__issue_date: date = issue_date
        self.__total_amount: float = float(total_amount)
      #self.__invoice_status: str = invoice_status
        self.__booking: Booking = booking
        self.__guest: Guest = guest
        self.__hotel: Hotel = hotel
        self.__room: Room = room

    # === Getter & Setter ===

    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def issue_date(self):
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, value):
        if not value:
            raise ValueError("issue_date is required")
        if not isinstance(value, date):
            raise ValueError("issue_date must be a date")
        self.__issue_date = value

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

    #@property
    #def invoice_status(self):
        return self.__invoice_status

    #@invoice_status.setter
    #def invoice_status(self, value):
        #if not value:
            #raise ValueError("invoice_status is required")
        #if not isinstance(value, str):
            #raise ValueError("invoice_status must be a string")
        #self.__invoice_status = value

    @property
    def booking(self):
        return self.__booking

    @property
    def guest(self):
        return self.__guest

    @property
    def hotel(self):
        return self.__hotel

    @property
    def room(self):
        return self.__room

    # === Zusatzmethoden ===
    
    def get_invoice_summary(self) -> str:
        from model.booking import Booking
        return (
            f"Rechnung {self.invoice_id} für {self.guest.first_name} {self.guest.last_name}\n"
            f"Hotel: {self.hotel.name}, Zimmer: {self.room.room_no}\n"
            f"Betrag: CHF {self.total_amount:.2f}\n"
            f"Datum: {self.issue_date}"
        )

    def __str__(self):
        return self.get_invoice_summary()

    def is_canceled(self) -> bool:
        return self.invoice_status.lower() == "canceled"