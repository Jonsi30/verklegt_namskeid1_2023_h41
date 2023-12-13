from logic.logic_wrapper import LogicEmployees
from prettytable import PrettyTable
from logic.logic_wrapper import LogicAircraft
from logic.logic_wrapper import Logic_wrapper

date = '12:00 16.12.2023'
aircrafts = LogicAircraft().get_all_aircrafts()
voayges = Logic_wrapper().get_all_voyages()

date = date[6:]
print(date)

not_available_planes = []
for voyage in voayges:
    if voyage.dep_time[6:] == date:
        not_available_planes.append(voyage.plane_insignia)
available_planes = []

for aircraft in aircrafts:
    if aircraft.plane_insignia not in not_available_planes:
        available_planes.append(aircraft)



plane_table = PrettyTable()
fieldnames = ["Plane Insignia", "Plane Type ID"]
plane_table.field_names = fieldnames
for aircraft in available_planes:
    plane_table.add_row([aircraft.plane_insignia, aircraft.plane_type_id])

print(plane_table)


