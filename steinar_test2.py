from data.voyage_data import Voyage_Data
from model.voyage_model import Voyage_Model
from data.employee_data import Employee_data
from data.employee_data import Employee
test = Employee_data().get_all_employees()

for employee in test:
    if employee.role == "Pilot":
        print(employee.name)




#voyage = test.create_voyage(new_voyage)



    