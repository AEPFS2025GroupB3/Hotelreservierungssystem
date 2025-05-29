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
    
    def update_booking_status(self, booking_id: int, new_status: str) -> None: #Methode User Story 6
        if not booking_id:
            raise ValueError("booking_id is required")

        sql = """
        UPDATE Booking
        SET status = ?
        WHERE booking_id = ?
        """
        self.execute(sql, (new_status, booking_id))

    def read_invoice_by_booking_id(self, booking_id: int) -> model.Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, status
        FROM Booking
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            return model.Booking(*row)
        return None

    def read_invoice_by_booking_id(self, booking_id: int) -> model.Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, booking_status
        FROM Booking
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            return model.Booking(*row)
        return None

    def read_bookings_by_hotel(self, hotel_id: int) -> list[model.Booking]: #Methode User Story 8
        sql = """
        SELECT 
        b.booking_id, b.check_in_date, b.check_out_date, b.is_cancelled, b.total_amount,
        h.hotel_id, h.name, h.stars, 
        a.address_id, a.street, a.city, a.zip_code,
        g.guest_id, g.first_name, g.last_name
        FROM Booking b
        JOIN Room r ON b.room_id = r.room_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        JOIN Guest g ON b.guest_id = g.guest_id
        WHERE h.hotel_id = ?

        """
        results = self.fetchall(sql, (hotel_id,))


        return [
            model.Booking(
                booking_id=booking_id, check_in_date=check_in_date, check_out_date=check_out_date, is_cancelled=is_cancelled, total_amount=total_amount,
                hotel=model.Hotel(hotel_id=hotel_id, name=name),
                address=model.Address(address_id=address_id, street=street,city=city, zip_code=zip_code),
                guest=model.Guest(guest_id=guest_id, first_name=first_name, last_name=last_name)
                )
            for booking_id, check_in_date, check_out_date, is_cancelled, total_amount, hotel_id, name, address_id, street, city, zip_code, guest_id, first_name, last_name in results
        ]
