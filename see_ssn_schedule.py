from logic.logic_wrapper import Logic_wrapper
from logic.logic_wrapper import VoyageLogic
from prettytable import PrettyTable
all_voyages = Logic_wrapper().get_all_voyages()





def main():

    ssn = valid_ssn()
    
    print(get_schedule_by_ssn(ssn))

def valid_ssn():
    
    all_employees = Logic_wrapper().get_all_crew()
    
    ssn_table = PrettyTable()
    fieldnames = ["Name", "SSN"]
    ssn_table.field_names = fieldnames
    
    ssn_list = []
    
    for info in all_employees:
        ssn_list.append(info.ssn)
        ssn_table.add_row([info.name, info.ssn])

    
    print(ssn_table)
    ssn_input = input("Enter a ssn from the list above: ")

    if ssn_input not in ssn_list:
        while ssn_input not in ssn_list:
            print(ssn_table)
            print("That id is not in the list above, try again")
            ssn_input = input("Enter a ssn from the list above: ")
    
    
    return ssn_input


def get_schedule_by_ssn(ssn):
    all_employees = Logic_wrapper().get_all_crew()
    name = ""
    role = ""
    for employee in all_employees:
        if employee.ssn == ssn:
            name += employee.name
            role += employee.role
        

    voyages = []

    for voyage in all_voyages:
        if name in voyage.captain or name in voyage.copilot or name in voyage.head_of_service or name in voyage.flight_attendant:
            voyages.append(voyage)

    fieldnames = ["Voyage Id", "Employee", "Role", "Departure Time", "Arrival Time Back", "Destination"]

    if voyages:
        work_scheadule = PrettyTable()
        work_scheadule.field_names = fieldnames
        for work in voyages:

            work_scheadule.add_row([work.id, name, role, work.dep_time, work.arr_time_back, work.arr_at])

        return (work_scheadule)
    
    return f"{name} doesn't have any upcoming voayges!"


if __name__ == "__main__":
    main()