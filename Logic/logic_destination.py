from data.data_wrapper import Data_wrapper
from model.destination import Destination
from prettytable import PrettyTable

class LogicDestination:
    def __init__(self) -> None:
        self.destination = Data_wrapper()

    def create_destination(
        self,
        destination,
        destination_id,
        distance_from_ice,
        flight_time,
        emergency_contact,
        emergency_contact_phone_nr,
    ):
        new_info = Destination(
            destination,
            destination_id,
            distance_from_ice,
            flight_time,
            emergency_contact,
            emergency_contact_phone_nr,
        )

        return self.destination.create_destination(new_info)

    def get_all_destinations(self):
        destinations = []

        for dest in Data_wrapper().get_all_destinations():
            destinations.append(dest)
        
        return destinations

    def generate_flight_number(self, dest_id_input):
        """Generates a flight number for the destination that was input into the function"""
        for i, destination in enumerate(Data_wrapper().get_all_destinations()):
            if destination.destination_id == dest_id_input:
                flight_nr = f"NA0{i+1}0"
                break

        return flight_nr
    
    def validate_dest_id_input(self, dest_id_input) -> bool:
        """Must be 3 letter str"""
        if len(dest_id_input) == 3:
            for letter in dest_id_input:
                if letter.isdigit():
                    return False
            return True
        return False
    
    def validate_dest_name_input(self, dest_name_input) -> bool:
        """Lenght must be below 20 letters and over 4 letters str"""
        if len(dest_name_input) < 20 and len(dest_name_input) > 4:
            
            for letter in dest_name_input:
                if letter.isdigit():
                    return False
            return True
        return False
    
    def validate_dest_distance(self, dest_distance) -> bool:
        """Distance must be numeric"""
        
            
        for digit in dest_distance:
                if digit.isalpha():
                    return False
        return True
    
    def validate_dest_duration_input(self, dest_duration) -> bool:
        """Duration must be in a correct from"""
        
        if len(dest_duration) == 5:
            if dest_duration[2] == ":":
                if dest_duration[0].isdigit() and dest_duration[1].isdigit() and dest_duration[3].isdigit() and dest_duration[4].isdigit():
                    hour = ""
                    hour += (dest_duration[0])
                    hour += (dest_duration[1])
                    
                    minutes = ""
                    minutes += (dest_duration[3])
                    minutes += (dest_duration[4])

                    if int(hour) <= 23 and int(minutes) <= 59:
                        return True
                    
        return False