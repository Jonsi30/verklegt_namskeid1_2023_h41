from data.voyage_data import Voyage_Data
from model.voyage_model import Voyage_Model
from data.employee_data import Employee_data
from data.employee_data import Employee
#test = Employee_data().get_all_employees()

def main():
    date = '16.12.2023'

    display_available_employees(date)

def display_available_employees(date):
    not_available_employees = []
    

    for voyage in Voyage_Data().get_all_voyage():
        if date == voyage.arr_time_back[6:]:
            if voyage.captain != 'Unassigned':
                not_available_employees.append(voyage.captain)
            if voyage.copilot != 'Unassigned':
                not_available_employees.append(voyage.copilot)
            if voyage.head_of_service != 'Unassigned':
                not_available_employees.append(voyage.head_of_service)
            if voyage.flight_attendant != 'Unassigned':
                not_available_employees.append(voyage.flight_attendant)
    non_available = list(dict.fromkeys(not_available_employees).keys())
    available_employees = get_available_employees(non_available)
    print(non_available)
    print()
    return (available_employees)

def get_available_employees(name_list):
    
    availabe_employees = []
    all_employees = Employee_data().get_all_employees()
    for name in all_employees:
        if name.name not in name_list:
            availabe_employees.append(name.name)
    return availabe_employees



if __name__ == "__main__":
    main()




#voyage = test.create_voyage(new_voyage)



    