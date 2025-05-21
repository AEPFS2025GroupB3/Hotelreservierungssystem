class AdminManager:
    def __init__(self):
        self.__room_da = RoomDataAccess()
        self.__facility_da = FacilityDataAccess()
        self.__roomtype_da = RoomTypeDataAccess()
    
    # --- Facility ---
    def create_facility(self, name: str):
        return self.__facility_da.create_facility(name)

    def update_facility_name(self, facility_id: int, new_name: str):
        return self.__facility_da.update_facility_name(facility_id, new_name)

    def delete_facility(self, facility_id: int):
        return self.__facility_da.delete_facility(facility_id)
    
    # --- RoomType ---
    def create_room_type(self, description: str, max_guests: int):
        return self.__roomtype_da.create_room_type(description, max_guests)

    def update_room_type(self, room_type_id: int, new_description: str, new_max_guests: int):
        return self.__roomtype_da.update_room_type(room_type_id, new_description, new_max_guests)

    def delete_room_type(self, room_type_id: int):
        return self.__roomtype_da.delete_room_type(room_type_id)
    
    # --- Room ---
    def update_room_price(self, room_id: int, new_price: float):
        return self.__room_da.update_room_price(room_id, new_price)

    def update_seasonal_factor(self, room_id: int, new_factor: float):
        return self.__room_da.update_seasonal_factor(room_id, new_factor)
