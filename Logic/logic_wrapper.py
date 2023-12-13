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
        """Returns a new destination to the destination list"""
        return self.logic_destinations.create_destination()

    def get_all_destinations(self):
        """EKKI SNERTA"""
        return self.logic_destinations.get_all_destinations()

    def update_emergency_contact(self, updated_info):
        """Returns an upadated emergency contact for a destination"""
        return self.logic_destinations.update_emergency_contact(updated_info)

    def create_employee(self, new_info):
        """Returns a new employee to the employee list"""
        return self.logic_employees.create_employee(new_info)

    def get_all_employees(self):
        """Returns all employess"""
        return self.logic_employees.get_all_employees()

    def get_employee_dict(self, ret_dict):
        """Returns all employess in the employee dict"""
        return self.logic_employees.get_employee_dict(ret_dict)

    def update_employee(self, ssn_input,role_input,rank_input,License_input,phone_input,address_input,email_input):
        """Returns an updated employee to the employee list"""
        return self.data_wrapper.update_employee(ssn_input,role_input,rank_input,License_input,phone_input,address_input,email_input)

    def get_all_pilots(self):
        """Returns all pilots"""
        return self.logic_employees.get_all_pilots()
    
    def get_all_cabincrew(self):
        """Return all the cabin crew"""
        return self.logic_employees.get_all_cabin_crew()

    def get_all_crew(self):
        """Returns all crew members"""
        return self.logic_employees.get_all_crew()

    def update_destination(self, new_info):
        """Returns an updated list of destinations"""
        return self.logic_destinations.update_destination_info(new_info)

    def get_voyagelists_from_week(self, year_number, week_number):
        """Takes in a year, and a week for that given year, returns a list of all the voyages in a given week"""
        return self.voyage_logic.get_week_number(year_number, week_number)

    def get_occupied_staff(self):
        """Returns a list of occupied staff"""
        return self.logic_employees.get_occupied_staff()

    def get_available_staff(self, date):
        """Returns a list of available staff"""
        return self.logic_employees.display_available_employees(date)

    def get_by_ssn(self, get_ssn):
        """Returns the employee of given social security number"""
        return self.logic_employees.get_by_ssn(get_ssn)

    def check_if_available(self):
        pass



    # def get_all_voyages(self):
    #     return self.voyage_logic.display_voyage_manager()

    def display_voyage(self):
        """Returns all voyages for the managers so the manager can put staff on voyage"""
        return self.voyage_logic.display_voyage_manager()

    def get_all_aircraft(self):
        """Returns all aircrafts and the info about the aircrafts"""
        return self.logic_aircraft.get_all_aircrafts()

    def get_get_certain_employee_schedule(self):
        return self

    def create_voyage(
        self,
        id_input,
        flight_nr_input,
        dep_from_input,
        arr_at_input,
        dep_time_input,
        dep_time_back_input,
        arr_time_input,
        arr_time_back_input,
        plane_insignia_input,
        captain,
        copilot,
        head_of_service,
        flight_attendant,
    ):
        return Data_wrapper().create_voyage(
            id_input,
            flight_nr_input,
            dep_from_input,
            arr_at_input,
            dep_time_input,
            dep_time_back_input,
            arr_time_input,
            arr_time_back_input,
            plane_insignia_input,
            captain,
            copilot,
            head_of_service,
            flight_attendant,
        )
    
    def add_voyage_crew(self, voyage_id_input, captain_input, copilot_input, head_of_service_input, flight_attendant_input):
        return Data_wrapper().add_voyage_crew(voyage_id_input, captain_input, copilot_input, head_of_service_input, flight_attendant_input)
