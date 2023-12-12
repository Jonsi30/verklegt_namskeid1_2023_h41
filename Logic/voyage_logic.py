from data.data_wrapper import Data_wrapper
import datetime
from model.voyage_model import Voyage_Model


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
            flight_nr = flight_nr[2::]
            flight_nr = int(flight_nr)
            flight_nr_back = flight_nr + 1
            flight_nr_back = f"NA{flight_nr_back}"

            result = f"\nVoyage ID: {id}\n\nFlight from Iceland:\nDeparture from: {dep_from}\tDeparting time: {dep_time}\nArriving too: {arr_at}\tArrival time: {arr_time}\n\nFlight to Iceland:\nDeparture from: {arr_at}\nDeparting time: {dep_time_back}\nArriving too: {dep_from}\tArrival time: {arr_time_back}\n\nEMPLOYEES:\nCaptain: {captain}\nCopilot: {copilot}\nHead of Service: {head_of_service}\nFlight Attendant: {flight_attendant}\nPlane insignia: {plane_insignia}\n\n"
            results.append(result)
        
        return results
