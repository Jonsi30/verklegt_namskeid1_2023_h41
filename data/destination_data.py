import csv
from model.destination import Destination
from ui.Destination_UI import destination

FIELDNAMES = [
    "Destination",
    "Distance from Iceland",
    "Flight Time",
    "Emergency Contact",
    "Emergency Contact Phone Number",
]


class Destination_data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/destinations.csv"  # filenameið sem inniheldur info um þetta class

    def get_all_destination(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    Destination(
                        row["Destination"],
                        row["Distance from Iceland"],
                        row["Flight Time"],
                        row["Emergency Contact"],
                        row["Emergency Contact Phone Number"],
                    )
                )
        return ret_list

    def create_destination(self, destination: Destination):
        # User can Create Destination
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = FIELDNAMES
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "Destination": destination.destination,
                    "Distance from Iceland": destination.distance_from_ice,
                    "Flight Time": destination.flight_time,
                    "Emergency Contact": destination.emergency_contact,
                    "Emergency Contact Phone Number": destination.emergency_contact_phone_nr,
                }
            )

    def update_destination(self, updated_dest: Destination):
        # *sækja öll destination
        # loopa yfir destinations
        # ef ég finnd match á id í updated of current dest þá geri ég breytingarnar
        # tæma skránna
        # write flag "w" writeheader()
        # kalla á create destination for each dest í þessum list *
        all_dest = Destination_data()
        every_dest = all_dest.get_all_destination()
        new_list = []
        for dest in every_dest:
            if dest.destination == updated_dest.destination:
                new_list.append(
                    Destination(
                        updated_dest.destination,
                        updated_dest.distance_from_ice,
                        updated_dest.flight_time,
                        updated_dest.emergency_contact,
                        updated_dest.emergency_contact_phone_nr,
                    )
                )
            else:
                new_list.append(
                    (
                        dest.destination,
                        dest.distance_from_ice,
                        dest.flight_time,
                        dest.emergency_contact,
                        dest.emergency_contact_phone_nr,
                    )
                )

        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, "w", newline="") as self.file_name:
            fields = FIELDNAMES
            writer = csv.DictWriter(self.file_name, fieldnames=fields)

            writer.writeheader()

        for dest in new_list:
            Destination_data().create_destination(dest)


"""
    def print_most_popular_destination(self):
        #User can read popular destinations
        pass

    def update_emergency_contact(self):
        #User can update emergency contact info
        pass

    def create_destination(self):
        #User can Create Destination
        pass
"""
