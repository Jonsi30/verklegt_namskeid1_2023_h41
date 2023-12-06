import os
from data.data_wrapper import Data_wrapper


class VoyageLogic:
    def __init__(self):
        self.data_wrapper = Data_wrapper()
        self.file = self.data_wrapper.get_voyage_data()

    def get_all_voyages(self):
        os.system("cls" if os.name == "nt" else "clear")
        flight_dict = dict()
        lines = self.file.readlines()[1:]
        for line in lines:
            values = line.split(",")
            if len(values) != 6:
                continue
            (
                flight_nr,
                dep_from,
                arr_at,
                departure,
                arrival,
                plane_insignia,
            ) = values
            dep_time, dep_date = departure.split(" ")
            arr_time, arr_date = arrival.split(" ")
            flight_dict[flight_nr] = {
                "Departure From": dep_from,
                "Arrival At": arr_at,
                "Departure Time": dep_time,
                "Departure Date": dep_date,
                "Arrival Time": arr_time,
                "Arrival Date": arr_date,
                "Plane Insignia": plane_insignia,
            }
        return flight_dict
