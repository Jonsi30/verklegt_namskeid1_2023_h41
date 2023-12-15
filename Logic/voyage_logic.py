
from data.data_wrapper import Data_wrapper
from model.voyage_model import Voyage_Model
from prettytable import PrettyTable

import datetime

from logic.logic_employees import LogicEmployees
from logic.logic_destination import LogicDestination


class VoyageLogic:
    def __init__(self):
        self.voyage = Data_wrapper()

    def create_voyage(
        self,
        id,
        flight_nr,
        dep_from,
        arr_at,
        dep_time,
        arr_time,
        dep_time_back,
        arr_time_back,
        plane_insignia,
        captain="",
        copilot="",
        head_of_service="",
        flight_attendant="",
    ):
        voyage_info = Voyage_Model(
            id,
            flight_nr,
            dep_from,
            arr_at,
            dep_time,
            arr_time,
            dep_time_back,
            arr_time_back,
            plane_insignia,
            captain,
            copilot,
            head_of_service,
            flight_attendant,
        )

        return self.voyage.create_voyage(voyage_info)

    def get_employee_week_schedule(self, year_number: int, week_number: int, ssn: str) -> list:
        all_voayges = self.voyage.get_all_voyages()
        employee = LogicEmployees().get_by_ssn(ssn)
        name = employee[0]
        name = name.name
        
        
        voyage_list = []

        for voyage in all_voayges:
            date = voyage.arr_time_back[6::]
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
                        voyage_list.append(voyage)
        
        return voyage_list

    def display_voyage_manager(self):
        """EKKI SNERTA"""
        voyage_list = self.voyage.get_voyage_data()
        results = []
        voyage_sep = ("-" * 56)
        for voyage in voyage_list:
            id = voyage["id"]
            dep_from = voyage["dep_from"]
            arr_at = voyage["arr_at"]
            dep_time = voyage["dep_time"]
            arr_time = voyage["arr_time"]
            dep_time_back = voyage["dep_time_back"]
            arr_time_back = voyage["arr_time_back"]
            plane_insignia = voyage["plane_insignia"]
            captain = voyage["captain"]
            copilot = voyage["copilot"]
            head_of_service = voyage["head_of_service"]
            flight_attendant = voyage["flight_attendant"]
            flight_nr = voyage["flight_nr"]
            flight_nr_new = flight_nr[2::]
            flight_nr_new = int(flight_nr_new)
            flight_nr_back = flight_nr_new + 1
            flight_nr_back = f"NA0{flight_nr_back}"

            result = f"Voyage ID: {id}\n\nFlight from Iceland: {flight_nr}\nDeparture from: {dep_from}\tDeparting time: {dep_time}\nArriving too: {arr_at}\tArrival time: {arr_time}\n\nFlight to Iceland: {flight_nr_back}\nDeparture from: {arr_at}\tDeparting time: {dep_time_back}\nArriving too: {dep_from}\tArrival time: {arr_time_back}\n\nEMPLOYEES:\nCaptain: {captain}\nCopilot: {copilot}\nHead of Service: {head_of_service}\nFlight Attendant: {flight_attendant}\nPlane insignia: {plane_insignia}\n\n{voyage_sep}\n"
            results.append(result)
        
        return results

    def select_position(self, employee_list: list, table, role, rank) -> str:
        employee = ""
        run = 0
        while run == 0:
            print(f"These are the {rank} available for this voyage:")
            print((table))
            employee_name = (input(f"Please type in the name of {role} for the voyage: "))
            print()
            for pilots in employee_list:
                name, role, rank = pilots
                if name.lower() == employee_name.lower():
                    employee += employee_name
                    run += 1
                    break
            if run == 0:    
                print("That name is not in the list above! Try again") 
                print() 
        return employee

    def table_making(self,list: list):
        pilot_fieldnames = ["Name", "Role", "Rank"]
        table = PrettyTable()
        table.field_names = pilot_fieldnames
        for employee in list:
            name, role, rank = employee
            table.add_row([name, role, rank])

        return table
    
    def time_formatter(self, departure_time, flight_time):
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
    
    def arrival_time_and_date(self, day, month, year, all_hours, all_minutes):
        day_added = 0
        
        if all_minutes >= 60:
            divmodminutes = divmod(all_minutes, 60)
            all_minutes = divmodminutes[1]
            all_hours += 1

        if all_hours > 24:
            divmodhours = divmod(all_hours, 24)
            all_hours = divmodhours[1]
            day_added += 1
            

        if all_minutes < 10:
            all_minutes = f"0{all_minutes}"

        if all_hours < 10:
            all_hours = f"0{all_hours}"

        new_time = f"{all_hours}:{all_minutes}"



        new_date = datetime.datetime(year, month, day) + datetime.timedelta(days=day_added)
        new_date = str(new_date)
        day = new_date[8:10]
        month = new_date[5:7]
        year = new_date[:4]


        arrival_time = f"{new_time} {day}.{month}.{year}"
        return(arrival_time)
    
    def all_voyage_ids(self) -> list:
        all_voyage_ids = []
        all_voayges = self.voyage.get_all_voyages()
        for voyage in all_voayges:
            all_voyage_ids.append(voyage.id)
        return all_voyage_ids
    
    def validate_voyage_id_input(self, id_input) -> bool:
        all_voyage_ids = self.all_voyage_ids()

        if len(id_input) == 4 and id_input not in all_voyage_ids:
            for digit in id_input:
                if digit.isalpha():
                    return False
            return True
        return False
    
    def validate_voyage_dest_input(self, dest_input) -> bool:
        all_dest_id = LogicDestination().get_all_dest_ids()

        if dest_input not in all_dest_id:
            return False
        return True
        
    def validate_departure_time(self, dep_time) -> bool:
        
        if len(dep_time) == 16:
            time = (dep_time[:5])
            date = dep_time[6:]
            validate_date = LogicEmployees().validate_date_input_format(date)
            validate_time = LogicDestination().validate_dest_duration_input(time)
            if validate_date == True  and validate_time == True:
                return True
            
        return False
    
    def validate_dep_time_back(self, arr_time, dep_time_back_input) -> bool:
        #arr_time 04:30 23.12.2023
        from datetime import datetime, timedelta
        dep_time_back = VoyageLogic().validate_departure_time(dep_time_back_input)
        
        if dep_time_back == True:
            date = "%H:%M %d.%m.%Y"
            
            dep_datetime = datetime.strptime(dep_time_back_input, date)
            arr_datetime = datetime.strptime(arr_time, date)

            time_between = dep_datetime - arr_datetime
            one_hour = timedelta(hours=1)
            

            
            return time_between >= one_hour
                
        
        return False
            
            #dep_time = (dep_time_back_input[:5])
           # dep_date = dep_time_back_input[6:]

           # arr_time = (arr_time[:5])
            #arr_date = arr_time[6:]

    def get_available_plane_insignia(self, available_planes: list) -> list:
        insigna_list = []
        for aircraft in available_planes:
            insigna_list.append(aircraft.plane_insignia)

        return insigna_list
    
    def get_unstaffed_voyages(self, upcoming_voyages: list) -> list:
        unstaffed_voyages = []
        for voyage in upcoming_voyages:
            
            if voyage.captain and voyage.copilot and voyage.head_of_service and voyage.flight_attendant == 'Unassigned':
                unstaffed_voyages.append(voyage)
        return unstaffed_voyages
        
    def validate_voyage_user_input_id(self, user_id_input, unstaffed_voyages: list) -> bool:
        
        for info in unstaffed_voyages:
            if info.id == user_id_input:
                return True
        return False
    
    def get_voyage_from_id_input(self, id_number):
        all_voyages = Data_wrapper().get_all_voyages()
        for voyage in all_voyages:
            if voyage.id == id_number:
                return voyage
            
    def get_available_captain_info(self, available_staff):
        available_captains = []
        for i in available_staff:
            name, role, rank = i
            if rank == 'Captain':
                available_captains.append([name, role, rank])

        return available_captains
    
    def get_available_copilot_info(self, available_staff):
        available_copilots = []

        for i in available_staff:
            name, role, rank = i
            if rank == 'Copilot':
                available_copilots.append([name, role, rank])
        return available_copilots
    
    def get_available_head_of_service_info(self, available_staff):
        available_head_of_services = []
        for i in available_staff:
            name, role, rank = i
            
            if rank == 'Flight Service Manager':
                available_head_of_services.append([name, role, rank])
        return available_head_of_services
    
    def get_available_flight_attendant_info(self, available_staff):
        available_flight_attendants = []

        for i in available_staff:
            name, role, rank = i
            
            if rank == 'Flight Attendant':
                available_flight_attendants.append([name, role, rank])
        return available_flight_attendants





        
            
            

    