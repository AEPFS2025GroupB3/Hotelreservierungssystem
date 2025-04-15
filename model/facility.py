class Facility: #Klasse Facility erstellen
    def __init__(self, facility_id: int, facility_name: string):
        self.facility_id = facility_id
        self.facility_name = facility_name

    def get_facility_name(self):
        return f" Der Name der Einrichtung lautet: {self.facility_name}"