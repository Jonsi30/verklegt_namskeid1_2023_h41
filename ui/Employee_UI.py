import os
from ui.ASCII import ascii
from logic.logic_wrapper import Logic_wrapper


class employee:
    def __init__(self):
        pass

    def create_new_employee(self):
        os.system("cls" if os.name == "nt" else "clear")
        name = """
        Please Input The Following Details
        ----------------------------------
        name"""
        print(name)
        name_input = input("=> ").lower()

        role = """ 
        
        role"""
        print(role)
        role_input = input("=> ").lower()

        rank = """
        
        Duration (hrs:minutes)"""
        print(rank)
        rank_input = input("=> ").lower()

        License = """
        
        License"""
        print(License)
        License_input = input("=> ").lower()

        phone = """
        
        phone"""
        print(phone)
        phone_input = input("=> ").lower()

        address = """
        
        address"""
        print(address)
        address_input = input("=> ").lower()

        email = """
        
        email"""
        print(email)
        email_input = input("=> ").lower()

        ssn = """
        
        ssn"""
        print(ssn)
        ssn_input = input("-> ").lower()

        options = """
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
            command = input("=> ").lower()
            if command == "b":
                return

    def get_all_employees(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("ALL EMPLOYEES")
            options = """ 
            [B]ACK

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return

    def get_all_pilots(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(Logic_wrapper().get_all_pilots())
            options = """ 
            [B]ACK

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return

    def get_all_cabin_crew(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("CREW")
            options = """ 
            [B]ACK

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
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

        [B]ACK

        """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return
            elif command == "p":
                self.get_all_pilots()
            elif command == "c":
                self.get_all_cabin_crew()
            elif command == "s":
                self.get_certain_employee_schedule()
            elif command == "n":
                self.create_new_employee()
            else:
                print("invalid input!")

    def get_certain_employee_schedule(self):
        while True:
            logic = Logic_wrapper()
            os.system("cls" if os.name == "nt" else "clear")
            print("INPUT EMPLOYEE SSN:")
            ssn = input("=> ")
            logic.get_by_ssn()
            options = """ 
            [B]ACK

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return

            return ssn

    def get_all_available_employees(self):
        return

    def get_all_occupied_employees(self):
        return

    def update_employee(self):
        return
