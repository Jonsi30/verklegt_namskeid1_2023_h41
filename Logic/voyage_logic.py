from data.data_wrapper import Data_wrapper

class VoyageLogic:
    def __init__(self):
        self.voyage = Data_wrapper

    def create_voyage(self, id, flight_nr, dep_from, arr_at, departure, arrival, plane_insignia, captain ="", copilot ="", head_of_service  ="", flight_attendant =""):
        voyage_info = id,flight_nr,dep_from,arr_at,departure,arrival,plane_insignia,captain,copilot,head_of_service,flight_attendant
        
        return self.voyage.create_voyage(voyage_info)
    
    def get_specific_day_voyage(self):
        pass

    def get_specific_week_voyage(self):
        pass

    # def get_voyage_by_flight_nr(self): MAAAYBE
    #     pass

    def update_voyage(self):
        pass