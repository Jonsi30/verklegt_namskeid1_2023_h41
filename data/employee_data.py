import csv
from model.employee import Employee
FIELDNAMES = ["Name", "Role", "Rank", "License", "Phone Number", "Address", "Email Address", "Social Security Number"]

class Employee_data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/employees.csv" #filenameið sem inniheldur info um þetta class

    def get_all_employees(self):
        
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["Name"], row["Role"], row["Rank"], row["License"], row["Phone Number"], row["Address"], row["Email Address"], row["Social Security Number"]))
        return ret_list

    def create_employee(self, employee: Employee):
        #User can Create Employee
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = FIELDNAMES
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'Name': employee.name,'Role': employee.role, 'Rank': employee.rank, 'License': employee.license, 'Phone Number': employee.phone_nr, 'Address': employee.address, 'Email Address': employee.email, 'Social Security Number': employee.ssn})
            
    def get_employee_dict(self):
        ret_dict = {}
        
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            for row in csvfile:
                name, role, rank, license, phone_number, address, ssn = row.split(",")
                if name not in ret_dict.keys():
                    
                    ret_dict[name] = [role, rank, license, phone_number, address, ssn.strip()]

        return ret_dict 
    
    
    def update_employee(self, updated_employee: Employee):
        all_dest = Employee_data()
        every_employee = all_dest.get_all_employees()
        new_list = []
        for employee in every_employee:
            if employee.ssn == updated_employee.ssn:
                new_list.append(Employee(employee.name, updated_employee.role, updated_employee.rank, updated_employee.license, updated_employee.phone_nr, updated_employee.address, updated_employee.email, employee.ssn))
            else:
                new_list.append(Employee(employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn))
       
        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, 'w', newline='') as self.file_name:
            fields = FIELDNAMES
            writer = csv.DictWriter(self.file_name, fieldnames=fields)
            
            writer.writeheader()

        for item in new_list:
            Employee_data().create_employee(item)






    """
    def print_most_experienced_pilot(self):
        #User can read pilot with the most flight time
        pass

    def edit_employee(self):
        #User can update information about an employee
        pass

    
    def read_employee_schedule(self):
        #User can read schedule for a given employee
        pass

    def read_pilot_license(self):
        #User can read pilot license
        pass

    def display_employee(self):
        #User can read information about an employee
        pass

    def read_employee_availability(self):
        pass

    def read_employee_status(self):
        #User can read employee status/availability
        pass
        
"""