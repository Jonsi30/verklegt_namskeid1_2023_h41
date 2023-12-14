import os
from logic.logic_wrapper import Logic_wrapper
from ui.ASCII import ascii
from prettytable import PrettyTable

class voyage:
    def __init__(self):
        self.get_all_voyages = Logic_wrapper()

    def create_new_voyage(self):
        voyage_id_list = []
        Destination_id_list = []
        all_destinations = []

        for voyage in Logic_wrapper().get_all_voyages():
            voyage_id_list.append(voyage.id)

        for destination in Logic_wrapper().get_all_destinations():
            Destination_id_list.append(destination.destination_id)
            all_destinations.append(destination)

        id = f"""
        Input a new ID(fx. 1111)
        Id's that are unavailable are as follows: {", ".join(voyage_id_list)}"""
        print(id)
        id_input = input("=>: ")
        if id_input in voyage_id_list:
            while id_input in voyage_id_list:
                print("ID has already been created! Please try again.")
                id_input = input("=>: ")

        arr_at = f"""
        Input destination ID for the place you are arriving at(fx. TOR)
        Destination ID's we fly too are: {", ".join(Destination_id_list)}"""
        print(arr_at)
        arr_at_input = input("=>: ")
        if arr_at_input not in Destination_id_list:
            while arr_at_input not in Destination_id_list:
                print("\n\tWe dont fly to any destination with that destination ID! Please try again.")
                arr_at_input = input("=>: ")

        flight_time = ""

        for dest in all_destinations:
            if arr_at_input == dest.destination_id:
                flight_time += dest.flight_time



        flight_nr_input = Logic_wrapper().generate_flight_number(arr_at_input)

        dep_time = """
        Input Departure time(fx. 00:00 16.12.2023)"""
        print(dep_time)
        dep_time_input = input("=>: ")
        
        day, month, year, all_hours, all_minutes = Logic_wrapper().date_and_time_formatter(dep_time_input, flight_time)
        arr_time = Logic_wrapper().arrival_time_and_date(day, month, year, all_hours, all_minutes)
        
        print(f"\n\tThe arrival to {arr_at_input} is {arr_time}\n")
        
        dep_time_back = """
        Input Departure Time Back(12:00 16.12.2023)"""
        print(dep_time_back)
        dep_time_back_input = input("=>: ")

        day, month, year, all_hours, all_minutes = Logic_wrapper().date_and_time_formatter(dep_time_back_input, flight_time)
        arr_time_back = Logic_wrapper().arrival_time_and_date(day, month, year, all_hours, all_minutes)

        print(f"\n\tThe arrival to RVK is {arr_time_back}\n")

        available_airplanes = Logic_wrapper().get_available_airplanes(dep_time_input)
        available_airplanes_insignia_list = []

        plane_table = PrettyTable()
        fieldnames = ["Plane Insignia", "Plane Type ID"]
        plane_table.field_names = fieldnames
        for aircraft in available_airplanes:
            plane_table.add_row([aircraft.plane_insignia, aircraft.plane_type_id])
            available_airplanes_insignia_list.append(aircraft.plane_insignia)

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

        upcoming_voyage_list = []
        for voyage in upcoming_voyages:
            
            if voyage.captain and voyage.copilot and voyage.head_of_service and voyage.flight_attendant == 'Unassigned':
                upcoming_voyage_list.append(voyage)
        
        if upcoming_voyage_list == []:
            print("\nThere are no voyages that needs employees to be added to!")
            return

        fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
        table = PrettyTable()
        table.field_names = fieldnames
        for voyage in upcoming_voyage_list:
            table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])

        voyage_in_work = []
        run = 0
        while run == 0:
            print((table))
            id_number = (input("Input an Id from the list above, that you want to work with: "))
            print()
            for voyage in upcoming_voyage_list:
                if voyage.id == id_number:
                    voyage_in_work.append(voyage)
                    run += 1
                    break
            if run == 0:    
                print("That id is not in the list above! Try again") 
                print() 
        
        for voyage in voyage_in_work:
            fieldnames = ["Id", "Flight Nr", "Plane Insignia", "Captain", "Copilot", "Head of Service", "Flight Attendant"]
            table = PrettyTable()
            table.field_names = fieldnames
            date = ""
            for voayge in voyage_in_work:
                
                table.add_row([voyage.id, voyage.flight_nr, voyage.plane_insignia, voyage.captain, voyage.copilot, voyage.head_of_service, voyage.flight_attendant])
                date += voayge.arr_time_back[6:]
            print(f"You will work with the voyage with the id: {id_number}")
            
            print((table))
            print()
            
        captain_list = []
        copilot_list = []
        head_of_service_list = []
        flight_attendant_list = []

        available = Logic_wrapper().get_available_staff(date)
        for i in available:
            name, role, rank = i
            if rank == 'Captain':
                captain_list.append([name, role, rank])
            elif rank == 'Copilot':
                copilot_list.append([name, role, rank])
            elif rank == 'Flight Service Manager':
                head_of_service_list.append([name, role, rank])
            elif rank == 'Flight Attendant':
                flight_attendant_list.append([name, role, rank])

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
