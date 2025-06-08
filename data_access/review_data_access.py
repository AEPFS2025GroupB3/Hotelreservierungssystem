from datetime import date
import model 

from data_access.base_data_access import BaseDataAccess

class ReviewDataAccess(BaseDataAccess): #Vererbung der Basisklasse
    def __init__(self, db_path: str = None): #db_path ist Pfad zur DB Datei (wird kein Wert übergeben, ist None der Stadardwert)
        super().__init__(db_path) #Übergibt db_path an die Basisklasse

    def add_review(self, guest_id, hotel_id, rating, comment, review_date):
        sql="""
        INSERT INTO Review (guest_id, hotel_id, rating, comment, review_date)
        VALUES (?,?,?,?,?)
        """
        params=(guest_id, hotel_id, rating, comment, review_date)
        self.execute(sql,params)

    def get_reviews_by_hotel(self,hotel_id) -> list[model.Review]: #Methode User Story mit DB Schemaänderung geschaut von Refernce Projekt track_Data_access 103
        sql="""
        SELECT r.review_id, r.rating, r.comment, r.review_date, 
        g.guest_id, g.first_name, g.last_name, g.email, 
        a.street, a.city, a.zip_code, a.address_id, 
        h.hotel_id, h.name, h.stars,
        ad.street, ad.city, ad.zip_code, ad.address_id
        FROM Review r 
        JOIN Guest g ON r.guest_id = g.guest_id
        JOIN Address a ON g.address_id = a.address_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address ad ON h.address_id = ad.address_id
        WHERE r.hotel_id = ?
        """
        params = (hotel_id,)
        rows = self.fetchall(sql, params)

        return [
            model.Review(
                review_id =review_id,
                rating=rating,
                comment=comment,
                review_date=review_date,
                guest=model.Guest(
                    guest_id=guest_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    address=model.Address(
                        street=street,
                        city=city,
                        zip_code=zip_code,
                        address_id=address_id,
                    )
                ),
                hotel=model.Hotel(
                    hotel_id=hotel_id,
                    name=name,
                    stars=stars,
                    address=model.Address(
                        street=street,
                        city=city,
                        zip_code=zip_code,
                        address_id=address_id,
                    )   
                )
            )
        for review_id, rating, comment, review_date, guest_id, first_name, last_name, email, street, city, zip_code, address_id, hotel_id, name, street, city, zip_code, address_id, hotel_id in rows #jede Zeile in diese Variablen packen
        ]
