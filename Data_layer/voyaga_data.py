import csv

class Voyage_data:
    def __init__(self):
        try: 
            self.file_name = input(f"Enter voyage filename: ") #filenameið sem inniheldur info um þetta class
            self.file = open(self.file_name, "r")             
        except FileNotFoundError:
            print("File not found, try again")

    def print_crew_list_for_voyage(self):
        pass

    def create_voyage(self):
        """User can Create Voyage"""
        pass

    def edit_voyage(self):
        pass

    def read_voyage_information(self):
        flight_dict = dict()
        """User can read information about a voyage"""
        for line in self.file:
            flight_nr, dep_from, arr_at, departure, arrival, plane_insignia = line
            flight_dict[flight_nr] = dep_from, arr_at, departure, arrival, plane_insignia
        
