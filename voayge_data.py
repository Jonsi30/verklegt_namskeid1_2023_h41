"""
import csv 
from model.voyage_model import Voyage_Model

def get_all_voyage(self):
        #Display every voyage
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage_Model(row["id"], row["flight_nr"], row["dep_from"], row["arr_at"], row["departure"], row["arrival"], row["plane_insignia"], row["captain"], row["copilot"], row["head_of_service"], row["flight_attendant"]))
        
        return ret_list

    def create_voayge(self, voyage):
        #User can Create Voayge
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
            if item["id"] == updated_info["id"]:
                new_list.append((item["id"], item["flight_nr"], item["dep_from"], item["arr_at"], item["departure"], item["arrival"], item["plane_insignia"], updated_info["captain"], updated_info["copilot"], updated_info["head_of_service"], updated_info["flight_attendant"]))
            else:
                new_list.append((item["id"], item["flight_nr"], item["dep_from"], item["arr_at"], item["departure"], item["arrival"], item["plane_insignia"], updated_info["captain"], updated_info["copilot"], updated_info["head_of_service"], updated_info["flight_attendant"]))
       
        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, 'w', newline='') as self.file_name:
            fields = ["id", "flight_nr", "dep_from", "arr_at", "departure", "arrival", "plane_insignia", "captain", "copilot", "head_of_service", "flight_attendant"]
            writer = csv.DictWriter(self.file_name, fieldnames=fields)
            
            writer.writeheader()

        for item in new_list:
            GetData().create_voayge(item)
"""