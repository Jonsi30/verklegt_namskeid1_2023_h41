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
        id_input = input("=>: ")

        flight_nr = """
        flight_nr(fx. NA010)"""
        print(flight_nr)
        flight_nr_input = input("=>: ")

        dep_from = """
        dep_from(fx. RKV)"""
        print(dep_from)
        dep_from_input = input("=>: ")

        arr_at = """
        arr_at(fx. TOR)"""
        print(arr_at)
        arr_at_input = input("=>: ")

        dep_time = """
        dep_time(fx. 00:00 16.12.2023)"""
        print(dep_time)
        dep_time_input = input("=>: ")

        arr_time = """
        arr_time(05:00 16.12.2023)"""
        print(arr_time)
        arr_time_input = input("=>: ")
        
        dep_time_back = """
        dep_time_back(12:00 16.12.2023)"""
        print(dep_time_back)
        dep_time_back_input = input("=>: ")


        arr_time_back = """
        arr_time_back(17:00 16.12.2023)"""
        print(arr_time_back)
        arr_time_back_input = input("=>: ")

        plane_insignia = """
        plane_insignia(TF-XXX)"""
        print(plane_insignia)
        plane_insignia_input = input("=>: ")

        options = """
        [B]ACK
        """

        print(options)

        return Logic_wrapper().create_voyage(
            id_input,
            flight_nr_input,
            dep_from_input,
            arr_at_input,
            dep_time_input,
            arr_time_input,
            dep_time_back_input,
            arr_time_back_input,
            plane_insignia_input,
            "Unassigned",
            "Unassigned",
            "Unassigned",
            "Unassigned",
        )

    def input_for_create_new_voyage(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.create_new_voyage()
            command = input("=> ").lower()

            if command == "b":
                return

    def Voyage_list_director(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(ascii().voyage_list_art())
            for voyage in Logic_wrapper().display_voyage():
                print(voyage)
            options = """
        [B]ACK
        """

            print(options)
            command = input("=> ")

            if command == "b":
                return

    def Voyage_list_manager(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(ascii().voyage_list_art())
            for voyage in Logic_wrapper().display_voyage():
                print(voyage)
            print("[A]DD EMPLOYEES")
            options = """
        [B]ACK
        """

            print(options)
            command = input("=> ")

            if command == "q":
                os.system("cls" if os.name == "nt" else "clear")
                print("shutting down")
                break
            elif command == "b":
                return
            elif command == "a":
                self.input_for_create_add_crew()

    def get_specific_day_voyages(self):
        return

    def add_crew_to_voyage(self):
        
        voyage_id = """
        input voyage id"""
        print(voyage_id)
        voyage_id_input = input("=> ")

        captain = """
        captain(fx. John Johnson)"""
        print(captain)
        captain_input = input("=> ")

        copilot = """
        copilot(fx. John Mikeson)"""
        print(copilot)
        copilot_input = input("=> ")

        head_of_service = """
        head_of_service(fx. Mike Johnson)"""
        print(head_of_service)
        head_of_service_input = input("=> ")

        flight_attendant = """
        flight_attendant(fx. Mike Mikeson)"""
        print(flight_attendant)
        flight_attendant_input = input("=> ")

        options = """
        [B]ACK
        """
        print(options)

        return Logic_wrapper().add_voyage_crew(
            voyage_id_input,
            captain_input,
            copilot_input,
            head_of_service_input,
            flight_attendant_input,
        )

    def input_for_create_add_crew(self):
        self.add_crew_to_voyage()
        while True:
            command = input("=> ").lower()
            if command == "b":
                return
