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

    def read_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        return self.__invoice_da.read_invoice_by_booking_id(booking_id)
    
    #Methode User Story 5 (Invoice Manager)
    def create_invoice(self, booking: Booking, guest: Guest, hotel: Hotel) -> model.Invoice:
        issue_date = date.today()

        total_amount = self.__invoice_da.calculate_total_price(booking)
        i_is_cancelled = bool(booking.is_cancelled)
        return self.__invoice_da.create_invoice(issue_date=issue_date, total_amount=total_amount, i_is_cancelled=i_is_cancelled, booking=booking, guest=guest, hotel=hotel, room_id=booking.room.room_id)

