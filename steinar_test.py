from data.data_wrapper import Data_wrapper
from data.destination_data import Destination_data
from model.destination import Destination
from logic.logic_wrapper import Logic_wrapper
from model.employee import Employee
from model.voyage_model import Voyage_Model
from data.voyage_data import Voyage_Data
from data.employee_data import Employee_data
from prettytable import PrettyTable
from datetime import datetime
def main():

    dep_time = '00:00 16.12.2023'

    
    print(dep_time[:2])

   

    
    #destination,distance_from_ice,flight time,emergency contact,emergency_contact_phone_nr
    #Nuuk,666,3:30,Kuupik Kleist,3334141
    """
    #Voyage_Data().create_new_flights()
    test = Logic_wrapper().get_all_employees()
    fieldnames = ["Name", "Role", "Rank", "License", "Phone Number", "Address", "Email Adress", "Social Security Number"]
    table = PrettyTable()
    table.field_names = fieldnames
    for employee in test:
        table.add_row([employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn])
    print((table))
    """
    """
    for item in test:
        name = item["name"]
        role = item["role"]
        rank = item["rank"]
        license = item["license"]
        phone_nr = item["phone_nr"]
        adress = item["address"]
        ssn = item["ssn"]
        info = f"{name} {role} {rank} {license} {phone_nr} {adress} {ssn}"
        print(info)
    """
    
    """
    model_info = Destination('Nuuk', '666', '3:30', 'steinar', '3334141')
    new_info = Logic_wrapper()
    
    new_info.update_destination(model_info)
    """
    #John Johnson,Pilot,Captain,NAFokker50,8203341,Engihjalli 30,0404952139

    """
    model_info = Employee('John Johnson', 'Pilot', 'Copilot', 'NAFokker50', '5812345', 'Engihjalli 30', 'john@email.com', '0404952139')
    new_info = Logic_wrapper()
    new_info.update_employee(model_info)
    
    #updated_dest = Logic_wrapper().update_destination(new_info)
    """

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
    new_voyage = ('1111', 'MA40', 'RVK', 'TOR', '06:00 16.12.2023', '12:00 16.12.2023', '15:00 16.12.2023', '21:00 16.12.2023', 'TF-20', 'Scarlett Johanson', 'John Johnson', 'Jessica Alba', 'Jamie Robert')
    #new_info = GetData().create_voyage(new_voyage)
    #new_info.create_voyage()
    """ 
    """
    updated_voyage = Voyage_Model('1111', 'MA40', 'USA', 'TOR', '06:00 16.12.2023', '12:00 16.12.2023', '15:00 16.12.2023', '21:00 16.12.2023', 'TF-20', 'Einar', 'John ', 'Jón Ágústsson Alba', 'Jamie Robert')
    Voyage_Data().update_voyage(updated_voyage)

    all_employees = employee.get_all_employees()
    for employee in all_employees:
       print(employee)
    
    from data.employee_data import Employee_data

    employees = Employee_data()

    print(employees.get_employee_dict())
    """
    
if __name__ == "__main__":
    main()