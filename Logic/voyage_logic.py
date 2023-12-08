from data.data_wrapper import Data_wrapper


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
        voyage_info = (
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

    def get_specific_week_voyage(self):
        pass

    # def get_voyage_by_flight_nr(self): MAAAYBE
    #     pass

    def update_voyage(self):
        pass

    def get_flight(self):
        """EKKI SNERTA"""
        flight_dict = dict()
        lines = self.voyage.get_voyage_data().readlines()[1:]
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
