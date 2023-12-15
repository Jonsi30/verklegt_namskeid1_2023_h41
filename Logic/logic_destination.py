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
    
    def validate_dest_id_input_create(self, dest_id_input) -> bool:
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
    
    def validate_emergency_contact_name_input(self, emerg_name_input) -> bool:
        
        """Emergency contact name can't include digits, and can't be longer than 20 letters"""
        
        if len(emerg_name_input) < 40 and len(emerg_name_input) >= 2:
            for letter in emerg_name_input:
                if letter.isdigit():
                    return False
            return True       
        return False
    
    def validate_phone_nr(self, contact_nr_input) -> bool:
        """Phone number can't include letters"""
        
        if len(contact_nr_input) == 7:
            for number in contact_nr_input:
                 if number.isalpha():
                    return False
            return True       
        return False
        

    def validate_dest_id_input(self, dest_id_input) -> bool:
        all_dest = LogicDestination().get_all_destinations()
        

        for destination in all_dest:
            if dest_id_input == destination.destination_id:
                return True

        return False
    

    def get_all_dest_ids(self) -> list:
        all_dest = LogicDestination().get_all_destinations()
        ids = []
        
        for dest in all_dest:
            ids.append(dest.destination_id)

        return ids

    def get_flight_time_from_dest_id(self, id) ->str:
        
        for dest in self.get_all_destinations():
            if dest.destination_id == id:
                return dest.flight_time