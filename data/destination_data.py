import csv
from model.destination import Destination
from ui.Destination_UI import destination

class Destination_data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/destinations.csv" #filenameið sem inniheldur info um þetta class

    def get_all_destination(self):
        
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Destination(row["destination"], row["distance_from_ice"], row["flight_time"], row["emergency_contact"], row["emergency_contact_phone_nr"]))
        return ret_list

    def create_destination(self, destination_instance):
        #User can Create Destination
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["destination", "distance_from_ice", "flight_time", "emergency_contact", "emergency_contact_phone_nr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'destination': destination_instance[0],'distance_from_ice': destination_instance[1], 'flight_time': destination_instance[2], 'emergency_contact': destination_instance[3], 'emergency_contact_phone_nr': destination_instance[4] })

    def update_destination(self, updated_dest):
        #*sækja öll destination
        #loopa yfir destinations
            #ef ég finnd match á id í updated of current dest þá geri ég breytingarnar
        #tæma skránna
        # write flag "w" writeheader()
        #kalla á create destination for each dest í þessum list *
        all_dest = Destination_data()
        every_dest = all_dest.get_all_destination()
        new_list = []
        for item in every_dest:
            if item["destination"] == updated_dest["destination"]:
                new_list.append((updated_dest["destination"], updated_dest["distance_from_ice"], updated_dest["flight_time"], updated_dest["emergency_contact"], updated_dest["emergency_contact_phone_nr"]))
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