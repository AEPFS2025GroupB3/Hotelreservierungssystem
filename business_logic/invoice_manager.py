from datetime import date
import model
import data_access #Importiert data_access
 
class InvoiceDataAccess:
    def __init__(self) -> None:
        self.__invoice_da = data_access.InvoiceDataAccess()

    #Methode User Story 5 (Invoice Manager)
    def create_invoice_for_booking(booking: Booking, guest: Guest, hotel: Hotel, issue_date: date, invoice_status: str = "offen") -> Invoice:
        nights = (booking.check_out_date - booking.check_in_date).days
        room = room_da.read_room_by_id(booking.room_id)
        total = room.calculate_dynamic_price() * nights
 
        return invoice_da.create_invoice(
            issue_date=issue_date,
            total_amount=total,
            invoice_status=invoice_status,
            booking=booking,
            guest=guest,
            hotel=hotel,
            room_id=booking.room_id
        )
