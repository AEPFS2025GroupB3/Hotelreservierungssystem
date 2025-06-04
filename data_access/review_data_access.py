from datetime import date
import model 

class ReviewDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def add_review(self, guest_id, hotel_id, rating, comment, review_date):
        sql="""
        INSERT INTO reviews(guest_id, hotel_id, rating, comment, review_date)
        VALUES (?,?,?,?,?)
        """

    def get_reviews_by_hotel(self,hotel_id):
        sql="""
        SELECT rating, comment, review_date FROM reviews WHERE hotel_id= ?"
        """
        