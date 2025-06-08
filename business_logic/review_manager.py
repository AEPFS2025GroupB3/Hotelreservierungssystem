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

    def add_review(self, guest_id, hotel_id, rating, comment, review_date):
        review_date = datetime.now().strftime('%Y-%m-%d')
        self.__review_da.add_review(guest_id, hotel_id, rating, comment, review_date)

    def get_reviews_by_hotel(self, name):
        self.__review_da.get_reviews_by_hotel(name)