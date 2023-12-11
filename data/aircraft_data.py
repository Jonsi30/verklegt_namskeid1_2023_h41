import csv
from model.aircraft_model import Aircraft_Model


class Aircraft_Data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/aircraft_types.csv"  # filenameið sem inniheldur info um þetta class

    def get_all_aircrafts(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    Aircraft_Model(
                        row["plane_insignia"],
                        row["plane_type_id"],
                        row["manufacturer"],
                        row["seat_capacity"],
                    )
                )
        return ret_list

    def create_aircraft(self, aircraft):
        # User can Create Aircraft
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "plane_insignia",
                "plane_type_id",
                "manufacturer",
                "seat_capacity",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "plane_insignia": aircraft.plane_insignia,
                    "plane_type_id": aircraft.plane_type_id,
                    "manufacturer": aircraft.manufacturer,
                    "seat_capacity": aircraft.seat_capacity,
                }
            )

    """
    

    def display_plane_status(self):
        #User can read plane status with a given time and date.
        pass

    def display_pilots_with_aircraft_license(self):
        #User can read no. pilots with license on a given plane
        pass
    """
