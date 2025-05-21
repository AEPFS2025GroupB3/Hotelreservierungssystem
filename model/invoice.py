from model.booking import Booking

class Invoice:
    # Konstruktor zur Initialisierung eines neuen Invoice-Objekts
    def __init__(self, invoice_id: int, issue_date: str, total_amount: float, invoice_status: str):
        if not isinstance(invoice_id, int):
            raise ValueError("invoice_id must be an integer")
        if not issue_date:
            raise ValueError("issue_date is required")
        if not isinstance(total_amount, (float, int)):
            raise ValueError("total_amount must be a number")
        if not invoice_status:
            raise ValueError("invoice_status is required")

        self.__invoice_id = invoice_id  # Private Variable (keine Änderung erlaubt)
        self.issue_date = issue_date    # wird via Setter gesetzt
        self.total_amount = total_amount
        self.invoice_status = invoice_status
        self.__booking = booking

    # Getter für invoice_id
    @property
    def invoice_id(self):
        return self.__invoice_id

    # Getter & Setter für issue_date
    @property
    def issue_date(self):
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, value):
        if not value:
            raise ValueError("issue_date is required")
        self.__issue_date = value

    # Getter & Setter für total_amount
    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        if value < 0:
            raise ValueError("total_amount cannot be negative")
        self.__total_amount = value

    # Getter &Setter für invoice_status
    @property
    def invoice_status(self):
        return self.__invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        if not value:
            raise ValueError("invoice_status is required")
        self.__invoice_status = value

    #Komposition zwischen Invoice und Booking
    @property
    def booking(self):
        return self.__booking

    # Methode zur retournierung des Gesamtbetrags
    def get_total_amount(self) -> float:
        return self.total_amount

    # ethode zurretournierung des Rechnungsdatums
    def get_invoice_date(self) -> str:
        return self.issue_date

    # methode zur retournierung des Rechnungsstatus
    def get_invoice_status(self) -> str:
        return self.invoice_status

    # Methode zur retournierung einer Storno-Benachrichtigung
    def get_canceled_invoice(self) -> str:
        if self.invoice_status.lower() == "canceled":
            return f"Rechnung {self.invoice_id} wurde storniert."
        return f"Rechnung {self.invoice_id} ist aktiv."