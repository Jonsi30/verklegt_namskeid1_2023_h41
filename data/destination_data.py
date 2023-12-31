import csv
from model.destination import Destination


FIELDNAMES = [
    "Destination",
    "Destination ID",
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
                        row["Destination ID"],
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
                    "Destination ID": destination.destination_id,
                    "Distance from Iceland": destination.distance_from_ice,
                    "Flight Time": destination.flight_time,
                    "Emergency Contact": destination.emergency_contact,
                    "Emergency Contact Phone Number": destination.emergency_contact_phone_nr,
                }
            )

    def update_destination(self, updated_dest: Destination):
        
        all_dest = Destination_data()
        every_dest = all_dest.get_all_destination()
        new_list = []
        for dest in every_dest:
            if dest.destination_id == updated_dest.destination_id:
                new_list.append(
                    ([
                        dest.destination,
                        updated_dest.destination_id,
                        updated_dest.distance_from_ice,
                        updated_dest.flight_time,
                        updated_dest.emergency_contact,
                        updated_dest.emergency_contact_phone_nr,
                    ])
                )
            else:
                new_list.append(
                    ([
                        dest.destination,
                        dest.destination_id,
                        dest.distance_from_ice,
                        dest.flight_time,
                        dest.emergency_contact,
                        dest.emergency_contact_phone_nr,
                    ])
                )

        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, "w", newline="") as self.file_name:
            fields = FIELDNAMES
            writer = csv.DictWriter(self.file_name, fieldnames=fields)

            writer.writeheader()

        for i, dest in enumerate(new_list):
            destination, destination_id, distance_from_ice, flight_time, emergency_contact, emergency_contact_phone_nr = dest
            
            if destination == '':
                destination = every_dest[i].destination
            if destination_id == '':
                destination_id = every_dest[i].destination_id
            if distance_from_ice == '':
                distance_from_ice = every_dest[i].distance_from_ice
            if flight_time == '':
                flight_time = every_dest[i].flight_time
            if emergency_contact == '':
                emergency_contact = every_dest[i].emergency_contact
            if emergency_contact_phone_nr == '':
                emergency_contact_phone_nr = every_dest[i].emergency_contact_phone_nr
            
            Destination_data().create_destination(Destination(destination, destination_id, distance_from_ice, flight_time, emergency_contact, emergency_contact_phone_nr))



