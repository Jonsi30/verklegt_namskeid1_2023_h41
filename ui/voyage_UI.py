from logic.logic_wrapper import Logic_wrapper
import os
from ui.ASCII import ascii


class voyage:
    def __init__(self):
        self.get_all_voyages = Logic_wrapper()

    def create_new_voyage(self):
        id = """
        id(fx. 1111)"""
        print(id)
        id_input = input("->: ").lower

        flight_nr = """
        flight_nr(fx. NA010)"""
        print(flight_nr)
        flight_nr_input = input("->: ").lower

        dep_from = """
        dep_from(fx. RKV)"""
        print(dep_from)
        dep_from_input = input("->: ").lower

        arr_at = """
        arr_at(fx. TOR)"""
        print(arr_at)
        arr_at_input = input("->: ").lower

        dep_time = """
        dep_time(fx. 00:00 16.12.2023)"""
        print(dep_time)
        dep_time_input = input("->: ").lower

        dep_time_back = """
        dep_time_back(12:00 16.12.2023)"""
        print(dep_time_back)
        dep_time_back_input = input("->: ").lower

        arr_time = """
        arr_time(05:00 16.12.2023)"""
        print(arr_time)
        arr_time_input = input("->: ").lower

        arr_time_back = """
        arr_time_back(17:00 16.12.2023)"""
        print(arr_time_back)
        arr_time_back_input = input("->: ").lower

        plane_insignia = """
        plane_insignia(TF-XXX)"""
        print(plane_insignia)
        plane_insignia_input = input("->: ").lower

        captain = """
        captain(fx. John Johnson)"""
        print(captain)
        captain_input = input("->: ").lower

        copilot = """
        copilot(fx. John Mikeson)"""
        print(copilot)
        copilot_input = input("->: ").lower

        head_of_service = """
        head_of_service(fx. Mike Johnson)"""
        print(head_of_service)
        copilot_input = input("->: ").lower

        flight_attendant = """
        flight_attendant(fx. Mike Mikeson)"""
        print(flight_attendant)
        flight_attendant_input = input("->: ").lower

        options = """
        [Q]UIT
        [B]ACK
        """
        print(options)

        return (
            id_input,
            flight_nr_input,
            dep_from_input,
            arr_at_input,
            dep_time_input,
            dep_time_back_input,
            arr_time_input,
            arr_time_back_input,
            plane_insignia_input,
            captain_input,
            copilot_input,
            flight_attendant_input,
        )

    def input_for_create_new_voyage(self):
        self.create_new_voyage()
        while True:
            command = input("select action: ").lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return

    def Voyage_list(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(ascii().voyage_list_art())
            Logic_wrapper().display_voyage()
            command = input("Enter yer command sire!: ")
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return

    def get_specific_day_voyages(self):
        return

    def update_voyage(self):
        return
