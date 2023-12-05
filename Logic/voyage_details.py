from data.data_wrapper import Data_wrapper


class Voyage_details:
    def __init__(self) -> None:
        self.file = Data_wrapper.get_voyage_data(self)

    def get_flight(self):
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

    def get_voyage(self):
        flight_dict = self.get_flight()
        voyage_dict = dict()
        flight_keys = list(flight_dict.keys())
        for i in range(0, len(flight_keys), 2):
            flight1 = flight_dict[flight_keys[i]]
            flight2 = flight_dict[flight_keys[i + 1]]
            voyage_dict[i // 2] = {"flight1": flight1, "flight2": flight2}
        return voyage_dict
