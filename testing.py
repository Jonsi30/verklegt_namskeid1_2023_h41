from datetime import datetime
from datetime import timedelta


def time_formatter(departure_time, flight_time):
    time = departure_time[:6]
    
    day = int(departure_time[6:8])
    month =  int(departure_time[9:11])
    year = int(departure_time[12:])

    hours_one = int(flight_time[:2])
    hours_two = int(time[:2])
    minutes_one = int(flight_time[3:])
    minutes_two = int(time[3:])

    all_hours = (hours_one + hours_two)
    all_minutes = minutes_one + minutes_two

    return day, month, year, all_hours, all_minutes
    
def adding_time(day, month, year, all_hours, all_minutes):
    day_added = 0
    
    if all_minutes > 60:
        divmodminutes = divmod(all_minutes, 60)
        all_minutes = divmodminutes[1]
        allhours += 1

    if allhours > 24:
        divmodhours = divmod(all_hours, 24)
        allhours = divmodhours[1]
        day_added += 1
        

    if all_minutes < 10:
        all_minutes = f"0{all_minutes}"

    if allhours < 10:
        allhours = f"0{all_hours}"

    new_time = f"{all_hours}:{all_minutes}"



    new_date = datetime(year, month, day) + timedelta(days=day_added)
    new_date = str(new_date)
    day = new_date[8:10]
    month = new_date[5:7]
    year = new_date[:4]


    arrival_time = f"{new_time} {day}.{month}.{year}"
    return(arrival_time)


def main():
    dep_time = '02:35 16.12.2023'
    flight_time = '23:30'
    time = dep_time[:6]
    
    day = int(dep_time[6:8])
    month =  int(dep_time[9:11])
    year = int(dep_time[12:])

    hours_one = int(flight_time[:2])
    hours_two = int(time[:2])
    minutes_one = int(flight_time[3:])
    minutes_two = int(time[3:])

    allhours = (hours_one + hours_two)
    all_minutes = minutes_one + minutes_two
    
    day_added = 0
    if all_minutes > 60:
        divmodminutes = divmod(all_minutes, 60)
        all_minutes = divmodminutes[1]
        allhours += 1

    if allhours > 24:
        divmodhours = divmod(allhours, 24)
        allhours = divmodhours[1]
        day_added += 1
        

    if all_minutes < 10:
        all_minutes = f"0{all_minutes}"

    if allhours < 10:
        allhours = f"0{allhours}"

    new_time = f"{allhours}:{all_minutes}"



    new_date = datetime(year, month, day) + timedelta(days=day_added)
    new_date = str(new_date)
    day = new_date[8:10]
    month = new_date[5:7]
    year = new_date[:4]


    arrival_time = f"{new_time} {day}.{month}.{year}"
    print(arrival_time)

if __name__ == "__main__":
    main()