import os


class manager_path:
    def __init__(self):
        pass

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
