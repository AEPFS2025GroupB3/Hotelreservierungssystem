class Booking:
    # Konstruktor für ein neues Booking-Objekt
    def __init__(self, booking_id: int, check_in_date: str, check_out_date: str, booking_status: str):
        if not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")
        if not check_in_date or not check_out_date:
            raise ValueError("Both check_in_date and check_out_date are required")
        if not booking_status:
            raise ValueError("booking_status is required")

        self.__booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = booking_status

    # Getter für booking_id
    @property
    def booking_id(self):
        return self.__booking_id

    # Getter & Setter für check_in_date
    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value

    # Getter & Setter für check_out_date
    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        self.__check_out_date = value

    # Getter & Setter für booking_status
    @property
    def booking_status(self):
        return self.__booking_status

    @booking_status.setter
    def booking_status(self, value):
        self.__booking_status = value

    # Methode zum Stornieren der Buchung
    def cancel(self):
        self.booking_status = "Canceled"

    # Methode zur Berechnung der Gesamtkosten (Platzhalter für später)
    def calculate_total(self) -> float:
        # Hier würde normalerweise der Preis aus Zimmerdaten kommen
        return 0.0  # Platzhalterwert

    # Methode zur retournierungder Buchungsdaten
    def get_booking_dates(self) -> str:
        return f"Check-in: {self.check_in_date}, Check-out: {self.check_out_date}"

    # Methode zur retournierung des Status
    def get_booking_status(self) -> str:
        return self.booking_status