from data.data_wrapper import Data_wrapper


class LogicEmployees:
    def __init__(self):
        self.employee = Data_wrapper()

    def create_employee(self,name,role,rank,license,phone,address,email,ssn):
        """Returns all the credentials of a new employee."""
        new_info = name, role, rank, license, phone, address, email, ssn
        return self.employee.create_employee(new_info)
    
    def get_all_employees(self):
        """Returns all the employees that work for the company NaN air."""
        return self.employee.get_all_employees()
    
    def update_employee(self, new_info):
        """Returns the info needed to update a particular employee"""
        return self.employee.update_employee(new_info)
    
    def get_all_pilots(self,employee_dict: dict):
        """Returns a dictionary with all the pilots working for the company NaN air."""
        pilot_dict = {}
        
        for employee in employee_dict:
            if employee["role"] == "pilot":
                pilot_dict[employee["name"]] = employee["rank"]
        
        return pilot_dict

    
    def get_all_crew(self,employee_dict: dict):
        """Returns a dictionary with all the crew members working for the company NaN air."""
        crew_dict = {}

        for employee in employee_dict:
            if employee["role"] == "cabin crew":
                crew_dict[employee["name"]] = employee["rank"]
        
        return crew_dict
    
    def get_occupied_staff(self):
        pass

    def get_available_staff(self):
        pass
    
    def get_by_ssn(self,employee_dict: dict, ssn: int):
        """Returns the employee with the ssn that the user put in. If no employee has that ssn, the function returns None"""
        
        for employee in employee_dict:
            if employee["ssn"] == ssn:
                return employee
            else:
                pass
        
        return None

    def check_if_available(self):
        pass

    def get_employee_dict(self, ret_dict):
        """Returns a dictionary with all the employees that work for the company NaN air."""
        return self.employee.get_employee_dict(ret_dict)

        
