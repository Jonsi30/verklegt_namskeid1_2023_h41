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
AVAILABLE_EMPLOYEE_FIELDNAMES = ["Name", "Role", "Rank"]

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
        while Logic_wrapper().validate_employee_name_input(name_input) == False:
            print("Invalid employee name input, try again!")
            name_input = input("=> ")

        role = """ 
        
        role"""
        print(role)
        role_input = input("=> ").capitalize()
        while Logic_wrapper().validate_employee_role_input(role_input) == False:
            print("Invalid Role input, must be Pilot or Cabincrew, try again!")
            role_input = input("=> ").capitalize()


        rank = """
        
        Rank"""
        print(rank)
        rank_input = input("=> ")
        while Logic_wrapper().validate_employee_rank_input(rank_input, role_input) == False:
            print("Invalid rank input, if Pilot is the role, the rank must be Copilot or Captain.\n If Cabincrew is the role, the rank must be Flight Service Manager or Flight Attendant! Try again!")
            rank_input = input("=> ")
        
        if role_input.lower() == 'pilot':
            
            aircraft_table = PrettyTable()
            aircraft_table.field_names = ["Aircraft"]
            all_aircrafts = Logic_wrapper().get_all_aircraft()
            for aircraft in all_aircrafts:
                aircraft_table.add_row([aircraft.plane_type_id])
            
            print(aircraft_table)
            License = """
            
            Choose the Aircraft license for this pilot from the list above"""
            print(License)
            license_input = input("=> ")
            
            
            while Logic_wrapper().validate_aircraft_license(license_input) == False:
                print(aircraft_table)
                print("That plane license doesn't exist in the list above, try again!")
                license_input = input("=> ")
        else:
            license_input = 'N/A'

        phone = """
        
        phone"""
        print(phone)
        phone_input = input("=> ")
        while Logic_wrapper().validate_employee_phone_nr(phone_input) == False:
            print("Invalid phone number, try again!")
            phone_input = input("=> ")
        
        address = """
        
        address"""
        print(address)
        address_input = input("=> ")
        while Logic_wrapper().validate_employee_address(address_input) == False:
            print("Invalid address input, try again!")
            address_input = input("=> ")

        email = """
        
        email"""
        print(email)
        email_input = input("=> ")
        while Logic_wrapper().validate_employee_email_address(email_input) == False:
            print("Invalid email input, must include @nan.is and be over than 8 letters, try again!")
            email_input = input("=> ")
        
        ssn = """
        
        ssn"""
        print(ssn)
        ssn_input = input("-> ")
        while Logic_wrapper().validate_employee_ssn_input(ssn_input) == False:
            print("Invalid ssn input, must be only digits and 10 digits long, try again!")
            ssn_input = input("-> ")
        
        success_message = f"You've succesfully created {name_input} in the system!"
        print(success_message)
        options = """
        [B]ACK
        """
        print(options)

        return Logic_wrapper().create_employee(
            name_input,
            role_input,
            rank_input,
            license_input,
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
            
            year = input("Enter in a year number: ")
            
            while Logic_wrapper().validate_year_input(year) == False:
                    print("Invalid year number, must be a year between 2023 - 2026, try again!")
                    year = (input("Enter in a year number: "))
            
            week = input("Enter in a week number: ")
            
            while Logic_wrapper().validate_week_input(week) == False:
                print("Invalid week number, try again")
                week = (input("Enter in a week number: "))
                
            employee_voyages = Logic_wrapper().get_employee_week_schedule(year, week, ssn)
            voyage_table = PrettyTable()
            fieldnames = ["Name", "Voyage Id", "Role", "Dep.Time", "Arr.Time Back", "Destination", "Week", "Year"]
            voyage_table.field_names = fieldnames
            
            name = Logic_wrapper().get_employee_name_by_ssn(ssn)
            role = Logic_wrapper().get_employee_role_by_ssn(ssn)

            if employee_voyages != []:
                for voyage in employee_voyages:
                    voyage_table.add_row([name, voyage.id, role, voyage.dep_time, voyage.arr_time_back, voyage.arr_at, week, year])
                
                print(voyage_table)

            else: print(f"No voyages scheduled for this employee in the week nr: {week} in the year: {year}")
            options = """ 
            [B]ACK

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
        
        for info in all_employees:
            ssn_table.add_row([info.name, info.ssn])

        print(ssn_table)
            
        ssn_input = input("Enter a ssn from the list above: ")

        while Logic_wrapper().validate_employee_ssn(ssn_input) == False:
            print("SSN doesn't match any ssn in the list above, try again")
            print(ssn_table)
            ssn_input = input("Enter a ssn from the list above: ")
                
                

        return ssn_input

    def get_available_staff(self):
        while True:
            print("\033[2J\033[H")
            print("INPUT DATE (DD.MM.YYYY):")
            
            date_input = input("=> ")
            while Logic_wrapper().validate_date_input_format(date_input) == False:
                print("Invalid date format, must be DD.MM.YYYY, try again!")
                date_input = input("=> ")


            print(f"Employees available for the date: {date_input}:")
            cabin_crew = Logic_wrapper().get_available_staff(date_input)
            
            table = PrettyTable()
            table.field_names = AVAILABLE_EMPLOYEE_FIELDNAMES

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

            return date_input

    def edit_employee(self):
        print("\033[2J\033[H")
        bang = """
        PRESS ENTER IF ITEM SHOULD NOT CHANGE
        ----------------------------------
        """
        print(bang)

        all_employees = Logic_wrapper().get_all_employees()

        employee_ssn_table = PrettyTable()
        employee_ssn_table.field_names = SSN_FIELDNAMES
        
        for employee in all_employees:
            employee_ssn_table.add_row([employee.name, employee.ssn])
            

        print(employee_ssn_table)

        ssn = """ 
        
        Enter the social security number of the employee you want to edit"""
        print(ssn)
        ssn_input = input("=> ")
        while Logic_wrapper().validate_employee_ssn(ssn_input) == False:
            print("That Social security number is not valid, try again!")
            ssn_input = input("=> ")


        employee_table = PrettyTable()
        employee_table.field_names = EMPLOYEE_FILDNAMES

        employee = Logic_wrapper().get_employee_model_from_ssn(ssn_input)
        
            
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
        if role_input == "":
            role_input = employee.role
        else:
            while Logic_wrapper().validate_employee_role_input(role_input) == False:
                print("Thats not a real role, it can either be Pilot or Cabincrew, try again!")
                role_input = input("=> ")

        rank = """
        
        Rank"""
        print(rank)
        rank_input = input("=> ")
        if rank_input == "":
            rank_input = employee.rank
        else:
            while Logic_wrapper().validate_employee_rank_input(rank_input, role_input) == False:
                print("That's not a real rank, pilot can either be Captain or Copilot, and cabincrew can either be Flight Service Manager or Flight Attendant")
                print("Try again!")
                rank_input = input("=> ")

            if role_input == 'Pilot':
                aircraft_table = PrettyTable()
                aircraft_table.field_names = ["Aircraft"]
                all_aircrafts = Logic_wrapper().get_all_aircraft()
                for aircraft in all_aircrafts:
                    aircraft_table.add_row([aircraft.plane_type_id])
                
                print(aircraft_table)
                
                License = """
            
                Choose the Aircraft license for this pilot from the list above"""
                print(License)
                license_input = input("=> ")
                while Logic_wrapper().validate_aircraft_license(license_input) == False:
                    print(aircraft_table)
                    print("That plane license doesn't exist in the list above, try again!")
                    license_input = input("=> ")

            else:
                license_input = 'N/A'

        phone = """
        
        phone"""
        print(phone)
        phone_input = input("=> ")
        while Logic_wrapper().validate_phone_nr(phone_input) == False:
            print("Not a valid phone number, can't include letters and must be 7 digits, try again!")
            phone_input = input("=> ")  
        
        address = """
        
        address"""
        print(address)
        address_input = input("=> ")
        while Logic_wrapper().validate_employee_address(address_input) == False:
            print("Invalid address input, try again!")
            address_input = input("=> ")

        email = """
        
        email"""
        print(email)
        email_input = input("=> ")
        while Logic_wrapper().validate_employee_email_address(email_input) == False:
            print("Invalid email input, must include @nan.is and be over than 8 letters, try again!")
            email_input = input("=> ")

        success_message = f"You have successfully edited the info for {employee.name}!"
        print(success_message)

        options = """
        [B]ACK
        """
        print(options)

        return Logic_wrapper().update_employee(
            ssn_input,
            role_input,
            rank_input,
            license_input,
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
