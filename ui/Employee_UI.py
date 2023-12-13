import os
from ui.ASCII import ascii
from logic.logic_wrapper import Logic_wrapper
from prettytable import PrettyTable


class employee:
    def __init__(self):
        pass

    def create_new_employee(self):
        print("\033[2J\033[H")
        name = """
        Please Input The Following Details
        ----------------------------------
        name"""
        print(name)
        name_input = input("=> ")

        role = """ 
        
        role"""
        print(role)
        role_input = input("=> ")

        rank = """
        
        Duration (hrs:minutes)"""
        print(rank)
        rank_input = input("=> ")

        License = """
        
        License"""
        print(License)
        License_input = input("=> ")

        phone = """
        
        phone"""
        print(phone)
        phone_input = input("=> ")

        address = """
        
        address"""
        print(address)
        address_input = input("=> ")

        email = """
        
        email"""
        print(email)
        email_input = input("=> ")

        ssn = """
        
        ssn"""
        print(ssn)
        ssn_input = input("-> ")

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

    def input_for_create_new_employee(self):
        self.create_new_employee()
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
            print("\033[2J\033[H")
            pilots = Logic_wrapper().get_all_pilots()
            for pilot in pilots:
                print(pilot)
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
            print("\033[2J\033[H")
            cabin_crew = Logic_wrapper().get_all_cabincrew()
            fieldnames = ["Name", "Role"]
            table = PrettyTable()
            table.field_names = fieldnames
            for employee in cabin_crew:
                name, role = employee
                table.add_row([name, role])
            print((table))

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
            print("\033[2J\033[H")
            ascii().employee_list_art()
            options = """
        
        [A]VAILABLE EMPLOYEES
        [P]ILOTS (see all)
        [C]ABIN CREW (see all)
        [S]CHEDULE FOR EMPLOYEE

        [E]DIT EMPLOYEE
        [N]EW EMPLOYEE

        [B]ACK

        """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return
            elif command == "a":
                self.get_available_staff()
            elif command == "p":
                self.get_all_pilots()
            elif command == "c":
                self.get_all_cabin_crew()
            elif command == "s":
                self.get_certain_employee_schedule()
            elif command == "n":
                self.create_new_employee()
            elif command == "e":
                self.input_for_edit_employee()
            else:
                print("invalid input!")

    def get_certain_employee_schedule(self):
        while True:
            logic = Logic_wrapper()
            print("\033[2J\033[H")
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

    def get_available_staff(self):
        while True:
            print("\033[2J\033[H")
            print("INPUT DATE (DD.MM.YYYY):")
            date = input("=> ")
            print("employees")
            options = """ 
            [B]ACK

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return

            return date

    def edit_employee(self):
        print("\033[2J\033[H")
        bang = """
        PRESS ENTER IF ITEM SHOULD NOT CHANGE
        ----------------------------------
        """
        print(bang)

        ssn = """ 
        
        SSN"""
        print(ssn)
        ssn_input = input("=> ")

        role = """ 
        
        role"""
        print(role)
        role_input = input("=> ")

        rank = """
        
        Rank"""
        print(rank)
        rank_input = input("=> ")

        License = """
        
        License"""
        print(License)
        License_input = input("=> ")

        phone = """
        
        phone"""
        print(phone)
        phone_input = input("=> ")

        address = """
        
        address"""
        print(address)
        address_input = input("=> ")

        email = """
        
        email"""
        print(email)
        email_input = input("=> ")

        options = """
        [B]ACK
        """
        print(options)

        return Logic_wrapper().update_employee(
            ssn_input,
            role_input,
            rank_input,
            License_input,
            phone_input,
            address_input,
            email_input,
        )

    def input_for_edit_employee_(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("INPUT SSN:")
            date = input("=> ")
            self.edit_employee()
            options = """ 
            [B]ACK

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "b":
                return

            return date

    def input_for_edit_employee(self):
        self.edit_employee()
        while True:
            command = input("=> ").lower()
            if command == "b":
                return
