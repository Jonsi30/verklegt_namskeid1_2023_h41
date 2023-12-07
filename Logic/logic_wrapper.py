from logic.logic_aircraft import LogicAircraft
from logic.logic_destination import LogicDestination
from data.data_wrapper import Data_wrapper
from logic.voyage_logic import VoyageLogic
from logic.logic_employees import LogicEmployees


class Logic_wrapper:
    def __init__(self):
        self.logic_destinations = LogicDestination()
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic()
        self.logic_employees = LogicEmployees()
        self.logic_aircraft = LogicAircraft()

    def create_destination(self):
        return self.logic_destinations.create_destination()

    def get_all_destinations(self):
        """EKKI SNERTA"""
        return self.logic_destinations.get_all_destinations()

    def update_emergency_contact(self, updated_info):
        return self.logic_destinations.update_emergency_contact(updated_info)

    def create_employee(self, new_info):
        return self.logic_employees.create_employee(new_info)

    def get_all_employees(self):
        return self.logic_employees.get_all_employees()
    
    def get_employee_dict(self,ret_dict):
        return self.logic_employees.get_employee_dict(ret_dict)
    
    def update_employee(self, updated_info):
        return self.logic_employees.update_employee(updated_info)

    def get_all_pilots(self):
        return self.logic_employees.get_all_pilots()

    def get_all_crew(self):
        return self.logic_employees.get_all_crew()

    def update_destination(self, new_info):
        return self.logic_destinations.update_destination_info(new_info)

    def get_occupied_staff(self):
        pass

    def get_available_staff(self):
        pass

    def get_by_ssn(self, get_ssn):
        return self.logic_employees.get_by_ssn(get_ssn)

    def check_if_available(self):
        pass

    def get_all_voyages(self):
        return self.voyage_logic.get_flight()
