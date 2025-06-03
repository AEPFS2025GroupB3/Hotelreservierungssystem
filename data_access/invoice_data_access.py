from datetime import date
import model 
from model import Booking, Guest, Hotel
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class InvoiceDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def create_invoice(self, issue_date: date, total_amount: float, invoice_status: str, booking: Booking, guest: Guest, hotel: Hotel, room_id: int) -> model.Invoice: #Methode User Story 5
        sql = """
        INSERT INTO Invoice (issue_date, total_amount, invoice_status, booking_id)
        VALUES (?, ?, ?, ?)
        """
        params = (issue_date, total_amount, invoice_status, booking.booking_id)
        invoice_id, _ = self.execute(sql, params)
        return model.Invoice(
            invoice_id=invoice_id,
            issue_date=issue_date,
            total_amount=total_amount,
            invoice_status=invoice_status,
            booking=booking,
            guest=guest,
            hotel=hotel,
            room_id=room_id
        )

    def calculate_total_price(self, booking: Booking) -> float:
        duration = (booking.check_out_date - booking.check_in_date).days
        return booking.room.price_per_night * duration