from data.destination_data import Destination_data
from data.voyage_data import Voyage_Data
from data.employee_data import Employee_data
from data.aircraft_data import Aircraft_Data


class Data_wrapper:
    def __init__(self):
        self.destination_data = Destination_data()
        self.voyage_data = Voyage_Data()
        self.employee_data = Employee_data()
        self.aircraft_data = Aircraft_Data()

    def get_all_destinations(self):
        return self.destination_data.get_all_destination()

    def create_destination(self, dest_input, dest_id_input, dist_input, dura_input, contact_input, contact_nr_input):
        from model.destination import Destination
        return self.destination_data.create_destination(Destination(dest_input, dest_id_input, dist_input, dura_input, contact_input, contact_nr_input))

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
        from model.voyage_model import Voyage_Model

        return self.voyage_data.create_voyage(
            Voyage_Model(
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
        )

    def updated_voyage(self, new_info):
        return self.voyage_data.update_voyage(new_info)

    def get_voyage_data(self):
        """EKKI SNERTA"""
        return self.voyage_data.get_all_voyage()

    def get_all_employees(self):
        return self.employee_data.get_all_employees()

    def create_employee(self, employee_info):
        return self.employee_data.create_employee(employee_info)

    def update_employee(self, ssn_input, role_input, rank_input, License_input, phone_input, address_input, email_input):
        from model.employee import Employee
        return self.employee_data.update_employee(Employee("irr", role_input, rank_input, License_input, phone_input, address_input, email_input, ssn_input))

    def get_all_aircrafts(self):
        return self.aircraft_data.get_all_aircrafts()

    def create_new_aircraft(self, insigna_input, type_input, manu_input, seat_input):
        from model.aircraft_model import Aircraft_Model
        return self.aircraft_data.create_aircraft(Aircraft_Model(insigna_input, type_input, manu_input, seat_input))

    def get_employee_dict(self):
        return self.employee_data.get_employee_dict()

    def update_destination(self, new_info):
        return self.destination_data.update_destination(new_info)

    def get_all_voyages(self):
        return self.voyage_data.get_all_voyage()
    
    def add_voyage_crew(self, voyage_id_input, captain_input, copilot_input, head_of_service_input, flight_attendant_input):
        from model.voyage_model import Voyage_Model
        return self.voyage_data.update_voyage(Voyage_Model(voyage_id_input, "lol", "lol", "lol", "lol", "lol", "lol", "lol", "lol", captain_input, copilot_input, head_of_service_input, flight_attendant_input))
