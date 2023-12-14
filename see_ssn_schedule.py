from logic.logic_wrapper import Logic_wrapper
from logic.logic_wrapper import VoyageLogic
from prettytable import PrettyTable
all_voyages = Logic_wrapper().get_all_voyages()





def main():

    ssn = '1212904889'
    
    #while validate == True:
        #validate = valid_ssn(ssn)
    
    print(get_schedule_by_ssn(ssn))

def valid_ssn(ssn) -> bool:
    all_employees = Logic_wrapper().get_all_crew()
    ssn_list = []
    for info in all_employees:
        ssn_list.append(info.ssn)
    
    if ssn in ssn_list:
        return True
    
    return False


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

    work_scheadule = PrettyTable()
    work_scheadule.field_names = fieldnames
    for work in voyages:

        work_scheadule.add_row([work.id, name, role, work.dep_time, work.arr_time_back, work.arr_at])

    return (work_scheadule)


if __name__ == "__main__":
    main()