from datetime import datetime
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel
import data_access
from data_access.review_data_access import ReviewDataAccess

class ReviewManager:
    def __init__(self) -> None:
        self.__review_da = data_access.ReviewDataAccess()

    #User Storys DB Schemaänderung
    #Generische Hilfsmethode prüft ob ein übergebener value eine positive Ganzzahl ist
    def __validate_id(self, value: int, name:str):
        if not isinstance(value, int) or value <1:
            raise ValueError(f"{name} muss eine positive Ganzzahl sein." )

    def __validate_rating(self, rating: int):
        if rating < 1 or rating > 5:
            raise ValueError("Bewertung muss zwischen 1 und 5 liegen.")

    def __validate_comment(self, comment: str):
        if not comment or not comment.strip():
            raise ValueError("Kommentar darf nicht leer sein.")

    def __validate_name(self, name: str):
        if not name or not name.strip():
            raise ValueError("Hotelname darf nicht leer sein.")


    def add_review(self, guest_id: int, hotel_id: int, rating: int, comment: str, review_date=None):
        self.__validate_id(guest_id, "Gast-ID")
        self.__validate_id(hotel_id, "Hotel-ID")
        self.__validate_rating(rating)
        self.__validate_comment(comment)
        
        if review_date is None:
            review_date = datetime.now().strftime('%Y-%m-%d')
        
        self.__review_da.add_review(guest_id, hotel_id, rating, comment, review_date)

    def get_reviews_by_hotel(self, name):
        self.__validate_name(name)
        return self.__review_da.get_reviews_by_hotel(name)
        