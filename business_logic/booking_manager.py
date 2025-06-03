from datetime import date
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
from model.invoice import Invoice

import data_access #Importiert data_access


class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = data_access.BookingDataAccess()
        #self.__price & invoice manager??
        
    #Methode User Story 4 (BookingManager)
    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, booking_status: str = "confirmed") -> model.Booking:
        is_available = self.__room_da.is_room_available(room_id, check_in_date, check_out_date)
        if not is_available:
            raise Exception("Zimmer ist im gewünschten Zeitraum nicht verfügbar.")
        
        return self.__booking_da.create_booking(
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            booking_status
        )

    #Methode User Story 5
    def get_booking(self, booking_id: int) -> Booking:
        return self.__booking_da.read_booking_by_id(booking_id)
    
    #Methode User Story 6 (Booking Manager)
    def cancel_booking(self, booking_id: int) -> bool:
        self.update_booking_status(booking_id, "canceled")
        invoice = invoice_da.read_invoice_by_booking_id(booking_id)
        if invoice:
            invoice_da.update_invoice_status(invoice.invoice_id, "canceled")
        return True

    def get_all_bookings(self) -> list[Booking]:
        return self.__booking_da.get_all_bookings()  # oder read_all_bookings() je nach Implementierung

    def get_booking(self, booking_id: int) -> Booking:
        return self.__booking_da.read_booking_by_id(booking_id)
        
    #Methode User Story 8(Booking Manager)
    def read_bookings_by_hotel(self, hotel_id: int) -> list[model.Booking]: 
        return self.__booking_da.read_bookings_by_hotel(hotel_id)
