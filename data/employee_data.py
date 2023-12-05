import csv
from model.employee import Employee
self, name="", role="", rank="", license="", phone_nr="", adress="", ssn="")

class Employee_data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/employees.csv" #filenameið sem inniheldur info um þetta class

    def get_all_employees(self):
        
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["name"], row["role"], row["rank"], row["license"], row["phone_nr"], row["adress"], row["ssn"]))
        return ret_list

    def create_employee(self, employee_info):
        #User can Create Destination
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "role", "rank", "license", "phone_nr", "adress", "ssn"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': employee_info[0],'role': employee_info[1], 'rank': employee_info[2], 'license': employee_info[3], 'phone_nr': employee_info[4], 'adress': employee_info[5], 'ssn': employee_info[6]})
        

    """
    def print_most_experienced_pilot(self):
        #User can read pilot with the most flight time
        pass

    def edit_employee(self):
        #User can update information about an employee
        pass

    def create_employee(self):
        #User can create employee
        pass

    def read_employee_schedule(self):
        #User can read schedule for a given employee
        pass

    def read_pilot_license(self):
        #User can read pilot license
        pass

    def display_employee_info(self):
        #User can read information about an employee
        pass

    def read_employee_availability(self):
        pass

    def read_employee_status(self):
        #User can read employee status/availability
        pass
        
"""