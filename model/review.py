from datetime import date
from model.hotel import Hotel
from model.guest import Guest

class Review:
    def __init__(self, review_id: int, rating: int, comment: str, review_date: date, hotel: Hotel, guest: Guest):

        if not review_id: #Sicherstellen das eine review_id übergeben wurde
            raise ValueError("review_id is required")
        if not isinstance(review_id, int): #Sicherstellen das review_id eine Zahl ist
            raise ValueError("review_id must be an integer")

        if not isinstance(rating, int):
            raise ValueError("rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")

        if not comment: #Sicherstellen das comment übergeben wurde
            raise ValueError("comment is required")
        if not isinstance(comment, str): #Sicherstellen das comment einen String ist
            raise ValueError("comment must be a string")

        if not review_date: #Sicherstellen das Datum übergeben wurde
            raise ValueError("review date is required")
        if not isinstance(review_date, date):
            raise ValueError("review date must be a date")

        if not hotel:
            raise ValueError("hotel is required")
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel must be a Hotel object")

        if not guest:
            raise ValueError("guest is required")
        if not isinstance(guest, Guest):
            raise ValueError("guest must be a Guest object")

    #Private Attribute erstellen, damit niemand von aussen Unsinn macht :)
        self.__review_id: int = review_id
        self.__rating: int = rating
        self.__comment: str = comment
        self.__review_date: date = review_date
        self.__hotel: Hotel = hotel
        self.__guest: Guest = guest

    #Properties
    #ich habe zu jedem Attribut eine Property erstellt damit der Code konsistent ist

    @property #lesbar (getter) aber nicht änderbar, kein Setter weil ID bleibt fix
    def review_id(self):
        return self.__review_id

    @property #darf geändert werden, muss aber noch geprüft werden (getter & setter)
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise ValueError("rating must be an integer")
        if not (1 <= value <= 5):
            raise ValueError("rating must be between 1 and 5")
        self.__rating = value
    
    @property #darf geändert werden, muss aber noch geprüft werden (getter & setter)
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        if not value:
            raise ValueError("comment is required")
        if not isinstance(value, str):
            raise ValueError("comment must be a string")
        self.__comment = value

    @property #lesbar (getter) aber nicht änderbar, kein Setter weil Datum bleibt fix
    def review_date(self):
        return self.__review_date

    @property
    def hotel(self):
        return self.__hotel

    @property
    def guest(self):
        return self.__guest

    #Methoden erstellen
    #Review updaten
    def update_review(self, new_rating: int, new_comment: str):
        # Ermöglicht die nachträgliche Anpassung der Bewertung
        self.rating = new_rating
        self.comment = new_comment
        return "Review updated."

    #Review löschen
    def delete_review(self):
        self.__rating = None #None = keinen Wert mehr vorhanden
        self.__comment = "" #Kommentar auf leeren Text setzen
        self.__review_date = None #None = keinen Wert mehr vorhanden
        return "Review deleted."

    #Review Details anschauhen
    def get_review_details(self) -> str:
        # Gibt formatierte Übersicht über die Bewertung zurück
        return (
            f"Review ID: {self.review_id} – Bewertung: {self.rating}/5\n"
            f"{self.comment}\n"
            f"Verfasst am {self.review_date} von {self.guest.first_name} {self.guest.last_name} "
            f"für {self.hotel.name}"
        )

    
#warum bei __init__ & property.setter ValueError
#__init__ : einmalige Prüfung beim erstellen
#@property.setter: wiederholge Prüfung bei änderungen