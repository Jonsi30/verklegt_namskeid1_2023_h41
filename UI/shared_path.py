from data.data_wrapper import Data_wrapper


class Shared_path:
    def __init__(self):
        """Constructor for Main_menu"""
        pass

    def landing_page():
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

    def voayge_list():
        """Prints the voyage list for the user"""
        print(Data_wrapper.get_voyage_data())
