from data.voyage_data import Voyage_Data
import datetime
def main():
    voyage_list = Voyage_Data().get_all_voyage()
    name = ("Einar")
    #departure = '08:00 17.12.2023'
    voyage_id = '1111'
    print(check_id(voyage_id, name))
    
    
def check_id(voyage_id, name):
    new_voyage_date = []
    voyage_list = Voyage_Data().get_all_voyage()
    for voyage in voyage_list:
        if voyage_id == voyage.id:
            departure = voyage.dep_time_back
            new_voyage_day, new_voayge_month, new_voyage_year = departure[6:8], departure[9:11], departure[12:]
            new_voyage_date.append(f"{new_voyage_day}.{new_voayge_month}.{new_voyage_year}")
    
    if check_availability(name):
        availability = check_availability(name)
        for item in availability:
            if item in new_voyage_date:
                print("Not available!")
        


def check_availability(name):
    voyage_list = Voyage_Data().get_all_voyage()



    for voyage in voyage_list:       
        if name in voyage.head_of_service or name in voyage.flight_attendant or name in voyage.captain or name in voyage.copilot:
            dep_time_back = (voyage.dep_time_back)
           
            date = dep_time_back[6:]
            day, month, year = date[:2], date[3:5], date[6:]
            day, month, year = int(day), int(month), int(year)
           
            availability = date_time_availability(year, month, day)
            
            
            return(availability)
            
    

def datetime_formatter(datetime):
    available_year, available_month, available_day = datetime[:4], datetime[5:7], datetime[8:]
    available_voyage = f"{available_day}.{available_month}.{available_year}"
    return available_voyage

def date_time_availability(year, month, day):
    voyage_date = datetime.date(year, month, day)
    
    
    voyage_date_next_day = voyage_date + datetime.timedelta(days=1)
    voyage_date_next_day = str(voyage_date_next_day)
    voyage_date = str(voyage_date)

    form_voyage_date = datetime_formatter(voyage_date)
    form_voyage_next_date = datetime_formatter(voyage_date_next_day)
    return [form_voyage_date, form_voyage_next_date]

if __name__ == "__main__":
    main()