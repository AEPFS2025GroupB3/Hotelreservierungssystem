from datetime import date
import model
from data_access.base_data_access import BaseDataAccess
 
class InvoiceDataAccess(BaseDataAccess):
    def __init__(self) -> None:
        self.__invoice_da = data_access.InvoiceDataAccess()
