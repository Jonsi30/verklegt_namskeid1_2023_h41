import os


class director_path:
    def __init__(self):
        pass

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
