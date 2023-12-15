from data.data_wrapper import Data_wrapper
from model.employee import Employee
from prettytable import PrettyTable
from datetime import datetime
from logic.logic_aircraft import LogicAircraft

class LogicEmployees:
    def __init__(self):
        self.employee = Data_wrapper()

    def create_employee(self, name, role, rank, license, phone, address, email, ssn):
        """Returns all the credentials of a new employee."""
        new_info = Employee(name, role, rank, license, phone, address, email, ssn)
        return self.employee.create_employee(new_info)

    def get_all_employees(self):
        """Returns all the employees that work for the company NaN air."""
        return self.employee.get_all_employees()

    def update_employee(self, new_info):
        """Returns the info needed to update a particular employee"""
        return self.employee.update_employee(new_info)

    def get_all_pilots(self):
        """Returns a list with all the pilots working for the company NaN air."""
        pilot_list = []

        all_employees = Data_wrapper().get_all_employees()
        for employee in all_employees:
            if employee.role == "Pilot":
                pilot_list.append(
                    [employee.name, employee.role, employee.rank, employee.license]
                )

        return pilot_list

    def get_all_cabin_crew(self):
        "Returns a list with all the cabin crew working for the company Nan Air"
        cabin_crew = []
        all_employees = Data_wrapper().get_all_employees()
        for employee in all_employees:
            if employee.role == "Cabincrew":
                cabin_crew.append([employee.name, employee.rank])

        return cabin_crew

    def get_all_crew(self):
        """Returns a list with all the crew members working for the company NaN air."""
        crew_list = []

        for employee in Data_wrapper().get_all_employees():
            crew_list.append(employee)

        return crew_list

    def get_employee_info(self, employee_name: str):
        """Returns a particlar employee and his attributes in a list. If the list is empty then no employee name matched the employess in the company"""
        employee_list = []

        for employee in Data_wrapper().get_all_employees():
            if employee_name == employee.name:
                employee_list.append(employee)
            else:
                pass

        return employee_list

    def get_occupied_staff(self, employee_dict: dict, employee_status: str):
        """Returns all occupied staff. Staff that cannot go on more voyages at the given time"""
        occupied_list = []

        for employee in employee_dict:
            if employee["occupied"] == employee_status:
                occupied_list.append(employee)
            else:
                pass
        return occupied_list

    def get_all_ssn(self):
        all_ssn = []
        for employee in LogicEmployees().get_all_employees():
            all_ssn.append(employee.ssn)
        return all_ssn


    def display_available_employees(self, date):
        """Takes in date in this format: '21:00 16.12.2023'"""
        """Returns a list of available employees for that particular date"""
        not_available_employees = []

        for voyage in Data_wrapper().get_all_voyages():
            if date == voyage.arr_time_back[6:]:
                if voyage.captain != "Unassigned":
                    not_available_employees.append(voyage.captain)
                if voyage.copilot != "Unassigned":
                    not_available_employees.append(voyage.copilot)
                if voyage.head_of_service != "Unassigned":
                    not_available_employees.append(voyage.head_of_service)
                if voyage.flight_attendant != "Unassigned":
                    not_available_employees.append(voyage.flight_attendant)
        non_available = list(dict.fromkeys(not_available_employees).keys())
        available_employees = LogicEmployees().get_available_employees(non_available)

        return available_employees

    def get_available_employees(self, name_list):
        availabe_employees = []
        all_employees = Data_wrapper().get_all_employees()
        for name in all_employees:
            if name.name not in name_list:
                availabe_employees.append([name.name, name.role, name.rank])
        return availabe_employees

    def get_by_ssn(self, ssn):
        """Returns the employee with the ssn that the user put in. If no employee has that ssn, the function returns None"""
        employee_ssn = []
        for employee in Data_wrapper().get_all_employees():
            if employee.ssn == ssn:
                employee_ssn.append(employee)
            else:
                pass

        return employee_ssn

    def get_schedule_by_ssn(self, ssn):
        all_voyages = Data_wrapper().get_all_voyages()
        all_employees = Data_wrapper().get_all_employees()
        name = ""
        role = ""
        for employee in all_employees:
            if employee.ssn == ssn:
                name += employee.name
                role += employee.role

        voyages = []

        for voyage in all_voyages:
            if (
                name in voyage.captain
                or name in voyage.copilot
                or name in voyage.head_of_service
                or name in voyage.flight_attendant
            ):
                voyages.append(voyage)

        fieldnames = [
            "Voyage Id",
            "Employee",
            "Role",
            "Departure Time",
            "Arrival Time Back",
            "Destination",
        ]

        if voyages:
            work_scheadule = PrettyTable()
            work_scheadule.field_names = fieldnames
            for work in voyages:
                work_scheadule.add_row(
                    [
                        work.id,
                        name,
                        role,
                        work.dep_time,
                        work.arr_time_back,
                        work.arr_at,
                    ]
                )

            return work_scheadule

        return f"{name} doesn't have any upcoming voayges!"

    def validate_employee_name_input(self, dest_name_input) -> bool:
        """Lenght must be below 20 letters and over 4 letters str"""
        if len(dest_name_input) < 40 and len(dest_name_input) > 4:
            
            for letter in dest_name_input:
                if letter.isdigit():
                    return False
            return True
        return False
    
    def validate_employee_role_input(self, role_input) -> bool:

        if role_input != "Pilot" and role_input != "Cabincrew" and role_input != "":
            return False
        return True
    
    def validate_employee_rank_input(self, rank_input, role_input) -> bool:

        if role_input == 'Pilot':
            if rank_input == 'Copilot' or rank_input == 'Captain':
                return True
            return False

        if role_input == 'Cabincrew':
            if rank_input == 'Flight Service Manager' or rank_input == 'Flight Attendant':
                return True
            return False
        else:
        
            return False
        
    def validate_license_input(self, license_input, role_input) -> bool:
        aircraft_ids = []
        all_aircrafts = Data_wrapper().get_all_aircrafts()
        for aircraft in all_aircrafts:
            aircraft_ids.append(aircraft.plane_type_id)

        if role_input == 'Cabincrew' and license_input == 'N/A':
            return True
        
        if role_input == 'Pilot' and license_input in aircraft_ids:
            return True
        
        else:
            return False
        

    def validate_employee_phone_nr(self, employee_phone_nr_input) -> bool:
        """Emergency contact phone number can't include letters"""
        
        if len(employee_phone_nr_input) == 7:
            for number in employee_phone_nr_input:
                 if number.isalpha():
                    return False
            return True       
        return False
    
    def validate_employee_address(self, address_input) -> bool:
        """Address must be more than 3 letters and less than 30, address doesn't have
        to include numeric values, fx. if employee lives in the countryside"""

        if len(address_input) < 30 and len(address_input) > 3:
            return True
        
        return False
    
    def validate_employee_email_address(self, email_input) -> bool:

        if email_input[7:] == '@nan.is' and len(email_input) > 8:
            return True
        
        return False
    
    def validate_employee_ssn_creation(self, ssn_input) -> bool:

        if len(ssn_input) == 10:
            for digit in ssn_input:
                if digit.isalpha():
                    return False
                
            return True
        return False
    
    def validate_year_input(self, year_input) -> bool:

        try:
            year_input = int(year_input)
            if year_input >= 2023 and year_input <= 2026:
                year_input = str(year_input)
                for digit in year_input:
                    if digit.isalpha():
                        return False
                    
                return True
            return False
        except ValueError:
            return False
    
    def validate_week_input(self, week_input) -> bool:

        try:
            week_input = int(week_input)
            if week_input >= 1 and week_input <= 52:
                week_input = str(week_input)
                for digit in week_input:
                    if digit.isalpha():
                        return False
                
                return True

            return False
        except ValueError:
            return False
    
    def get_employee_name_by_ssn(self, ssn) -> str:
        name = ""
        all_employees = LogicEmployees().get_all_employees()
        for employee in all_employees:
            if employee.ssn == ssn:
                name += employee.name

        return name
    
    def get_employee_role_by_ssn(self, ssn) -> str:
        role = ""
        all_employees = LogicEmployees().get_all_employees()
        for employee in all_employees:
            if employee.ssn == ssn:
                role += employee.role

        return role
    
    def validate_employee_ssn(self, ssn_input) -> bool:

        for employee in LogicEmployees().get_all_employees():
            if ssn_input == employee.ssn:
                return True
        return False
    
    def validate_date_input_format(self, date_input) -> bool:
        """Input date must be in this format: DD.MM.YYYY"""
        try:
            if len(date_input) == 10:
                if date_input[2] == "." and date_input[5] == ".":
                    for letter in date_input:
                        if letter.isalpha():
                            return False
                        day = date_input[0]+date_input[1]
                        month = date_input[3]+date_input[4]
                        year = date_input[6:]
                        datetime(int(year), int(month), int(day))
                        
                        return True
                return False       
            return False
        except ValueError:
            """datetime function return ValueError if invalid date"""
            return False
        
    def get_employee_model_from_ssn(self, ssn_input):
        """Returns the employee model that matches the ssn"""
        for employee in self.get_all_employees():
            if employee.ssn == ssn_input:
                return (employee)
            
    def validate_aircraft_license(self, license_input):
        """Check if aircraft license from input exists"""

        for aircraft in LogicAircraft().get_all_aircrafts():
            if aircraft.plane_type_id == license_input:
                return True
        return False