from datetime import date
import model 
from model import Booking, Guest, Hotel
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess

class InvoiceDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse
        self.__guest_da = GuestDataAccess()
        self.__hotel_da = HotelDataAccess()
        self.__room_da = RoomDataAccess()

    def create_invoice(self, issue_date: date, total_amount: float, i_is_cancelled: bool, booking: Booking, guest: Guest, hotel: Hotel, room_id: int) -> model.Invoice: #Methode User Story 5
        sql = """
        INSERT INTO Invoice (issue_date, total_amount, i_is_cancelled, booking_id)
        VALUES (?, ?, ?, ?)
        """
        params = (issue_date, total_amount, i_is_cancelled, booking.booking_id)
        invoice_id, _ = self.execute(sql, params)

        room = self.__room_da.read_room_by_id(room_id)

        return model.Invoice(
            invoice_id=invoice_id, issue_date=issue_date, total_amount=total_amount, i_is_cancelled=i_is_cancelled, booking=booking, guest=guest, hotel=hotel, room=room
        )
        
    def calculate_total_price(self, booking: Booking) -> float:
        duration = (booking.check_out_date - booking.check_in_date).days
        return booking.room.price_per_night * duration


#Methode User Story 6
    def read_invoice_by_booking_id(self, booking_id:int) -> model.Invoice | None:
        sql = """
        SELECT invoice_id, issue_date, total_amount, i_is_cancelled
        FROM Invoice
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        
        if row is None:
            return None #keine RG gefunden

        invoice_id, issue_date, total_amount, i_is_cancelled = row
            
        if i_is_cancelled is None:
            raise ValueError (f"i_is_cancelled ist NULL für booking_id = {booking_id}")

        # Holt die verknüpften Objekte aus anderen DataAccess-Klassen
        from data_access.booking_data_access import BookingDataAccess
        booking_da = BookingDataAccess()
        booking = booking_da.read_booking_by_id(booking_id)  

        if booking is None:
            raise ValueError(f"Booking mit ID {booking_id} nicht gefunden.")     

            return model.Invoice(
                invoice_id=invoice_id, issue_date=issue_date, total_amount=total_amount, i_is_cancelled=bool(i_is_cancelled), booking=booking, guest=booking.guest, hotel=booking.room.hotel, room=booking.room     
            )
        return None


    def update_invoice_status(self, invoice_id: int, status: str) -> None:
        if not invoice_id:
            raise ValueError("invoice_id ist erforderlich")

        sql = """
        UPDATE Invoice
        SET i_is_cancelled = ?
        WHERE invoice_id = ?
        """
        is_cancelled = 1 if status.lower() == "canceled" else 0
        self.execute(sql, (is_cancelled, invoice_id))
