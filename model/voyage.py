from Data_layer.voyaga_data import GetData


class Voyage:
    def __init__(self) -> None:
        self.file = GetData.get_voyage_data()

    def get_flight(self):
        flight_dict = dict()
        for line in self.file:
            (
                flight_nr,
                dep_from,
                arr_at,
                departure,
                arrival,
                plane_insignia,
            ) = line.split(",")
            dep_time, dep_date = departure.split("")
            arr_time, arr_date = arrival.split("")
            flight_dict[flight_nr] = (
                dep_from,
                arr_at,
                dep_time,
                dep_date,
                arr_time,
                arr_date,
                plane_insignia,
            )
        return flight_dict

    def get_voyage(self):
        voyage_dict = dict()
        for i in range(0, len(self.file), 2):
            flight1 = self.file[i].split(",")
            flight2 = self.file[i + 1].split(",")
            voyage_dict[i // 2] = {"flight1": flight1, "flight2": flight2}
        return voyage_dict


print(Voyage().get_voyage())
