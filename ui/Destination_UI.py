import os
from ui.ASCII import ascii

from prettytable import PrettyTable


class destination:
    def __init__(self):
        pass

    def create_new_destination(self):
        from logic.logic_wrapper import Logic_wrapper
        print("\033[2J\033[H")
        new_destination = """
        Please Input The Following Details
        ----------------------------------
        destination"""
        print(new_destination)
        dest_input = input("=> ")

        distance = """ 
        
        distance from iceland (km)"""
        print(distance)
        dist_input = input("=> ")

        duration = """
        
        Duration (hrs:minutes)"""
        print(duration)
        dura_input = input("=> ")

        Contact = """
        
        Emergency contact"""
        print(Contact)
        contact_input = input("=> ")

        Number = """
        
        emergency contact phone_nr"""
        print(Number)
        contact_nr_input = input("=> ")

        options = """
        [B]ACK
        """
        print(options)

        return Logic_wrapper().create_destination(dest_input, dist_input, dura_input, contact_input, contact_nr_input)

    def input_for_create_new_destination(self):
        self.create_new_destination()
        while True:
            command = input("=>").lower()
            if command == "b":
                return

    def get_all_destinations(self):
        from logic.logic_wrapper import Logic_wrapper

        print("\033[2J\033[H")
        ascii().destination_list_art()

        all_dest = Logic_wrapper().get_all_destinations()
        fieldnames = [
            "Destination",
            "Distance from Iceland(KM)",
            "Flight Time",
            "Emergency Contact",
            "Emergency Contact Phone Number",
        ]
        table = PrettyTable()
        table.field_names = fieldnames
        for destination in all_dest:
            table.add_row(
                [
                    destination.destination,
                    destination.distance_from_ice,
                    destination.flight_time,
                    destination.emergency_contact,
                    destination.emergency_contact_phone_nr,
                ]
            )
        print((table))

        get_all_destinations = """
        [N]EW 
        [B]ACK
        """
        print(get_all_destinations)

        while True:
            command = input("=> ").lower()
            if command == "n":
                self.create_new_destination()
                break
            elif command == "b":
                return
