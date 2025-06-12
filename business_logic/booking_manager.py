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
        self.__room_da = data_access.RoomDataAccess()
        self.__invoice_da = data_access.InvoiceDataAccess()
        #self.__price & invoice manager??

    def _validate_date_range(self, check_in: date, check_out: date):
        if check_in >= check_out:
            raise ValueError("Check-out-Datum muss nach dem Check-in-Datum liegen.")

    def _validate_id(self, id_value: int, name="ID"):
        if id_value < 1:
            raise ValueError(f"{name} muss eine positive Ganzzahl sein.")

    def _validate_total_amount(self, total_amount: float):
        if total_amount < 0:
            raise ValueError("Totalbetrag darf nicht negativ sein.")
        
    #Methode User Story 4 (BookingManager)
    def create_booking(self, guest_id: int, room_id: int, check_in_date: date, check_out_date: date, total_amount: float, is_cancelled: bool) -> model.Booking:
        
        self._validate_id(guest_id, "Gast-ID")
        self._validate_id(room_id, "Raum-ID")
        self._validate_date_range(check_in_date, check_out_date)
        self._validate_total_amount(total_amount)

        return self.__booking_da.create_booking(
            guest_id,
            room_id,
            check_in_date,
            check_out_date,
            total_amount,
            is_cancelled
        )

    #Methode User Story 4 letzte Zeile musste ich anpassen voher : self.__booking_da = data_access.BookingDataAccess ?????
    def is_room_available(self, room_id, check_in_date, check_out_date): 
        self._validate_id(room_id, "Room-ID")
        self._validate_date_range(check_in_date, check_out_date)
        return self.__booking_da.is_room_available(room_id, check_in_date, check_out_date)

    #Methode User Story 5
    def get_booking(self, booking_id: int) -> Booking:
        self._validate_id(booking_id, "Booking-ID")
        return self.__booking_da.read_booking_by_id(booking_id)
    
    #Methode User Story 6 (Booking Manager
    def read_booking_by_id(self, booking_id: int):
        self._validate_id(booking_id, "Booking-ID")
        return self.__booking_da.read_booking_by_id(booking_id)

    def cancel_booking(self, booking_id: int) -> bool:
        self._validate_id(booking_id, "Booking-ID")
        self.update_booking_status(booking_id, True)
        invoice = self.__invoice_da.read_invoice_by_booking_id(booking_id)
        if invoice:
            self.__invoice_da.update_invoice_status(invoice.invoice_id, "canceled")
        return True
    
    def update_booking_status(self, booking_id: int, is_cancelled: bool):
        self._validate_id(booking_id, "Booking-ID")
        self.__booking_da.update_booking_status(booking_id, is_cancelled)

    #Hilfsmethode damit cancel_booking funktioniert
    def get_all_bookings(self) -> list[Booking]:
        return self.__booking_da.get_all_bookings()  # oder read_all_bookings() je nach Implementierung

    def get_booking(self, booking_id: int) -> Booking:
        return self.__booking_da.read_booking_by_id(booking_id)
        
    #Methode User Story 8
    def read_bookings_by_hotel(self, hotel_id: int) -> list[model.Booking]: 
        self._validate_id(hotel_id, "Hotel-ID")
        return self.__booking_da.read_bookings_by_hotel(hotel_id)
 