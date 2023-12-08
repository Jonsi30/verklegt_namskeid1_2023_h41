import os

from logic.logic_wrapper import Logic_wrapper
from ui.voyage_UI import voyage
from ui.Destination_UI import destination
from ui.Aircraft_UI import Aircraft


class main_UI:
    def __init__(self):
        """Constructor for Main_menu"""
        self.logicwrapper = Logic_wrapper()
        pass

    def landing_page(self):
        """Prints the landing page for the user"""
        landing_ui = """


                                   _
                                __~a~_
                                ~~;  ~_
                  _                ~  ~_                _
                 '_\;__._._._._._._]   ~_._._._._._.__;/_`
                 '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
                 (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
                (/ / / / / | | | ~(/    \) ~ | | \ \ \ \ \)
               (/ / / / /  ~ ~ ~   (/  \)    ~ ~  \ \ \ \ \)
              (/ / / / ~          / (||)|          ~ \ \ \ \)
              ~ / / ~            M  /||\M             ~ \ \ ~
               ~ ~                  /||\                 ~ ~
                                   //||\\
                                   //||\\
                                   //||\\
                                   '/||\'                                                                     
                                                                      
        /|    / /                /|    / /                                
       //|   / /      ___       //|   / /        ___       ( )      __    
      // |  / /     //   ) )   // |  / /       //   ) )   / /     //  ) ) 
     //  | / /     //   / /   //  | / /       //   / /   / /     //       
    //   |/ /     ((___( (   //   |/ /       ((___( (   / /     //        


                                Please Login
                        [m] Manager  [d] director

                                or [q] quit
                    """

        print(landing_ui)
        """Returns the input from the user"""

    def landing_page_input_prompt(self):
        self.landing_page()
        m = main_UI()
        while True:
            command = input("Enter yer command sire!: ")
            command = command.lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "m":
                m.manager_menu_input_prompt()
            elif command == "d":
                m.director_menu_input_prompt()
            else:
                print("invalid input!")

    def manager_menu(self):
        """Prints the manager menu for the user"""
        os.system("cls" if os.name == "nt" else "clear")
        manager_ui = """
    Welcome Manager 

    [0] Voyage List  
    [1] View All Employees

    [Q]UIT
    [B]ACK
    """
        print(manager_ui)

    def manager_menu_input_prompt(self):
        while True:
            self.manager_menu()
            command = input("Enter yer command sire!: ")
            command = command.lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return
            elif command == "0":
                voyage.Voyage_list()
            elif command == "1":
                pass
            else:
                print("invalid input!")

    def director_menu(self):
        """prints director page and asks for input"""
        os.system("cls" if os.name == "nt" else "clear")
        director_ui = """
    Welcome Director 

    [0] Voyage List  
    [1] Create Voyage
    [2] View All Airplanes
    [3] View All Destinations


    [Q]UIT 
    [B]ACK
    """

        print(director_ui)

    def director_menu_input_prompt(self):
        while True:
            self.director_menu()
            v = voyage()
            command = input("Enter yer command sire!: ")
            command = command.lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return
            elif command == "0":
                v.Voyage_list()
            elif command == "1":
                pass
            elif command == "2":
                Aircraft().get_all_aircrafts()
            elif command == "3":
                destination().get_all_destinations()
            else:
                print("invalid input!")
