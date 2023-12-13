from data.data_wrapper import Data_wrapper
import datetime
from model.voyage_model import Voyage_Model
from prettytable import PrettyTable


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

    def get_specific_day_voyage(self):
        pass

    def get_week_number(self, year_number: int, week_number: int) -> list:
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

    # def get_voyage_by_flight_nr(self): MAAAYBE
    #     pass

    def update_voyage(self, id, rankn):
        pass

    def display_voyage_director(self):
        """EKKI SNERTA"""
        voyage_list = self.voyage.get_voyage_data()
        results = []
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
            flight_attendant = voyage["flight_attendant"]
            flight_nr = voyage["flight_nr"]
            flight_nr = flight_nr[2::]
            flight_nr = int(flight_nr)
            flight_nr_back = flight_nr + 1
            flight_nr_back = f"NA{flight_nr_back}"

            result = f"\nVoyage_id = {id}\n\nFlight from Iceland:\nDeparture from: {dep_from}\tDeparting time: {dep_time}\nArriving too: {arr_at}\tArrival time: {arr_time}\n\n"
            result += f"Flight to Iceland:\nDeparture from: {arr_at}\nDeparting time: {dep_time_back}\nArriving too: {dep_from}\tArrival time: {arr_time_back}\n\n"
            results.append(result)
        return results

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

            result = f"Voyage ID: {id}\n\nFlight from Iceland: {flight_nr}\nDeparture from: {dep_from}\tDeparting time: {dep_time}\nArriving too: {arr_at}\tArrival time: {arr_time}\n\nFlight to Iceland: {flight_nr_back}\nDeparture from: {arr_at}\nDeparting time: {dep_time_back}\nArriving too: {dep_from}\tArrival time: {arr_time_back}\n\nEMPLOYEES:\nCaptain: {captain}\nCopilot: {copilot}\nHead of Service: {head_of_service}\nFlight Attendant: {flight_attendant}\nPlane insignia: {plane_insignia}\n\n{voyage_sep}\n"
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
    
    