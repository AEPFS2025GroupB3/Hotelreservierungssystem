from datetime import date

class Review:
    def __init__(self, review_id: int, rating: int, comment: str, review_date: date):

        if not review_id: #Sicherstellen das eine review_id übergeben wurde
            raise ValueError("review_id is required")
        if not isinstance(review_id, int): #Sicherstellen das review_id eine Zahl ist
            raise ValueError("review_id must be an integer")

        if not rating: #Sicherstellen das ein rating übergeben wurde
            raise ValueError("rating is required")
        if not isinstance(rating, int): #Sicherstellen das rating eine Zahl ist
            raise ValueError("rating must be an integer")

        if not comment: #Sicherstellen das comment übergeben wurde
            raise ValueError("comment is required")
        if not isinstance(comment, str): #Sicherstellen das comment einen String ist
            raise ValueError("comment must be a string")

        if not review_date: #Sicherstellen das Datum übergeben wurde
            raise ValueError("review date is required")
        if not isinstance(review_date, date):
            raise ValueError("review date must be a date")

    
    #Private Attribute erstellen, damit niemand von aussen Unsinn macht :)
        self.__review_id: int = review_id
        self.__rating: int = rating
        self.__comment: str = comment
        self.__review_date: date = review_date

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
        if value < 1 or value >5:
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

    #Methoden erstellen
    

    #Review updaten
    def update_review(self, new_rating: int, new_comment: str):
        if not isinstance(new_rating, int): #prüft, ob Rating Zahl
            raise ValueError("rating must be an integer")
        if not isinstance(new_comment, str): #prüft, ob Comment String
            raise ValueError("comment must be a string")
        
        self.rating = new_rating #Aufruf setter, setzt neuen Wert rating
        self.comment = new_comment #Aufruf setter, setzt neuen Wert Comment
        return "Review updated."

    #Review löschen
    def delete_review(self):
        self.__rating = None #None = keinen Wert mehr vorhanden
        self.__comment = "" #Kommentar auf leeren Text setzen
        self.review_date = None #None = keinen Wert mehr vorhanden
        return "Review deleted."

    #Review Details anschauhen
    def get_review_details(self): #gibt Daten in formatierten String zurück
        return(
            f"Review ID: {self.__review_id}, "
            f"Rating: {self.__rating}, "
            f"Comment: {self.__comment}, "
            f"Date: {self.__review_date}"
        )


#warum bei __init__ & property.setter ValueError
#__init__ : einmalige Prüfung beim erstellen
#@property.setter: wiederholge Prüfung bei änderungen