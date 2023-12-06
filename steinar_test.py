from data.data_wrapper import Data_wrapper

def main():
    
    """
    name = Data_wrapper()
    
    id = str(input("Enter new id: "))
    id = id.upper()
    destination = input("Enter new destination: ")
    numeric_id = input("Enter numeric id: ")

    new_destination = (id, destination, numeric_id)
    name.create_destination(new_destination)
    all_destinations = name.get_all_destinations()
    
    for destination in all_destinations:
        
        print(destination)
    
     """
    
    employee = Data_wrapper()
    """
    name = input("Enter employee name: ")
    role = input("Enter employee role: ")
    rank = input("Enter employee rank: ")
    license = input("Enter employee license: ")
    phone = input("Enter employee's phone number: ")
    adress = input("Enter employee adress: ")
    ssn = input("Enter employee ssn: ")
    
    new_info = name, role, rank, license, phone, adress, ssn

    employee.create_employee(new_info)
   """
   
    all_employees = employee.get_all_employees()
    for employee in all_employees:
       print(employee)
    
    from data.employee_data import Employee_data

    employees = Employee_data()

    print(employees.get_employee_dict())
    
    
if __name__ == "__main__":
    main()