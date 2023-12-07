from data.data_wrapper import Data_wrapper


class LogicEmployees:
    def __init__(self):
        self.employee = Data_wrapper()

    def create_employee(self,name,role,rank,license,phone,address,ssn):
        new_info = name, role, rank, license, phone, address, ssn
        
        return self.employee.create_employee(new_info)
    
    def get_all_employees(self):
        return self.employee.get_all_employees()
    
    def update_employee(self, new_info):
        

        return self.employee.update_employee(new_info)
    
    def get_all_pilots(self,name,role,license):
        pilot_info = name, role, license

        return self.employee.get_all_pilots(pilot_info)
    
    def get_all_crew(self,name,role,rank):
        crew_info = name, role, rank

        return self.employee.get_all_crew(crew_info)
    
    def get_occupied_staff(self):
        pass

    def get_available_staff(self):
        pass
    
    def get_by_ssn(self,ssn):
        get_ssn = ssn
        
        return self.employee.get_by_ssn(get_ssn)

    def check_if_available(self):
        pass

    

        
