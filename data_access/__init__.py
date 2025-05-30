from datetime import date, datetime
import sqlite3

from .base_data_access import BaseDataAccess
#from .address_data_access import AddressDataAccess
from .booking_data_access import BookingDataAccess
#from .facility_data_access import FacilityDataAccess
from .guest_data_access import GuestDataAccess
from .hotel_data_access import HotelDataAccess
from .invoice_data_access import InvoiceDataAccess
#from .review_data_access import ReviewDataAccess
from .room_data_access import RoomDataAccess
from .room_type_data_access import RoomTypeDataAccess

def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)
## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)
