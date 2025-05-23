from datetime import date
from model import Booking, Guest, Hotel  # falls nicht automatisch importiert

class Invoice:
    def __init__(self, invoice_id: int, issue_date: date, total_amount: float, invoice_status: str, booking: Booking, guest: Guest, hotel: Hotel, room_id: int):

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

        if not invoice_status:
            raise ValueError("invoice_status is required")
        if not isinstance(invoice_status, str):
            raise ValueError("invoice_status must be a string")

        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be a Booking object")

        if not guest:
            raise ValueError("guest is required")
        if not isinstance(guest, Guest):
            raise ValueError("guest must be a Guest object")

        if not hotel:
            raise ValueError("hotel is required")
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel must be a Hotel object")

        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")

        # === Attributzuweisung ===
        self.__invoice_id: int = invoice_id
        self.__issue_date: date = issue_date
        self.__total_amount: float = float(total_amount)
        self.__invoice_status: str = invoice_status
        self.__booking = booking
        self.__guest = guest
        self.__hotel = hotel
        self.__room_id: int = room_id

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
        if not isinstance(value, float):
            raise ValueError("total_amount must be a float")
        if value < 0:
            raise ValueError("total_amount cannot be negative")
        self.__total_amount = value

    @property
    def invoice_status(self):
        return self.__invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        if not value:
            raise ValueError("invoice_status is required")
        if not isinstance(value, str):
            raise ValueError("invoice_status must be a string")
        self.__invoice_status = value

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
    def room_id(self):
        return self.__room_id

    # === Zusatzmethoden ===

    def get_invoice_summary(self) -> str:
        return (
            f"Rechnung {self.invoice_id} für {self.guest.first_name} {self.guest.last_name}\n"
            f"Hotel: {self.hotel.name}, Zimmer: {self.room_id}\n"
            f"Betrag: CHF {self.total_amount:.2f} – Status: {self.invoice_status}\n"
            f"Datum: {self.issue_date}"
        )

    def is_canceled(self) -> bool:
        return self.invoice_status.lower() == "canceled"