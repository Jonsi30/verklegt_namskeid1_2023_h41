import csv
from model.destination import Destination

class Destination_data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/destinations.csv" #filenameið sem inniheldur info um þetta class

    def get_all_destination(self):
        
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Destination(row["destination"], row["distance_from_ice"], row["flight time"], row["emergency contact"], row["emergency_contact_phone_nr"]))
        return ret_list

    def create_destination(self, destination_instance):
        #User can Create Destination
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["destination", "distance_from_ice", "flight time", "emergency contact", "emergency_contact_phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'destination': destination_instance[0],'distance_from_ice': destination_instance[1], 'flight_time': destination_instance[2], 'emergency contact': destination_instance[3], 'emergency_contact_phone_nr': destination_instance[4] })


    
"""
    def print_most_popular_destination(self):
        #User can read popular destinations
        pass

    def change_security_info(self):
        #User can update emergency contact info
        pass

    def create_destination(self):
        #User can Create Destination
        pass
"""