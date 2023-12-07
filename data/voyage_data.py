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
        # Display every voyage
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage_Model(row["id"], row["flight_nr"], row["dep_from"], row["arr_at"], row["dep_time"], row["arr_time"], row["dep_time_back"], row["arr_time_back"], row["plane_insignia"], row["captain"], row["copilot"], row["head_of_service"], row["flight_attendant"]))
        
        return ret_list

    def create_voyage(self, new_voyage):
        #User can Create Voayge
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "flight_nr", "dep_from", "arr_at", "dep_time", "arr_time", "dep_time_back", "arr_time_back", "plane_insignia", "captain", "copilot", "head_of_service", "flight_attendant"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': new_voyage[0],'flight_nr': new_voyage[1], 'dep_from': new_voyage[2], 'arr_at': new_voyage[3], 'dep_time': new_voyage[4], 'arr_time': new_voyage[5], 'dep_time_back': new_voyage[6], 'arr_time_back': new_voyage[7], 'plane_insignia': new_voyage[8], 'captain': new_voyage[9], 'copilot': new_voyage[10], 'head_of_service': new_voyage[11], 'flight_attendant': new_voyage[12] })

    def update_voyage(self, updated_info):
        all_dest = GetData()
        every_voayge = all_dest.get_all_voyage()
        new_list = []
        for item in every_voayge:
            if item["id"] == updated_info["id"]:
                new_list.append((item["id"], item["flight_nr"], item["dep_from"], item["arr_at"], item["dep_time"], item["arr_time"], item["dep_time_back"], item["arr_time_back"], item["plane_insignia"], updated_info["captain"], updated_info["copilot"], updated_info["head_of_service"], updated_info["flight_attendant"]))
            else:
                new_list.append((item["id"], item["flight_nr"], item["dep_from"], item["arr_at"], item["dep_time"], item["arr_time"], item["dep_time_back"], item["arr_time_back"], item["plane_insignia"], updated_info["captain"], updated_info["copilot"], updated_info["head_of_service"], updated_info["flight_attendant"]))
       
        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, 'w', newline='') as self.file_name:
            fields = ["id", "flight_nr", "dep_from", "arr_at", "dep_time", "arr_time", "dep_time_back", "arr_time_back" "plane_insignia", "captain", "copilot", "head_of_service", "flight_attendant"]
            writer = csv.DictWriter(self.file_name, fieldnames=fields)

            writer.writeheader()

        for item in new_list:
            GetData().create_voyage(item)
