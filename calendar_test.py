
import datetime
from data.voyage_data import Voyage_Data


def get_week_number(self, year_number:int, week_number:int) -> str:
    test = Voyage_Data()
    listi = (test.get_all_voyage())
    voage_list = []

    for item in listi:
        date = (item["arr_time_back"][6::])
        year = date[6::]
        if year == year_number:
            month = date[3:5]
            day = date[:2]
            
            year = int(year)
            month = int(month)
            day = int(day)
            real_week = datetime.date(year, month, day).isocalendar()[1]
            if real_week == week_number:
                voage_list.append(item)
        
    return voage_list



#print(datetime.date(voayge))


