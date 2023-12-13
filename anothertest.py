from logic.logic_employees import LogicEmployees
from prettytable import PrettyTable
from logic.logic_wrapper import LogicEmployees
from logic.logic_wrapper import LogicDestination
from logic.logic_wrapper import Logic_wrapper
"""
test = LogicEmployees().get_all_crew()
for i in test:
    print(i)
"""
"""
fieldnames = ["Name", "Role", "Rank", "License", "Phone Number", "Address", "Email Adress", "Social Security Number"]
table = PrettyTable()
table.field_names = fieldnames
for employee in test:
    table.add_row([employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn])
print((table))
"""

"""
test = LogicEmployees().get_employee_info('John Stones')
fieldnames = ["Name", "Role", "Rank", "License", "Phone Number", "Address", "Email Address", "Social Security Number"]
table = PrettyTable()
table.field_names = fieldnames
for employee in test:
    table.add_row([employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn])
print((table))
"""
"""
test = LogicEmployees().get_by_ssn('1910702559')
for i in test:
    print(i)
"""
"""
pilots = LogicEmployees().get_all_pilots()
            
fieldnames = ["Name", "Role"]
table = PrettyTable()
table.field_names = fieldnames
for employee in pilots:
    name, role = employee
    table.add_row([name, role])
print((table))
"""

"""
from logic.logic_employees import LogicEmployees
available = LogicEmployees().display_available_employees('16.12.2023')
for i in available:
    print(i)
"""
from data.voyage_data import Voyage_Data
upcoming_voyages = Voyage_Data().get_all_voyage()




upcoming_voyage_list = []
for voyage in upcoming_voyages:
    
    if voyage.captain and voyage.copilot and voyage.head_of_service and voyage.flight_attendant == 'Unassigned':
        upcoming_voyage_list.append(voyage)


fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
table = PrettyTable()
table.field_names = fieldnames
for voyage in upcoming_voyage_list:
    
    table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])

voyage_in_work = []
run = True
while run == True:
    print((table))
    id_number = (input("Input an Id from the list above, that you want to work with: "))
    for voyage in upcoming_voyage_list:
        if voyage.id == id_number:
            voyage_in_work.append(voyage)
            run == False
            pass
        elif id_number not in voyage.id:
            print("You inputted a number id that isn't in the list")   
        
            
    




for voyage in voyage_in_work:
    fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
    table = PrettyTable()
    table.field_names = fieldnames
    for voayge in voyage_in_work:
        
        table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])
    
    print(f"You will work with the voyage with the id: {id_number}")
    print((table))


