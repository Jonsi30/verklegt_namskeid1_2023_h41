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
