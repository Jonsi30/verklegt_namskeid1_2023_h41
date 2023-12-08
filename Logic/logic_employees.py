from data.data_wrapper import Data_wrapper


class LogicEmployees:
    def __init__(self):
        self.employee = Data_wrapper()

    def create_employee(self,name,role,rank,license,phone,address,email,ssn):
        new_info = name, role, rank, license, phone, address, email, ssn
        return self.employee.create_employee(new_info)
    
    def get_all_employees(self):
        return self.employee.get_all_employees()
    
    def update_employee(self, new_info):
        return self.employee.update_employee(new_info)
    
    def get_all_pilots(self,employee_dict):
        pilot_dict = {}
        
        for employee in employee_dict:
            if employee ["role"] == "pilot":
                pilot_dict[employee["name"]] = employee["rank"]
        
        return pilot_dict

    
    def get_all_crew(self,employee_dict):
        crew_dict = []

        for employee in employee_dict:
            if employee ["role"] == "cabin crew":
                crew_dict[employee["name"]] = employee["rank"]
        
        return crew_dict
    
    def get_occupied_staff(self):
        pass

    def get_available_staff(self):
        pass
    
    def get_by_ssn(self,employee_dict,ssn):
        
        for employee in employee_dict:
            if employee ["ssn"] == ssn:
                return employee
            else:
                pass
        return None

    def check_if_available(self):
        pass

    def get_employee_dict(self, ret_dict):
        return self.employee.get_employee_dict(ret_dict)

        
