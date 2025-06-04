from datetime import date
import model
from model.booking import Booking
from model.guest import Guest
from model.hotel import Hotel


import data_access #Importiert data_access

class ReviewManager:
    def __init__(self) -> None:
        self.__review_da = data_access.ReviewDataAccess()

    def submit_review(self, guest_id, hotel_id, rating, comment):
        review_date = datetime.now().strftime('%Y-%m-%d')
        self.review_data_access.add_review(guest_id, hotel_id, rating, comment, review_date)

    def get_reviews_by_hotel(self, hotel_id):
        return self.review_data_access.get_reviews_by_hotel(hotel_id)