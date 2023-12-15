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

    def create_destination(self, dest_input, dest_id_input, dist_input, dura_input, contact_input, contact_nr_input):
        """Returns a new destination to the destination list"""
        return self.data_wrapper.create_destination(dest_input, dest_id_input, dist_input, dura_input, contact_input, contact_nr_input)

    def create_employee(self, name_input, role_input, rank_input, License_input, phone_input, address_input, email_input, ssn_input):
        """Returns a new employee to the employee list"""
        return self.data_wrapper.create_employee(name_input, role_input, rank_input, License_input, phone_input, address_input, email_input, ssn_input)
    
    def create_aircraft(self, insigna_input, type_input, manu_input, seat_input):
        """Sends the data from the UI to the Data_wrapper"""
        return self.data_wrapper.create_new_aircraft(insigna_input, type_input, manu_input, seat_input)
    
    def create_voyage(
        self,
        id_input,
        flight_nr_input,
        dep_from_input,
        arr_at_input,
        dep_time_input,
        arr_time_input,
        dep_time_back_input,
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
            arr_time_input,
            dep_time_back_input,
            arr_time_back_input,
            plane_insignia_input,
            captain,
            copilot,
            head_of_service,
            flight_attendant,
        )
    
    def get_employee_week_schedule(self, year_number: int, week_number: int, ssn: str):
        return self.voyage_logic.get_employee_week_schedule(year_number, week_number, ssn)

    def get_all_pilots(self):
        """Returns all pilots"""
        return self.logic_employees.get_all_pilots()
    
    def get_all_crew(self):
        """Returns all crew members"""
        return self.logic_employees.get_all_crew()
    
    
    def get_all_destinations(self):
        """EKKI SNERTA"""
        return self.logic_destinations.get_all_destinations()

    def get_all_cabincrew(self):
        """Return all the cabin crew"""
        return self.logic_employees.get_all_cabin_crew()
    
    def get_all_aircraft(self):
        """Returns all aircrafts and the info about the aircrafts"""
        return self.logic_aircraft.get_all_aircrafts()
    
    def get_all_voyages(self):
        return self.data_wrapper.get_all_voyages()
    
    def get_all_employees(self):
        """Returns all employess"""
        return self.logic_employees.get_all_employees()
    
    
    def get_available_airplanes(self, date):
        return self.logic_aircraft.get_available_aircraft(date)

    def update_employee(self, ssn_input,role_input,rank_input,License_input,phone_input,address_input,email_input):
        """Returns an updated employee to the employee list"""
        return self.data_wrapper.update_employee(ssn_input,role_input,rank_input,License_input,phone_input,address_input,email_input)

    def add_voyage_crew(self, voyage_id_input, captain_input, copilot_input, head_of_service_input, flight_attendant_input):
        return Data_wrapper().add_voyage_crew(voyage_id_input, captain_input, copilot_input, head_of_service_input, flight_attendant_input)


    def update_destination(self, destination_name, dest_id_input, dist_input, dura_input, contact_input, contact_nr_input):
        """Returns an updated list of destinations"""
        return self.data_wrapper.update_destination(destination_name, dest_id_input, dist_input, dura_input, contact_input, contact_nr_input)

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

    def select_position(self, employee_list, table, role, rank):
        return self.voyage_logic.select_position(employee_list, table, role, rank)
    
    def table_making(self, list):
        return self.voyage_logic.table_making(list)
    
    def generate_flight_number(self, dest_id_input):
        """Returns a flight nubmer from the destination ID that the user put in"""
        return self.logic_destinations.generate_flight_number(dest_id_input)

    def display_voyage(self):
        """Returns all voyages for the managers so the manager can put staff on voyage"""
        return self.voyage_logic.display_voyage_manager()

    def get_certain_employee_schedule(self, ssn):
        return self.logic_employees.get_schedule_by_ssn(ssn)

    def date_and_time_formatter(self, departure_time, flight_time):
        return self.voyage_logic.time_formatter(departure_time, flight_time)
    
    def arrival_time_and_date(self, day, month, year, all_hours, all_minutes):
        return self.voyage_logic.arrival_time_and_date(day, month, year, all_hours, all_minutes)
    
    def validate_dest_id_input(self, dest_id_input) -> bool:
        return LogicDestination().validate_dest_id_input(dest_id_input)
    
    def validate_dest_name_input(self, dest_name_input) -> bool:
        return LogicDestination().validate_dest_name_input(dest_name_input)
    
    def validate_dest_distance(self, dest_distance_input) -> bool:
        return LogicDestination().validate_dest_distance(dest_distance_input)
    
    def validate_duration_input(self, dest_duration_input) -> bool:
        return LogicDestination().validate_dest_duration_input(dest_duration_input)
    
    def validate_emergency_contact_name_input(self, emerg_name_input) -> bool:
        return LogicDestination().validate_emergency_contact_name_input(emerg_name_input)
    
    def validate_phone_nr(self, emerg_phone_nr) -> bool:
        return LogicDestination().validate_phone_nr(emerg_phone_nr)
    
    def get_all_dest_ids(self) -> list:
        return LogicDestination().get_all_dest_ids()
    
    def validate_input_id(self, id_input) -> bool:
        return LogicDestination().validate_dest_id_input(id_input)
    
    def validate_employee_name_input(self, name_input) -> bool:
        return LogicEmployees().validate_employee_name_input(name_input)
    
    def validate_employee_role_input(self, role_input) -> bool:
        return LogicEmployees().validate_employee_role_input(role_input)
    
    def validate_employee_rank_input(self, rank_input, role_input) -> bool:
        return LogicEmployees().validate_employee_rank_input(rank_input, role_input)
    
    def validate_employee_license_input(self, license_input, role_input) -> bool:
        return LogicEmployees().validate_license_input(license_input, role_input)
    
    def validate_employee_phone_nr(self, employee_phone_input) -> bool:
        return LogicEmployees().validate_employee_phone_nr(employee_phone_input)
    
    def validate_employee_address(self, address_input) -> bool:
        return LogicEmployees().validate_employee_address(address_input)
    
    def validate_employee_email_address(self, email_input) -> bool:
        return LogicEmployees().validate_employee_email_address(email_input)
    
    def validate_employee_ssn_input(self, ssn_input) -> bool:
        return LogicEmployees().validate_employee_ssn_creation(ssn_input)
    
    def validate_year_input(self, year_input) -> bool:
        return LogicEmployees().validate_year_input(year_input)
    
    def validate_week_input(self, week_input) -> bool:
        return LogicEmployees().validate_week_input(week_input)
    
    def get_employee_role_by_ssn(self, ssn) -> str:
        return LogicEmployees().get_employee_role_by_ssn(ssn)
    
    def get_employee_name_by_ssn(self, ssn) -> str:
        return LogicEmployees().get_employee_name_by_ssn(ssn)
    
    def get_all_employees_ssn(self) -> list:
        return LogicEmployees().get_all_ssn()
    
    def validate_employee_ssn(self, ssn_input) -> bool:
        return LogicEmployees().validate_employee_ssn(ssn_input)
    
    def validate_date_input_format(self, date_input) -> bool:
        return LogicEmployees().validate_date_input_format(date_input)
    
    def get_employee_model_from_ssn(self, ssn_input):
        return LogicEmployees().get_employee_model_from_ssn(ssn_input)
    
    def validate_aircraft_license(self, license_input) -> bool:
        return LogicEmployees().validate_aircraft_license(self, license_input)
    
    def get_all_voyage_ids(self) -> list:
        return VoyageLogic().all_voyage_ids()

    def validate_voyage_id(self, id_input):
        return VoyageLogic().validate_voyage_id_input(id_input)
    
    def validate_voyage_dest(self, dest_input):
        return VoyageLogic().validate_voyage_dest_input(dest_input)
    
    def get_flight_time_from_dest_id(self, arr_at_input):
        return LogicDestination().get_flight_time_from_dest_id(arr_at_input)
    
    def validate_departure_time(self, dep_time):
        return VoyageLogic().validate_departure_time(dep_time)
    
    def validate_dep_time_back(self, arr_time, dep_time_back_input) -> bool:
        return VoyageLogic().validate_dep_time_back(arr_time, dep_time_back_input)
    
    def get_available_plane_insignia(self, available_planes: list) -> list:
        return VoyageLogic().get_available_plane_insignia(available_planes)
    
    def get_unstaffed_voyages(self, upcoming_voyages) -> list:
        return VoyageLogic().get_unstaffed_voyages(upcoming_voyages)
    
    def validate_voyage_user_input_id(self, user_id_input, unstaffed_voyages: list) -> bool:
        return VoyageLogic().validate_voyage_user_input_id(user_id_input, unstaffed_voyages)
    
    def get_voyage_from_id_input(self, id_number):
        return VoyageLogic().get_voyage_from_id_input(self, id_number) 
    
    def get_available_captain_info(self, available_staff):
        return VoyageLogic().get_available_captain_info(available_staff)
    
    def get_available_copilot_info(self, available_staff):
        return VoyageLogic().get_available_copilot_info(available_staff)
    
    def get_available_flight_service_manager_info(self, available_staff):
        return VoyageLogic().get_available_head_of_service_info(available_staff)
    
    def get_available_flight_attendant_info(self, available_staff):
        return VoyageLogic().get_available_flight_attendant_info(available_staff)
    
    def validate_plane_insignia(self, plane_insignia_input) -> bool:
        return LogicAircraft().validate_plane_insignia(plane_insignia_input)
    
    def validate_plane_type_id(self, type_input) -> bool:
        return LogicAircraft().validate_plane_type_id(type_input)
    
    def validate_manu_input(self, manu_input, type_input) -> bool:
        return LogicAircraft().validate_manu_input(manu_input, type_input)
    
    def validate_seat_input(self, seat_input) -> bool:
        return LogicAircraft().validate_seat_input(seat_input)