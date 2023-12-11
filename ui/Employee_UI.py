import os
from ui.ASCII import ascii


class employee:
    def __init__(self):
        pass

    def create_new_employee(self):
        return

    def get_all_employees(self):
        return

    def get_all_pilots(self):
        return

    def get_all_crew(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            ascii().employee_list_art()
            print("maggi faggi")
            options = """
        [P]ILOTS
        [C]ABIN CREW
        [Q]UIT
        [B]ACK
        """
            print(options)
            command = input("Enter yer command sire!: ")
            command = command.lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return
            elif command == "0":
                pass
            elif command == "1":
                pass
            else:
                print("invalid input!")

    def get_all_available_employees(self):
        return

    def get_all_occupied_employees(self):
        return

    def update_employee(self):
        return
