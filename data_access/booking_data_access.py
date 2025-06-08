from datetime import date 
import model 
from data_access.base_data_access import BaseDataAccess #Basisklasse für Datenbankzugriff
from data_access.guest_data_access import GuestDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.invoice_data_access import InvoiceDataAccess


class BookingDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse
        self.__guest_da = GuestDataAccess()
        self.__room_da = RoomDataAccess()

    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool = True) -> model.Booking: #Methode User Story 4
        # changed status to is_cancelled by Charuta
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (guest_id, room_id, check_in_date, check_out_date, is_cancelled)
        booking_id, _ = self.execute(sql, params)
    
        #last_row_id, row_count = self.execute(sql, params)
        #return model.Booking(last_row_id, room, guest)

        guest = self.__guest_da.read_guest_by_id(guest_id)
        room = self.__room_da.read_room_by_id(room_id)
        
        return model.Booking(
            booking_id=booking_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled=bool(is_cancelled),
            total_amount=room.price_per_night * (check_out_date - check_in_date).days,
            guest=guest,
            room=room
        )

    def is_room_available(self, room_id: int, check_in_date: date, check_out_date: date) -> bool: #Mehtode User Story 4
        sql = """
        SELECT COUNT (*)
        FROM Booking
        WHERE room_id = ?
            AND NOT (
                check_out_date <= ? OR 
                check_in_date >= ?
            )
        """

        params = (room_id, check_in_date, check_out_date)
        count, = self.fetchone(sql, params)
        return count == 0 #True wenn kein koflikt = vefügbar

    def get_all_bookings(self) -> list[model.Booking]: #Methode User Story 5
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled
        FROM Booking
        """
        rows = self.fetchall(sql)

        guest_da = GuestDataAccess()
        room_da = RoomDataAccess()
        invoice_da = InvoiceDataAccess()

        bookings = []
        for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled in rows:
            guest = guest_da.read_guest_by_id(guest_id)
            room = room_da.read_room_by_id(room_id)
            invoice = invoice_da.read_invoice_by_booking_id(booking_id)

            #Dauer Berechnen und total amount
            duration = (check_out_date - check_in_date).days
            total_amount = room.price_per_night * duration 

            booking = model.Booking(
                booking_id=booking_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=bool(is_cancelled),
                total_amount=float(total_amount),
                guest=guest,
                room=room
            )

            if invoice:
                booking.invoice = invoice

            bookings.append(booking)

        return bookings

    
    def update_booking_status(self, booking_id: int, is_cancelled: bool) -> None: #Methode User Story 6
        if not booking_id:
            raise ValueError("booking_id is required")

        sql = """
        UPDATE Booking
        SET is_cancelled = ?
        WHERE booking_id = ?
        """
        self.execute(sql, (int(is_cancelled), booking_id))

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled
        FROM Booking
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled = row

            guest_da = GuestDataAccess()
            room_da = RoomDataAccess()

            guest = guest_da.read_guest_by_id(guest_id)
            room = room_da.read_room_by_id(room_id)
            
            total_amount = room.price_per_night * (check_out_date - check_in_date).days
            
            return model.Booking(
                booking_id=booking_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=bool(is_cancelled),
                total_amount=total_amount,
                guest=guest,
                room=room
            )
        return None


    def read_bookings_by_hotel(self, hotel_id: int) -> list[model.Booking]: #Methode User Story 8
        sql = """
        SELECT 
        b.booking_id, b.check_in_date, b.check_out_date, b.is_cancelled, b.total_amount,
        r.room_id, r.room_number, r.price_per_night, r.type_id,
        rt.type_id, rt.max_guests, rt.description,
        h.hotel_id, h.name, h.stars, 
        a.address_id, a.street, a.city, a.zip_code,
        g.guest_id, g.first_name, g.last_name, g.email
        FROM Booking b
        JOIN Room r ON b.room_id = r.room_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        JOIN Guest g ON b.guest_id = g.guest_id
        WHERE h.hotel_id = ?
        """
        results = self.fetchall(sql, (hotel_id,))

        return [
            model.Booking(
                booking_id=booking_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                is_cancelled=bool(is_cancelled),
                total_amount=total_amount,
                hotel=model.Hotel(
                    hotel_id=hotel_id,
                    name=name,
                    stars=stars,
                    address=model.Address(
                        address_id=address_id,
                        street=street,
                        city=city,
                        zip_code=zip_code
                    )
                ),
                guest=model.Guest(
                    guest_id=guest_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    address=model.Address(
                        address_id=address_id,
                        street=street,
                        city=city,
                        zip_code=zip_code
                    )
                ),
                room = model.Room(
                    room_id=room_id,
                    room_number=room_number,
                    price_per_night=price_per_night,
                    room_type=model.RoomType(
                        type_id=type_id,
                        max_guests=max_guests,
                        description=description
                    ),
                    hotel=model.Hotel(
                        hotel_id=hotel_id,
                        name=name,
                        stars=stars,
                        address=model.Address(
                            address_id=address_id,
                            street=street,
                            city=city,
                            zip_code=zip_code
                        )
                    )
                )
            )
            for booking_id, check_in_date, check_out_date, is_cancelled, total_amount,
                room_id, room_number, price_per_night, room_type_id,
                type_id, max_guests, description,
                hotel_id, name, stars,
                address_id, street, city, zip_code,
                guest_id, first_name, last_name, email in results
        ]
