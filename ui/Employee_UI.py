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
        pass

    def get_all_cabin_crew(self):
        pass

    def get_all_crew(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            ascii().employee_list_art()
            print("AVAILABLE EMPLOYEES")
            print("-------------------")
            options = """
        [P]ILOTS (see all)
        [C]ABIN CREW (see all)
        [O]CCUPIED STAFF
        [N]EW EMPLOYEE

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
            elif command == "p":
                self.get_all_pilots
            elif command == "c":
                self.get_all_cabin_crew
            else:
                print("invalid input!")

    def get_all_available_employees(self):
        return

    def get_all_occupied_employees(self):
        return

    def update_employee(self):
        return
