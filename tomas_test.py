from ui.voyage_UI import voyage
from ui.main_UI import main_UI
from ui.Destination_UI import destination
from ui.Aircraft_UI import Aircraft

# from logic.logic_wrapper import Logic_wrapper


def main():
    m = main_UI()
    user_input = m.landing_page()
    if user_input == "m":
        main_UI.manager_menu()

    elif user_input == "d":
        director_input = main_UI.director_menu()
        if director_input == "0":
            all_voyages = voyage().format_voyages()
            print(all_voyages)
        if director_input == "2":
            Aircraft().get_all_aircrafts()
            director_input = Aircraft().get_all_aircrafts()
            if director_input == "n":
                Aircraft().create_new_aircraft()
        if director_input == "3":
            destination().get_all_destinations()
            director_input = destination().get_all_destinations()
            if director_input == "n":
                destination().create_new_destination()


if __name__ == "main":
    main()


import os

from logic.logic_wrapper import Logic_wrapper


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
        input_str = input("login: ").lower()
        return input_str

    def manager_menu():
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
        input_str = input("Select Option: ").lower()
        return input_str

    def director_menu():
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
        input_str = input("Select Option: ").lower()
        return input_str
