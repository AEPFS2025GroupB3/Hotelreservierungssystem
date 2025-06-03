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

    #Methode User Story 5 (Invoice Manager)
    def create_invoice_for_booking(self, booking: Booking, guest: Guest, hotel: Hotel, issue_date: date, invoice_status: str = "offen") -> Invoice:
        nights = (booking.check_out_date - booking.check_in_date).days
        room = self.__room_da.read_room_by_id(booking.room_id)
        total = room.calculate_dynamic_price() * nights
 
        return self.__invoice_da.create_invoice(
            issue_date=issue_date,
            total_amount=total,
            invoice_status=invoice_status,
            booking=booking,
            guest=guest,
            hotel=hotel,
            room_id=booking.room_id
        )
