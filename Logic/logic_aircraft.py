from data.data_wrapper import Data_wrapper

class LogicAircraft:
    def __init__(self):
        self.aircraft = Data_wrapper()

    def create_new_aircraft(self,plane_insignia,plane_type_id,manufacturer,seat_capacity):
        new_info = plane_insignia,plane_type_id,manufacturer,seat_capacity

        return self.aircraft.create_new_aircraft(new_info)
    
    def get_all_aircrafts(self):
        return self.aircraft.get_all_aircrafts()