from data.data_wrapper import Data_wrapper
from model.aircraft_model import Aircraft_Model
from prettytable import PrettyTable

class LogicAircraft:
    def __init__(self):
        self.aircraft = Data_wrapper()

    def create_new_aircraft(self,plane_insignia,plane_type_id,manufacturer,seat_capacity):
        new_info = Aircraft_Model(plane_insignia,plane_type_id,manufacturer,seat_capacity)

        return self.aircraft.create_new_aircraft(new_info)
    
    def get_all_aircrafts(self):
        return self.aircraft.get_all_aircrafts()
    
    def get_available_aircraft(self, date):
        aircrafts = LogicAircraft().get_all_aircrafts()
        voayges = self.aircraft.get_all_voyages()

        date = date[6:]
        

        not_available_planes = []
        for voyage in voayges:
            if voyage.dep_time[6:] == date:
                not_available_planes.append(voyage.plane_insignia)
        available_planes = []
        for aircraft in aircrafts:
            if aircraft.plane_insignia not in not_available_planes:
                available_planes.append(aircraft)

        return available_planes

    def validate_plane_insignia(self, plane_insignia_input) -> bool:
        if len(plane_insignia_input) == 6 :
            if plane_insignia_input[:3] == 'TF-':
                return True
            return False
        return False
    
    def validate_plane_type_id(self, type_input) -> bool:
        if len(type_input) < 20:
            if type_input[:2] == 'NA':
                return True
            return False
        return False
    
    def validate_manu_input(self, manu_input, type_input) -> bool:
        if manu_input in type_input:
            return True
        return False
    
    def validate_seat_input(self, seat_input) -> bool:
        for digit in seat_input:
            if digit.isalpha():
                return False
        return True