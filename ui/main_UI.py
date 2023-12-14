import os

from logic.logic_wrapper import Logic_wrapper
from ui.voyage_UI import voyage
from ui.Destination_UI import destination
from ui.Aircraft_UI import Aircraft
from ui.ASCII import ascii
from ui.Employee_UI import employee


# Class for the landing page and main menus
class main_UI:
    def __init__(self):
        self.logicwrapper = Logic_wrapper()
        pass

        # prints out and asks for input for the landing page

    def landing_page_input_prompt(self):
        lp = ascii.landing_page(self)
        print(lp)

        while True:

            command = input("=> ")
            command = command.lower()
            if command == "q":
                os.system("cls" if os.name == "nt" else "clear")
                print("shutting down")
                break
            elif command == "m":
                self.manager_menu_input_prompt()
                break
            elif command == "d":
                self.director_menu_input_prompt()
                break
            elif command == "e":
                employee().get_certain_employee_schedule()
                break
            else:
                print("invalid input!")

    # Prints the manager menu for the user
    def manager_menu(self):
        manager_ui = """
    Welcome Manager 

    [0] Voyage List  
    [1] View All Employees

    
    [Q]UIT
    """

        print(manager_ui)

    # gets input for manager menu
    def manager_menu_input_prompt(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            ascii().manager_menu_art()
            self.manager_menu()
            command = input("=> ")
            command = command.lower()
            if command == "q":
                os.system("cls" if os.name == "nt" else "clear")
                print("shutting down")
                break
            elif command == "0":
                voyage().Voyage_list_manager()
            elif command == "1":
                employee().get_all_crew()
            else:
                print("invalid input!")

    # prints the director menu for the user
    def director_menu(self):
        """prints director page and asks for input"""
        director_ui = """
    Welcome Director 

    [0] Voyage List  
    [1] Create Voyage
    [2] View All Airplanes
    [3] View All Destinations


    [Q]UIT 
    """

        print(director_ui)

    # gets input for director menu
    def director_menu_input_prompt(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(ascii().director_menu_art())
            self.director_menu()
            v = voyage()
            command = input("=> ")
            command = command.lower()
            if command == "q":
                os.system("cls" if os.name == "nt" else "clear")
                print("shutting down")
                break
            elif command == "0":
                v.Voyage_list_director()
            elif command == "1":
                v.input_for_create_new_voyage()
            elif command == "2":
                Aircraft().get_all_aircrafts()
            elif command == "3":
                destination().get_all_destinations()
            else:
                print("invalid input!")
