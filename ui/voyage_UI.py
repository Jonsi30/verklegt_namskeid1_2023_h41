import os
from logic.logic_wrapper import Logic_wrapper
from ui.ASCII import ascii
from prettytable import PrettyTable


class voyage:
    def __init__(self):
        self.get_all_voyages = Logic_wrapper()

    def create_new_voyage(self):
        
        
        taken_voyage_ids = Logic_wrapper().get_all_voyage_ids()
        all_destinations_id = Logic_wrapper().get_all_dest_ids()

        id = f"""
        Input a new ID(fx. 1111)
        Id's that are unavailable are as follows: {", ".join(taken_voyage_ids)}"""
        print(id)
        id_input = input("=>: ")
        while Logic_wrapper().validate_voyage_id(id_input) == False:
            print(id)
            print("ID is either in the list above, or invalid, ID must be 4 digits, try again!")
            id_input = input("=>: ")

        arr_at = f"""
        Input destination ID for the place you are arriving at(fx. TOR)
        Destination ID's we fly too are: {", ".join(all_destinations_id)}"""
        print(arr_at)
        arr_at_input = input("=>: ")
       
        while Logic_wrapper().validate_voyage_dest(arr_at_input) == False:
            print(f'Invalid destination id!, please select one these options: {", ".join(all_destinations_id)}')
            arr_at_input = input("=>: ")

        flight_time = Logic_wrapper().get_flight_time_from_dest_id(arr_at_input)

        flight_nr_input = Logic_wrapper().generate_flight_number(arr_at_input)

        dep_time = """
        Input Departure time(fx. 00:00 16.12.2023)"""
        print(dep_time)
        dep_time_input = input("=>: ")
        while Logic_wrapper().validate_departure_time(dep_time_input) == False:
            print("Invalid departure time, format must be: MM:HH dd.mm.yy fx. 00:00 16.12.2023")
            dep_time_input = input("=>: ")
        
        day, month, year, all_hours, all_minutes = Logic_wrapper().date_and_time_formatter(dep_time_input, flight_time)
        arr_time = Logic_wrapper().arrival_time_and_date(day, month, year, all_hours, all_minutes)
        
        print(f"\n\tThe arrival to {arr_at_input} is {arr_time}\n")
        
        dep_time_back = """
        Input Departure Time Back, must be in this format: 12:00 16.12.2023)"""
        print(dep_time_back)
        dep_time_back_input = input("=>: ")
        while Logic_wrapper().validate_dep_time_back(arr_time, dep_time_back_input) == False:
            print("Invalid departure time back, departure time back must be after arrival date!")
            dep_time_back_input = input("=>: ")



        day, month, year, all_hours, all_minutes = Logic_wrapper().date_and_time_formatter(dep_time_back_input, flight_time)
        arr_time_back = Logic_wrapper().arrival_time_and_date(day, month, year, all_hours, all_minutes)

        print(f"\n\tThe arrival to RVK is {arr_time_back}\n")

        available_airplanes = Logic_wrapper().get_available_airplanes(dep_time_input)
        
        available_airplanes_insignia_list = Logic_wrapper().get_available_plane_insignia(available_airplanes)

        plane_table = PrettyTable()
        fieldnames = ["Plane Insignia", "Plane Type ID"]
        plane_table.field_names = fieldnames
        for aircraft in available_airplanes:
            plane_table.add_row([aircraft.plane_insignia, aircraft.plane_type_id])
            

        print(f"\nAvailable planes:\n{plane_table}")

        plane_insignia = """
        Input Plane Insignia of an available plane fx.(TF-XXX)"""
        print(plane_insignia)
        plane_insignia_input = input("=>: ")
        
        
        if plane_insignia_input not in available_airplanes_insignia_list:
            while plane_insignia_input not in available_airplanes_insignia_list:
                print("\n\tNo airplane with that plane insignia is available! Please try again.")
                plane_insignia_input = input("=>: ")

        return Logic_wrapper().create_voyage(
            id_input,
            flight_nr_input,
            "RVK",
            arr_at_input,
            dep_time_input,
            arr_time,
            dep_time_back_input,
            arr_time_back,
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
            options = """
        Voyage has succesfully been created!
        [B]ACK
        """

            print(options) 
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


    def add_crew_to_voyage(self):
        """This function lets the manager add Employees to a particular trip, after that it returns the information that the manager put in and cheanges the voyage data."""
        upcoming_voyages = Logic_wrapper().get_all_voyages()


        upcoming_unassigned_voyage_list = Logic_wrapper().get_unstaffed_voyages(upcoming_voyages)
        
        
        if upcoming_unassigned_voyage_list == []:
            print("\nThere are no voyages that needs employees to be added to!")
            return

        fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
        table = PrettyTable()
        table.field_names = fieldnames
        for voyage in upcoming_unassigned_voyage_list:
            table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])

        
        
        
        print((table))
        id_number = (input("Input an Id from the list above, that you want to work with: "))
        
        while Logic_wrapper().validate_voyage_user_input_id(id_number, upcoming_unassigned_voyage_list) == False:
            print((table))
            id_number = (input("Invalid id, input an Id from the list above, that you want to work with: "))

        voyage = Logic_wrapper().get_voyage_from_id_input(id_number)  
        
        fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
        table = PrettyTable()
        table.field_names = fieldnames
                
        table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])
        
        print(f"You will work with the voyage with the id: {id_number}")
        
        print((table))
        print()
        
        available = Logic_wrapper().get_available_staff(voyage.arr_time_back[6:])
            
        captain_list = Logic_wrapper().get_available_captain_info(available)
        copilot_list = Logic_wrapper().get_available_copilot_info(available)
        head_of_service_list = Logic_wrapper().get_available_flight_service_manager_info(available)
        flight_attendant_list = Logic_wrapper().get_available_flight_attendant_info(available)


        captain_table = Logic_wrapper().table_making(captain_list)
        copilot_table = Logic_wrapper().table_making(copilot_list)
        head_of_service_table = Logic_wrapper().table_making(head_of_service_list)
        flight_attendant_table = Logic_wrapper().table_making(flight_attendant_list)

        captain = Logic_wrapper().select_position(captain_list, captain_table, 'Captain', 'Captains')
        copilot = Logic_wrapper().select_position(copilot_list, copilot_table, 'Copilot', 'Copilots'  )
        head_of_service = Logic_wrapper().select_position(head_of_service_list, head_of_service_table, 'Flight Service Manager', 'Flight Service Managers' )
        flight_attendant = Logic_wrapper().select_position(flight_attendant_list, flight_attendant_table, 'Flight Attendant', 'Flight Attendants')

        print("Voyage has been staffed succesfully!")
    
        return Logic_wrapper().add_voyage_crew(
            id_number,
            captain,
            copilot,
            head_of_service,
            flight_attendant,
        )

    def input_for_create_add_crew(self):
        self.add_crew_to_voyage()
        while True:
            options = """
        [B]ACK
        """
            print(options)
            command = input("=> ").lower()
            if command == "b":
                return
