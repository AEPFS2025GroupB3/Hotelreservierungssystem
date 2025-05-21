from datetime import date
import model #Klassen importieren
from model import Booking, Guest, Hotel, Invoice
import data_access #Importiert data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.HotelDataAccess()
    
    #Methode User Story 1.3
    def read_hotels_by_city_number_of_guests(self, city: str, max_guests: int ) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city_number_of_guests(city, max_guests)
        
    #Methode User Story 1.4
    def read_available_hotels_by_city_and_date(self, city: str, check_in_date: date, check_out_date: date) -> list[model.hotel]:
        return self.__hotel_da.read_available_hotels_by_city_and_date(city, check_in_date, check_out_date)

    #Methode User Story 1.5
    def read_hotels_by_criteria(self, city:str, check_in_date: date, check_out_date: date, max_guests: int, stars: int) -> list[model.hotel]:
        return self.__hotel_da.read_hotels_by_criteria(city, check_in_date, check_out_date, max_guests, stars)

    #Methode User Story 1.6
    def read_hotels_information(self) ->list[model.Hotel]:
        return self.__hotel_da.read_hotels_information(self)
        
    #Methode User Story 2.1 / Philip fragen oder Charuta unklar
    def read_room_details_by_hotel(hotel_id: int, check_in_date: date, check_out_date: date) -> list[dict]:
        rooms = room_da.read_available_rooms_by_hotel(hotel_id, check_in_date, check_out_date)
        nights = (check_out_date - check_in_date).days
        result = [] #Zimmerdaten als Dictionary ablegen
    
        for room in rooms:
            result.append({
                "room_no": room.room_no,
                "room_type": room.room_type.description,
                "max_guests": room.room_type.max_guests,
                "facilities": [f.facility_name for f in room.get_facilities()],
                "price_per_night": room.price_per_night,
                "total_price": round(room.calculate_dynamic_price() * nights, 2),
                "description": room.get_room_details()
            })
    
        return result

    #Methode User Story 3.1 (Hotelmanager)
    def create_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        return self.__hotel_da.create_hotel(name, stars, address)
        
    #Methode User Story 3.2 (Hotelmanager)
    def delete_hotel(hotel_id: int) -> bool:
        return hotel_da.delete_hotel(hotel_id)
        
    #Methode User Story 3.3 (Hotelmanager)
    def update_hotel(self, hotel: model.Hotel) -> None:
        return hotel_da.update_hotel(hotel)
    
    #Methode User Story 4 (BookingManager)
    def create_booking(guest_id: int, room_id: int, check_in_date: date, check_out_date: date, booking_status: str = "confirmed") -> model.Booking:
        return booking_da.create_booking(guest_id, room_id, check_in_date, check_out_date, booking_status)

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

    #Methode User Story 6 (Booking Manager)
    def cancel_booking(self, booking_id: int) -> bool:
        self.update_booking_status(booking_id, "canceled")
        invoice = invoice_da.read_invoice_by_booking_id(booking_id)
        if invoice:
            invoice_da.update_invoice_status(invoice.invoice_id, "canceled")
        return True

    #Methode User Story 7
    #def calculate_dynamic_price(self, price_per_night: float, seasonal_factor: float):

    #Methode User Story 8(Booking Manager)
    def read_bookings_by_hotel(hotel_id: int) -> list[model.Booking]: 
        return booking_da.read_bookings_by_hotel(hotel_id)

    #Methode User Story 9(Room Manager)
    def read_room_with_facilities(self) -> list:
        return self.__room_da.read_room_with_facilities() 