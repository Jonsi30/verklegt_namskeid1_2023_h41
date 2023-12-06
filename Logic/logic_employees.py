from data.data_wrapper import Data_wrapper


class LogicEmployees:
    def __init__(self):
        self.employee = Data_wrapper()

    def create_employee(self,name,role,rank,license,phone,address,ssn):
        new_info = name, role, rank, license, phone, address, ssn
        
        return self.employee.create_employee(new_info)
    

    def get_all_employees(self):
        return self.employee.get_all_employees()
        
