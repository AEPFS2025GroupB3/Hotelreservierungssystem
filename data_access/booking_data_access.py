from datetime import date 
import model 
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff

class BookingDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, booking_status: str = "confirmed") -> model.Booking: #Methode User Story 4
        is_available = self.__room_da.is_room_available(room_id, check_in_date, check_out_date)
        if not is_available:
            raise Exception("Das Zimmer ist im gewählten Zeitraum nicht verfügbar.")
 
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, status)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (guest_id, room_id, check_in_date, check_out_date, booking_status)
        booking_id, _ = self.execute(sql, params)
    
        last_row_id, row_count = self.execute(sql, params)
        return model.Booking(last_row_id, room, guest)

        return model.Booking(
            booking_id=booking_id,
            guest_id=guest_id,
            room_id=room_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            status=booking_status
        )
    
    def cancel_booking(booking_id: int) -> bool: #Methode User Story 6
    booking = booking_da.read_booking_by_id(booking_id)
    if not booking:
        raise Exception("Buchung existiert nicht.")
 
    # Schritt 1: Status der Buchung ändern
    booking.booking_status = "canceled"
    booking_da.update_booking_status(booking_id, "canceled")
 
    # Schritt 2: Rechnung ebenfalls aktualisieren (falls vorhanden)
    invoice = invoice_da.read_invoice_by_booking_id(booking_id)
    if invoice:
        invoice.invoice_status = "canceled"
        invoice_da.update_invoice_status(invoice.invoice_id, "canceled")
 
    return True
 