from data.destination_data import Destination_data
from data.voyage_data import GetData
from data.employee_data import Employee_data


class Data_wrapper:
    def __init__(self):
        self.destination_data = Destination_data()
        self.voyage_data = GetData()
        self.employee_data = Employee_data()
    def get_all_destinations(self):
        return self.destination_data.get_all_destination()

    def create_destination(self, new_destination):
        return self.destination_data.create_destination(new_destination)

    def get_voyage_data(self):
        return self.voyage_data.get_voyage_data()

    def get_all_employees(self):
        return self.employee_data.get_all_employees()

    def create_employee(self, employee_info):
        return self.employee_data.create_employee(employee_info)
