FLIGHT_FILE = "../VERKLEGT_NAMSKEID1_2023_H41/Files/flight_list.csv"
import csv
from model.voyage_model import Voyage_Model


class Voyage_Data:
    def __init__(self) -> None:
        self.file_name = "../verklegt_namskeid1_2023_h41/files/voyage.csv"
        self.flight_list = "../verklegt_namskeid1_2023_h41/files/flight_list.csv"

    def get_voyage_data(self):
        file_name = FLIGHT_FILE
        file = open(file_name, "r", encoding="utf-8")
        return file

    def get_all_voyage(self):
        # Display every voyage
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    Voyage_Model(
                        row["id"],
                        row["flight_nr"],
                        row["dep_from"],
                        row["arr_at"],
                        row["dep_time"],
                        row["arr_time"],
                        row["dep_time_back"],
                        row["arr_time_back"],
                        row["plane_insignia"],
                        row["captain"],
                        row["copilot"],
                        row["head_of_service"],
                        row["flight_attendant"],
                    )
                )

        return ret_list

    def create_voyage(self, voyage):
        # User can Create Voayge
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "Id",
                "Flight Number",
                "Departure From",
                "Arrival at",
                "Departure Time",
                "Arrival Time",
                "Departure Time Back",
                "Arrival Time Back",
                "Plane Insignia",
                "Captain",
                "Copilot",
                "Head of Service",
                "Flight Attendant",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "id": voyage[0],
                    "flight_nr": voyage[1],
                    "dep_from": voyage[2],
                    "arr_at": voyage[3],
                    "dep_time": voyage[4],
                    "arr_time": voyage[5],
                    "dep_time_back": voyage[6],
                    "arr_time_back": voyage[7],
                    "plane_insignia": voyage[8],
                    "captain": voyage[9],
                    "copilot": voyage[10],
                    "head_of_service": voyage[11],
                    "flight_attendant": voyage[12],
                }
            )

    def update_voyage(self, updated_info):
        all_dest = Voyage_Data()
        every_voayge = all_dest.get_all_voyage()
        new_list = []
        for item in every_voayge:
            if item["id"] == updated_info["id"]:
                new_list.append(
                    (
                        item["id"],
                        item["flight_nr"],
                        item["dep_from"],
                        item["arr_at"],
                        item["dep_time"],
                        item["arr_time"],
                        item["dep_time_back"],
                        item["arr_time_back"],
                        item["plane_insignia"],
                        updated_info["captain"],
                        updated_info["copilot"],
                        updated_info["head_of_service"],
                        updated_info["flight_attendant"],
                    )
                )
            else:
                new_list.append(
                    (
                        item["id"],
                        item["flight_nr"],
                        item["dep_from"],
                        item["arr_at"],
                        item["dep_time"],
                        item["arr_time"],
                        item["dep_time_back"],
                        item["arr_time_back"],
                        item["plane_insignia"],
                        item["captain"],
                        item["copilot"],
                        item["head_of_service"],
                        item["flight_attendant"],
                    )
                )

        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, "w", newline="") as self.file_name:
            fields = [
                "id",
                "flight_nr",
                "dep_from",
                "arr_at",
                "dep_time",
                "arr_time",
                "dep_time_back",
                "arr_time_back",
                "plane_insignia",
                "captain",
                "copilot",
                "head_of_service",
                "flight_attendant",
            ]
            writer = csv.DictWriter(self.file_name, fieldnames=fields)

            writer.writeheader()

        for item in new_list:
            Voyage_Data().create_voyage(item)

    def create_new_flights(self):
        all_voyages = Voyage_Data().get_all_voyage()

        with open(self.flight_list, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "flight_nr",
                "dep_from",
                "arr_at",
                "departure",
                "arrival",
                "plane_insignia",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for voyage in all_voyages:
                flight_number = voyage["flight_nr"]
                flight_nr_back = flight_number_back(
                    flight_number
                )  # Gets the flight number for the returning flight

                writer.writerow(
                    {
                        "flight_nr": voyage["flight_nr"],
                        "dep_from": voyage["dep_from"],
                        "arr_at": voyage["arr_at"],
                        "departure": voyage["dep_time"],
                        "arrival": voyage["arr_time"],
                        "plane_insignia": voyage["plane_insignia"],
                    }
                )

                writer.writerow(
                    {
                        "flight_nr": flight_nr_back,
                        "dep_from": voyage["arr_at"],
                        "arr_at": voyage["dep_from"],
                        "departure": voyage["dep_time_back"],
                        "arrival": voyage["arr_time_back"],
                        "plane_insignia": voyage["plane_insignia"],
                    }
                )


def flight_number_back(flight_nr):
    """This function takes in a flight number, returns a returning flight number"""
    flight_nr = flight_nr[2::]
    flight_nr = int(flight_nr)
    flight_nr_back = flight_nr + 1
    flight_nr_back = f"NA{flight_nr_back}"
    return flight_nr_back
