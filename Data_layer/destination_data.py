import csv
from model.destination import Destination

class Destination_data:
    def __init__(self):
        self.file_name = "verklegt_namskeid1_2023_h41/files/destinations.csv" #filenameið sem inniheldur info um þetta class


    def create_destination(self):
        #User can Create Destination
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "destination", "numeric_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': destination.id,'destination': destination.name, 'numeric_id': destination.numeric_id})


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