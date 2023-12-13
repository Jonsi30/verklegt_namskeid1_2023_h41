import os
from logic.logic_wrapper import Logic_wrapper
from ui.ASCII import ascii
from prettytable import PrettyTable

class voyage:
    def __init__(self):
        self.get_all_voyages = Logic_wrapper()

    def create_new_voyage(self):
        id = """
        Input ID(fx. 1111)"""
        print(id)
        id_input = input("=>: ")

        flight_nr = """
        Input Flight Number(fx. NA010)"""
        print(flight_nr)
        flight_nr_input = input("=>: ")

        dep_from = """
        Input Departure from(fx. RKV)"""
        print(dep_from)
        dep_from_input = input("=>: ")

        arr_at = """
        Input Arrival at(fx. TOR)"""
        print(arr_at)
        arr_at_input = input("=>: ")

        dep_time = """
        Input Departure time(fx. 00:00 16.12.2023)"""
        print(dep_time)
        dep_time_input = input("=>: ")

        arr_time = """
        Input Arrival time(05:00 16.12.2023)"""
        print(arr_time)
        arr_time_input = input("=>: ")
        
        dep_time_back = """
        Input Departure Time Back(12:00 16.12.2023)"""
        print(dep_time_back)
        dep_time_back_input = input("=>: ")

        arr_time_back = """
        Input Arrival time Back(17:00 16.12.2023)"""
        print(arr_time_back)
        arr_time_back_input = input("=>: ")

        available_airplanes = Logic_wrapper().get_available_airplanes(dep_time_input)
        
        plane_table = PrettyTable()
        fieldnames = ["Plane Insignia", "Plane Type ID"]
        plane_table.field_names = fieldnames
        for aircraft in available_airplanes:
            plane_table.add_row([aircraft.plane_insignia, aircraft.plane_type_id])

        print(plane_table)

        plane_insignia = """
        Input Plane Insignia(TF-XXX)"""
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


    def add_crew_to_voyage(self):
        """This function lets the manager add Employees to a particular trip, after that it returns the information that the manager put in and cheanges the voyage data."""
        upcoming_voyages = Logic_wrapper().get_all_voyages()

        upcoming_voyage_list = []
        for voyage in upcoming_voyages:
            
            if voyage.captain and voyage.copilot and voyage.head_of_service and voyage.flight_attendant == 'Unassigned':
                upcoming_voyage_list.append(voyage)

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
        Voyage has been staffed succesfully!
        [B]ACK
        """
            print(options)
            command = input("=> ").lower()
            if command == "b":
                return
