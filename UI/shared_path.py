from logic.logic_wrapper import logic_wrapper
from logic.voyage_details import Voyage_details


class Shared_Path:
    def __init__(self):
        """Constructor for Main_menu"""
        self.logicwrapper = logic_wrapper()
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
