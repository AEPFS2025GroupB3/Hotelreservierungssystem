from datetime import date
import model #Klassen importieren
from model import Booking, Guest, Hotel, Invoice
import data_access #Importiert data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.HotelDataAccess()
        
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
 