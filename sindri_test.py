from data.data_wrapper import Data_wrapper
from model.employee import Employee

class LogicEmployees:
    def __init__(self):
        self.employee = Data_wrapper()


    def get_certain_employee_scedule(self,):
        x = self.employee.get_all_voyages()
        employee_schedule = []
        ssn_input = "1905813249"
        for line in x:
             if line["ssn"] == ssn_input:
                employee_schedule.append["blah"]
        print(employee_schedule)
        