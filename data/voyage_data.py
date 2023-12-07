FLIGHT_FILE = "../VERKLEGT_NAMSKEID1_2023_H41/Files/flight_list.csv"
import csv 
from model.voyage_model import Voyage_Model

class GetData:
    def __init__(self) -> None:
        self.file_name = "../verklegt_namskeid1_2023_h41/files/voyage.csv"

    def get_voyage_data(self):
        file_name = FLIGHT_FILE
        file = open(file_name, "r", encoding="utf-8")
        return file
    
    def get_all_voyage(self):
        #Display every voyage
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage_Model(row["id"], row["flight_nr"], row["dep_from"], row["arr_at"], row["departure"], row["arrival"], row["plane_insignia"], row["captain"], row["copilot"], row["head_of_service"], row["flight_attendant"]))
        
        return ret_list

    def create_voayge(self, voyage):
        #User can Create Destination
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "flight_nr", "dep_from", "arr_at", "departure", "arrival", "plane_insignia", "captain", "copilot", "head_of_service", "flight_attendant"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': voyage[0],'flight_nr': voyage[1], 'dep_from': voyage[2],
            'arr_at': voyage[3], 'departure': voyage[4], 'arrival': voyage[5], 'plane_insignia': voyage[6],
            'captain': voyage[7], 'copilot': voyage[8], 'head_of_service': voyage[9], 'flight_attendant': voyage[10] })

    def update_voyage(self, updated_info):
        all_dest = GetData()
        every_voayge = all_dest.get_all_voyage()
        new_list = []
        for item in every_voayge:
            if item["flight_nr"] == updated_info["flight_nr"]:
                new_list.append((item["id"], updated_info["distance_from_ice"], updated_info["flight_time"], updated_info["emergency_contact"], updated_info["emergency_contact_phone_nr"]))
            else:
                new_list.append((item["destination"], item["distance_from_ice"], item["flight_time"], item["emergency_contact"], item["emergency_contact_phone_nr"]))
       
        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, 'w', newline='') as self.file_name:
            fields = ["destination", "distance_from_ice", "flight_time", "emergency_contact", "emergency_contact_phone_nr"]
            writer = csv.DictWriter(self.file_name, fieldnames=fields)
            
            writer.writeheader()

        for item in new_list:
            Destination_data().create_destination(item)