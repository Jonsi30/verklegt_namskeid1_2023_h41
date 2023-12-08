
import datetime
from data.voyage_data import Voyage_Data



test = Voyage_Data()
listi = (test.get_all_voyage())
voage_list = []
week_number = 50
year_number = 2023

"""
for item in listi:
    date = (item["arr_time_back"][6::])
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
            print(item)


"""

from logic.logic_wrapper import Logic_wrapper

dt = Logic_wrapper()
voyage = dt.get_voyagelists_from_week(2023, 50)#Year, week_number
for item in voyage:
    print(item)
    print()


#print(datetime.date(voayge))


