from datetime import date
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.room import Room
from model.invoice import Invoice
import data_access #Importiert data_access
 
class InvoiceManager:
    def __init__(self) -> None:
        self.__invoice_da = data_access.InvoiceDataAccess()
        self.__room_da = data_access.RoomDataAccess()

    def _validate_id(self, value: int, name: str = "ID"):
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} muss eine positive Ganzzahl sein.")

    def _validate_booking(self, booking: Booking):
        if not isinstance(booking, Booking):
            raise TypeError("Ungültiges Booking-Objekt.")
        if not hasattr(booking, "room") or not booking.room or not hasattr(booking.room, "room_id"): #hasattr -> prüft ob ein Objekt bestimmtes Attribut besitzt
            raise ValueError("Die Buchung enthält keine gültige Zimmer-ID.")
        self._validate_id(booking.room.room_id, "Zimmer-ID")

    def _validate_guest(self, guest: Guest):
        if not isinstance(guest, Guest):
            raise TypeError("Ungültiges Gast-Objekt.")

    def _validate_hotel(self, hotel: Hotel):
        if not isinstance(hotel, Hotel):
            raise TypeError("Ungültiges Hotel-Objekt.")

    def read_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        self._validate_id(booking_id, "Buchungs-ID") #
        return self.__invoice_da.read_invoice_by_booking_id(booking_id)
    
    #Methode User Story 5 (Invoice Manager)
    def create_invoice(self, booking: Booking, guest: Guest, hotel: Hotel) -> model.Invoice:
        self._validate_booking(booking) #
        self._validate_guest(guest) #
        self._validate_hotel(hotel) #

        issue_date = date.today()
        total_amount = self.__invoice_da.calculate_total_price(booking)
        i_is_cancelled = bool(booking.is_cancelled)
        issue_date = date.today()

        total_amount = self.__invoice_da.calculate_total_price(booking)
        i_is_cancelled = bool(booking.is_cancelled) 
        return self.__invoice_da.create_invoice(issue_date=issue_date, total_amount=total_amount, i_is_cancelled=i_is_cancelled, booking=booking, guest=guest, hotel=hotel, room_id=booking.room.room_id)
        

