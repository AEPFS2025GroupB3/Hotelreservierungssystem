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

        return model.Invoice(
            invoice_id=invoice_id, issue_date=issue_date, total_amount=total_amount, i_is_cancelled=i_is_cancelled, booking=booking, guest=guest, hotel=hotel, room=room
        )
        
        #return [
         #   model.Invoice(
          #      invoice_id=invoice_id, issue_date=issue_date, total_amount=total_amount, i_is_cancelled=i_is_cancelled,
           #     booking=model.Booking( booking_id=booking_id, check_in_date=check_in_date, check_out_date=check_out_date, is_cancelled=bool(is_cancelled), total_amount=total_amount, 
            #        hotel=model.Hotel(hotel_id=hotel_id, name=name, stars=stars, 
             #           address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
              #      )
               # ),
                #guest=model.Guest(guest_id=guest_id, first_name=first_name, last_name=last_name, email=email,
                 #   address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code
                  #  )
              #  ),
               # room = model.Room(room_id=room_id, room_number=room_number, price_per_night=price_per_night,
                #    room_type=model.RoomType(type_id=type_id, max_guests=max_guests, description=description),
                 #   hotel=model.Hotel(hotel_id=hotel_id, name=name, stars=stars, 
                  #      address=model.Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
                   # )  
             #   )
            #)
        
        
            #for booking_id, check_in_date, check_out_date, is_cancelled, total_amount,
             #   room_id, room_number, price_per_night, room_type_id,
              #  type_id, max_guests, description,
               # hotel_id, name, stars,
                #address_id, street, city, zip_code,
                #guest_id, first_name, last_name, email in results
        #]

    def calculate_total_price(self, booking: Booking) -> float:
        duration = (booking.check_out_date - booking.check_in_date).days
        return booking.room.price_per_night * duration


#Methode User Story 6
    def read_invoice_by_booking_id(self, booking_id:int)->model.Invoice| None:
        sql = """
        SELECT invoice_id, issue_date, total_amount, i_is_cancelled
        FROM Invoice
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        
        if row:
            invoice_id, issue_date, total_amount, i_is_cancelled = row
            
            # Hole die verknüpften Objekte aus anderen DataAccess-Klassen
            from data_access.booking_data_access import BookingDataAccess
            booking = BookingDataAccess().read_booking_by_id(booking_id)          

            return model.Invoice(
                invoice_id=invoice_id, issue_date=issue_date, total_amount=total_amount, i_is_cancelled=bool(i_is_cancelled), booking=booking, guest=booking.guest, hotel=booking.room.hotel, room=booking.room
                
            )
        
        return None
