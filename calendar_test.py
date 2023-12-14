
import datetime
from data.voyage_data import Voyage_Data
from logic.logic_wrapper import Logic_wrapper


test = Voyage_Data()
listi = (test.get_all_voyage())

voage_list = []
week_number = 51
year_number = 2023
ssn = '0101802329'

employee = Logic_wrapper().get_by_ssn(ssn)
name = employee[0]
name = name.name


voyages = []
for voyage in listi:
    date = (voyage.arr_time_back[6::])
    year = date[6::]
    year = int(year)
    if year == year_number:
        month = date[3:5]
        day = date[:2]
        
        year = int(year)
        month = int(month)
        day = int(day)
        real_week = datetime.date(year, month, day).isocalendar()[1]
        if real_week == week_number:
            if voyage.captain == name or voyage.copilot == name or voyage.head_of_service == name or voyage.flight_attendant == name:
                voyages.append(voyage) 
        
if voyages:
    for i in voyages:
        print(i)
else: print("No voayges")
            


    
"""
from logic.logic_wrapper import Logic_wrapper
name = "Einar"

dt = Logic_wrapper()
voyage = dt.get_voyagelists_from_week(2023, 50)#Year, week_number
for item in voyage:
    if name in item["captain"]:
        print(item)
    


#print(datetime.date(voayge))

"""
