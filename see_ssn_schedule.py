from logic.logic_wrapper import Logic_wrapper
from logic.logic_wrapper import VoyageLogic

all_voyages = Logic_wrapper().get_all_voyages()
all_employees = Logic_wrapper().get_all_crew()

ssn = '1212904889'

staff_member = []

for employee in all_employees:
    if employee.ssn == ssn:
        staff_member.append(employee)

name = ""
for info in staff_member:
        name += info.name


    

