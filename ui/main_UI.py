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

    [q] Quit 
    [b] Back
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


    [q] Quit 
    [b] Back
    """

        print(director_ui)
        input_str = input("Select Option: ").lower()
        return input_str
