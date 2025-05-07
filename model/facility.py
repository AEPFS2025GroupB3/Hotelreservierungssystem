class Facility: #Klasse Facility erstellen
    def __init__(self, facility_id: int, facility_name: str):

        if not facility_id: #Kontrolliert, dass id angegeben wurde
            raise ValueError("facility_id is required")
        if not isinstance(facility_id, int): #Kontrolliert, dass id ein integer ist
            raise ValueError("facility_id must be an integer")

        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise ValueError("facility_name must be a string")

        #Private Attribute zuweisen
        self.__facility_id: int = facility_id
        self.__facility_name: str = facility_name

    #Gibt die id zurück
    @property
    def facility_id(self):
        return self.__facility_id

    #Gibt den Namen der Einrichtung zurück
    @property 
    def facility_name(self):
        return self.__facility_name

    @facility.setter
    def facility_name(self, value):
        if not value:
            raise ValueError("facility_name is required")
        if not isinstance(value, str):
            raise ValueError("facility_name must be a string")
        self.__facility_name 