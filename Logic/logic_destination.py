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