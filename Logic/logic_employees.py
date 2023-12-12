from data.data_wrapper import Data_wrapper
from model.employee import Employee
from prettytable import PrettyTable

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

    def get_all_pilots(self: dict):
        """Returns a list with all the pilots working for the company NaN air."""
        pilot_list = []
        fieldnames = ["Employee", "Rank"]
        table = PrettyTable()
        all_employees = Data_wrapper().get_all_employees()
        for employee in all_employees:
            if employee.role == "Pilot":
                pilot_list.append([employee.name, employee.rank])

        return pilot_list
        

    def get_all_crew(self, employee_dict: dict):
        """Returns a dictionary with all the crew members working for the company NaN air."""
        crew_dict = {}

        for employee in employee_dict:
            if employee["role"] == "cabin crew":
                crew_dict[employee["name"]] = employee["rank"]

        return crew_dict

    def get_employee_info(self, employee_dict: dict, employee_name: str):
        """Returns a particlar employee and his attributes in a list. If the list is empty then no employee name matched the employess in the company"""
        employee_list = []

        for employee in employee_dict:
            if employee["name"] == employee_name:
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

    def get_available_staff(self, employee_dict: dict, employee_status):
        """Returns all available staff. Staff that can go on voyages at the given time"""
        available_staff_list = []

        for employee in employee_dict:
            if employee["avialable"] == employee_status:
                available_staff_list.append(employee)
            else:
                pass
        return available_staff_list

    def get_by_ssn(self, employee_dict: dict, ssn: int):
        """Returns the employee with the ssn that the user put in. If no employee has that ssn, the function returns None"""

        for employee in employee_dict:
            if employee["Social Security Number"] == ssn:
                return employee
            else:
                pass

        return None

    def check_if_available(self):
        pass

    def get_employee_dict(self, ret_dict):
        """Returns a dictionary with all the employees that work for the company NaN air."""
        return self.employee.get_employee_dict(ret_dict)

    def get_certain_employee_scedule(self, past_flights):
        employee_schedule = []
        ssn_input = 1905813249
        for employee in past_flights:
            if employee["ssn"] == ssn_input:
                employee_schedule.append["blah"]
        print(employee_schedule)
