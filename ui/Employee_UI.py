import os
from ui.ASCII import ascii


class employee:
    def __init__(self):
        pass

    def create_new_employee(self):
        # os.system("cls" if os.name == "nt" else "clear")
        name = """
        Please Input The Following Details
        ----------------------------------
        name"""
        print(name)
        name_input = input("-> ").lower()

        role = """ 
        
        role"""
        print(role)
        role_input = input("-> ").lower()

        rank = """
        
        Duration (hrs:minutes)"""
        print(rank)
        rank_input = input("-> ").lower()

        License = """
        
        License"""
        print(License)
        License_input = input("-> ").lower()

        phone = """
        
        phone"""
        print(phone)
        phone_input = input("-> ").lower()

        address = """
        
        address"""
        print(address)
        address_input = input("-> ").lower()

        email = """
        
        email"""
        print(phone)
        email_input = input("-> ").lower()

        ssn = """
        
        ssn"""
        print(ssn)
        ssn_input = input("-> ").lower()

        options = """
        [Q]UIT
        [B]ACK
        """
        print(options)

        return (
            name_input,
            role_input,
            rank_input,
            License_input,
            phone_input,
            address_input,
            email_input,
            ssn_input,
        )

    def input_for_create_new_destination(self):
        self.create_new_destination()
        while True:
            command = input("select action: ").lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return

    def get_all_employees(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("ALL EMPLOYEES")
            options = """ 
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

    def get_all_pilots(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("ALL PILOTS")
            options = """ 
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

    def get_all_cabin_crew(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("CREW")
            options = """ 
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
        [S]CHEDULE FOR EMPLOYEE
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
                self.get_all_pilots()
            elif command == "c":
                self.get_all_cabin_crew()
            elif command == "s":
                self.get_certain_employee_schedule()
            else:
                print("invalid input!")

    def get_certain_employee_schedule(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("INPUT EMPLOYEE SSN:")
            ssn = input("")
            print("emplyee schedule")
            options = """ 
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

            return ssn

    def get_all_available_employees(self):
        return

    def get_all_occupied_employees(self):
        return

    def update_employee(self):
        return
