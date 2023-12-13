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
def main():
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
    run = 0
    while run == 0:
        print((table))
        id_number = (input("Input an Id from the list above, that you want to work with: "))
        print()
        for voyage in upcoming_voyage_list:
            if voyage.id == id_number:
                voyage_in_work.append(voyage)
                run += 1
                break
        if run == 0:    
            print("That id is not in the list above! Try again") 
            print() 
       

    for voyage in voyage_in_work:
        fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
        table = PrettyTable()
        table.field_names = fieldnames
        date = ""
        for voayge in voyage_in_work:
            
            table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])
            date += voayge.arr_time_back[6:]
        print(f"You will work with the voyage with the id: {id_number}")
        
        print((table))
        print()
        

    captain_list = []
    copilot_list = []
    head_of_service_list = []
    flight_attendant_list = []

    available = Logic_wrapper().get_available_staff(date)
    for i in available:
        name, role, rank = i
        if rank == 'Captain':
            captain_list.append([name, role, rank])
        elif rank == 'Copilot':
            copilot_list.append([name, role, rank])
        elif rank == 'Flight Service Manager':
            head_of_service_list.append([name, role, rank])
        elif rank == 'Flight Attendant':
            flight_attendant_list.append([name, role, rank])


    captain_table = table_making(captain_list)
    copilot_table = table_making(copilot_list)
    head_of_service_table = table_making(head_of_service_list)
    flight_attendant_table = table_making(flight_attendant_list)

    captain = select_position(captain_list, captain_table, 'Captain', 'Captains')
    copilot = select_position(copilot_list, copilot_table, 'Copilot', 'Copilots'  )
    head_of_service = select_position(head_of_service_list, head_of_service_table, 'Flight Service Manager', 'Flight Service Managers' )
    flight_attendant = select_position(flight_attendant_list, flight_attendant_table, 'Flight Attendant', 'Flight Attendants')
    print(captain)
    print(copilot)
    print(head_of_service)
    print(flight_attendant)

   
def select_position(employee_list: list, table, role, rank) -> str:
    employee = ""
    run = 0
    while run == 0:
        print(f"These are the {rank} available for this voyage:")
        print((table))
        employee_name = (input(f"Please type in the name of {role} for the voyage: "))
        print()
        for pilots in employee_list:
            name, role, rank = pilots
            if name.lower() == employee_name.lower():
                employee += employee_name
                run += 1
                break
        if run == 0:    
            print("That name is not in the list above! Try again") 
            print() 
    return employee

def table_making(list: list):
    pilot_fieldnames = ["Name", "Role", "Rank"]
    table = PrettyTable()
    table.field_names = pilot_fieldnames
    for employee in list:
        name, role, rank = employee
        table.add_row([name, role, rank])

    return table

if __name__ == "__main__":
    main()


