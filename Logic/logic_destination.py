from data.data_wrapper import Data_wrapper
from model.destination import Destination


class LogicDestination:
    def __init__(self) -> None:
        self.destination = Data_wrapper()

    def create_destination(
        self,
        destination,
        distance_from_ice,
        flight_time,
        emergency_contact,
        emergency_contact_phone_nr,
    ):
        new_info = Destination(
            destination,
            distance_from_ice,
            flight_time,
            emergency_contact,
            emergency_contact_phone_nr,
        )

        return self.destination.create_destination(new_info)

    def get_all_destinations(self):
        all_destinations = self.destination.get_all_destinations()

        for i in all_destinations:
            print(i)

    def update_emergency_contact(self, emergency_contact, emergency_contact_phone_nr):
        updated_info = emergency_contact, emergency_contact_phone_nr

        return self.destination.update_emergency_contact(updated_info)

    def update_destination_info(self, new_info):#new info er model af destination klasanum
        return self.destination.update_destination(new_info)
