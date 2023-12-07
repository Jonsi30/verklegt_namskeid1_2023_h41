from data.data_wrapper import Data_wrapper
from data.destination_data import Destination_data
from model.destination import Destination
from logic.logic_wrapper import Logic_wrapper
from model.employee import Employee
def main():
    #destination,distance_from_ice,flight time,emergency contact,emergency_contact_phone_nr
    #Nuuk,666,3:30,Kuupik Kleist,3334141
    
    
    
    """
    model_info = Destination('Nuuk', '666', '3:30', 'steinar', '3334141')
    new_info = Logic_wrapper()
    
    new_info.update_destination(model_info)
    """
    #John Johnson,Pilot,Captain,NAFokker50,8203341,Engihjalli 30,0404952139

    """
    model_info = Employee('John Johnson', 'Pilot', 'Copilot', 'NAFokker50', '5812345', 'Engihjalli 30', '0404952139')
    new_info = Logic_wrapper()
    new_info.update_employee(model_info)
    """
    #updated_dest = Destination_data().update_destination(new_info)
    

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
     
    
    #employee = Data_wrapper()
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
"""
    all_employees = employee.get_all_employees()
    for employee in all_employees:
       print(employee)
    
    from data.employee_data import Employee_data

    employees = Employee_data()

    print(employees.get_employee_dict())
    """
    
if __name__ == "__main__":
    main()