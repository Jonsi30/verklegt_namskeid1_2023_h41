from logic.voyage_logic import VoyageLogic

listi = self.voyage.get_all_voyages()
voyage_list = []

for item in listi:
    date = item["arr_time_back"][6::]
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
            voyage_list.append(item)

return voyage_list