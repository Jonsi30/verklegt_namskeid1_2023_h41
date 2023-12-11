from logic.logic_aircraft import LogicAircraft
from prettytable import PrettyTable
from logic.logic_employees import LogicEmployees
#self,plane_insignia,plane_type_id,manufacturer,seat_capacity
#TF-SMJ,NAFokker50,Fokker,8

plane_insignia = "TF-SAM"
plane_type_id = "NAAirbus69"
manufacturer = "Airbus"
seat_capacity = "10"

#plane = LogicAircraft().create_new_aircraft(plane_insignia, plane_type_id, manufacturer, seat_capacity)
"""
test = LogicAircraft().get_all_aircrafts()
fieldnames = ["plane_insignia", "plane_type_id", "manufacturer", "seat_capacity"]
table = PrettyTable()
table.field_names = fieldnames
for aircraft in test:
    table.add_row([aircraft.plane_insignia, aircraft.plane_type_id, aircraft.manufacturer, aircraft.seat_capacity])
print(table)
"""

#Name,Role,Rank,License,Phone Number,Address,Email,Social Security Number
name = 'Steinar'
role = 'Pilot'
rank = 'Captain'
license = 'NAFokker 40'
phone_nr = '5649823'
address= 'Dúfnahólar 10'
email = 'steinar98@gmail.com'
ssn = '3007983229'

test = LogicEmployees().create_employee(name, role, rank, license, phone_nr, address, email, ssn)
