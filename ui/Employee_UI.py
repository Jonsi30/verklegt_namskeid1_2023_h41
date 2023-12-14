import os
from ui.ASCII import ascii
from logic.logic_wrapper import Logic_wrapper
from prettytable import PrettyTable

SSN_FIELDNAMES = ["Name", "Social Security Number"]
EMPLOYEE_FILDNAMES = [
    "Name",
    "Role",
    "Rank",
    "License",
    "Phone Number",
    "Address",
    "Email Address",
    "SSN",
]


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

        ssn = """
        
        ssn"""
        print(ssn)
        ssn_input = input("-> ")

        options = """
        [B]ACK
        """
        print(options)

        return Logic_wrapper().create_employee(
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
            self.display_every_employee()
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
            fieldnames = ["Name", "Role", "Rank", "License"]
            table = PrettyTable()
            table.field_names = fieldnames
            for employee in pilots:
                name, role, rank, license = employee
                table.add_row([name, role, rank, license])
            print((table))

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
            SSN_FIELDNAMES = ["Name", "Role"]
            table = PrettyTable()
            table.field_names = SSN_FIELDNAMES
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
        [D]ISPLAY ALL EMPLOYEES (see all)
        [G]ET EMPLOYEE SCHEDULE BY WEEK

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
            elif command == "d":
                self.get_all_employees()
            elif command == "n":
                self.create_new_employee()
            elif command == "e":
                self.input_for_edit_employee()
            elif command == "g":
                self.get_certain_employee_schedule()
            else:
                print("invalid input!")

    def get_employee_schedule(self):
        while True:
            logic = Logic_wrapper()
            print("\033[2J\033[H")
            ssn = self.validate_ssn()
            schedule = Logic_wrapper().get_certain_employee_schedule(ssn)
            print(schedule)
            options = """ 
            [Q]UIT

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "q":
                break

            return ssn


    def get_certain_employee_schedule(self):
        while True:
            print("\033[2J\033[H")
            ssn = self.validate_ssn()
            
            year = int(input("Enter in a year number: "))
            if year < 2023 or year > 2026:
                while year < 2023 or year > 2026:
                    print("Invalid year number, try again")
                    year = int(input("Enter in a year number: "))
            try:
                week = int(input("Enter in a week number: "))
                
                if week > 52 or week < 1:
                    while week > 52 or week < 1:
                        print("Invalid week number, try again")
                        week = int(input("Enter in a week number: "))
            except ValueError: print("Invalid week number, try again")
            
            employee_voyages = Logic_wrapper().get_employee_week_schedule(year, week, ssn)
            voyage_table = PrettyTable()
            fieldnames = ["Name", "Voyage Id", "Role", "Dep.Time", "Arr.Time Back", "Destination", "Week", "Year"]
            voyage_table.field_names = fieldnames
            
            name = ""
            role = ""

            all_employees = Logic_wrapper().get_all_employees()
            for employee in all_employees:
                if employee.ssn == ssn:
                    name += employee.name
                    role += employee.role

            if employee_voyages:
                for voyage in employee_voyages:
                    voyage_table.add_row([name, voyage.id, role, voyage.dep_time, voyage.arr_time_back, voyage.arr_at, week, year])
                print(voyage_table)


            else: print(f"No voyages scheduled for this employee in the week nr: {week} in the year: {year}")
            options = """ 
            [Q]UIT

            """
            print(options)
            command = input("=> ")
            command = command.lower()
            if command == "q":
                break

            return ssn

    def validate_ssn(self):
        all_employees = Logic_wrapper().get_all_crew()

        ssn_table = PrettyTable()
        fieldnames = ["Name", "SSN"]
        ssn_table.field_names = fieldnames

        ssn_list = []

        for info in all_employees:
            ssn_list.append(info.ssn)
            ssn_table.add_row([info.name, info.ssn])

        print(ssn_table)
        ssn_input = input("Enter a ssn from the list above: ")

        if ssn_input not in ssn_list:
            while ssn_input not in ssn_list:
                print(ssn_table)
                print("That id is not in the list above, try again")
                ssn_input = input("Enter a ssn from the list above: ")

        return ssn_input

    def get_available_staff(self):
        while True:
            print("\033[2J\033[H")
            print("INPUT DATE (DD.MM.YYYY):")
            date = input("=> ")
            print(f"Employees available for the date: {date}:")
            cabin_crew = Logic_wrapper().get_available_staff(date)
            SSN_FIELDNAMES = ["Name", "Role", "Rank"]
            table = PrettyTable()
            table.field_names = SSN_FIELDNAMES

            for employee in cabin_crew:
                name, role, rank = employee
                table.add_row([name, role, rank])
            print((table))

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

        all_employees = Logic_wrapper().get_all_employees()

        employee_ssn_table = PrettyTable()
        employee_ssn_list = []
        employee_ssn_table.field_names = SSN_FIELDNAMES

        for employee in all_employees:
            employee_ssn_table.add_row([employee.name, employee.ssn])
            employee_ssn_list.append(employee.ssn)

        print(employee_ssn_table)

        ssn = """ 
        
        Enter the social security number of the employee you want to edit"""
        print(ssn)
        ssn_input = input("=> ")

        run = 0
        while run != 1:
            if ssn_input not in employee_ssn_list:
                print("That Social security number is not valid, try again!")
                ssn_input = input("=> ")
            else:
                run += 1
                break

        employee_table = PrettyTable()
        employee_filendames = EMPLOYEE_FILDNAMES
        employee_table.field_names = employee_filendames

        for employee in all_employees:
            if employee.ssn == ssn_input:
                employee_table.add_row(
                    [
                        employee.name,
                        employee.role,
                        employee.rank,
                        employee.license,
                        employee.phone_nr,
                        employee.address,
                        employee.email,
                        employee.ssn,
                    ]
                )

        print(employee_table)
        role = """ 
        
        role"""
        print(role)
        role_input = input("=> ")
        if role_input != "Pilot" and role_input != "Cabincrew" and role_input != "":
            while (
                role_input != "Pilot" and role_input != "Cabincrew" and role_input != ""
            ):
                print("That is not a real role! try again.")
                role_input = input("=> ")

        rank = """
        
        Rank"""
        print(rank)
        rank_input = input("=> ")
        if (
            rank_input != "Copilot"
            and rank_input != "Captain"
            and rank_input != "Flight Service Manager"
            and rank_input != "Flight Attendant"
            and rank_input != ""
        ):
            while (
                rank_input != "Copilot"
                and rank_input != "Captain"
                and rank_input != "Flight Service Manager"
                and rank_input != "Flight Attendant"
                and rank_input != ""
            ):
                print("That is not a real rank! try again.")
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

    def display_every_employee(self):
        all_employees = Logic_wrapper().get_all_crew()
        employee_table = PrettyTable()
        fieldnames = EMPLOYEE_FILDNAMES
        employee_table.field_names = fieldnames

        for employee in all_employees:
            employee_table.add_row(
                [
                    employee.name,
                    employee.role,
                    employee.rank,
                    employee.license,
                    employee.phone_nr,
                    employee.address,
                    employee.email,
                    employee.ssn,
                ]
            )

        print(employee_table)
