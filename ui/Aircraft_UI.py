import os
from ui.ASCII import ascii
from logic.logic_wrapper import LogicAircraft
from prettytable import PrettyTable
from logic.logic_wrapper import Logic_wrapper

class Aircraft:
    def __init__(self):
        pass

    def create_new_aircraft(self):
        print("\033[2J\033[H")
        new_insigna = """
        Please Input The Following Details
        ----------------------------------
        plane_insigna(TF-XXX)"""
        print(new_insigna)
        insigna_input = input("=> ").upper()
        while Logic_wrapper().validate_plane_insignia(insigna_input) == False:
            print("Invalid plane insignia, must be in the format: TF-XXX, try again!")
            insigna_input = input("=> ").upper()

        type = """ 
        
        plane_type_id(NAxxxxx)"""
        print(type)
        type_input = input("=> ")
        while Logic_wrapper().validate_plane_type_id(type_input) == False:
            print("Invalid plane type id, must be on this format: NAxxxxx, try again!")
            type_input = input("=> ")

        manufacturor = """
        
        manufacturor"""
        print(manufacturor)
        manu_input = input("=> ")
        while Logic_wrapper().validate_manu_input(manu_input, type_input) == False:
            print("Invalid manufacturer name, manufacturer name must include the plane type in it, try again!")
            manu_input = input("=> ")
        
        
        seat_capacity = """
        
        number of seats"""
        print(seat_capacity)
        seat_input = input("=> ")
        while Logic_wrapper().validate_seat_input(seat_input) == False:
            print("Seat number must be all digits, try again!")
            seat_input = input("=> ")

        
        options = """
        Aircraft has been created!
        [B]ACK"""
        print(options)

        return Logic_wrapper().create_aircraft(insigna_input, type_input, manu_input, seat_input)


    def input_for_create_new_aircraft(self):
        self.create_new_aircraft()
        while True:
            command = input("=>").lower()
            if command == "b":
                return

    def get_all_aircrafts(self):
        print("\033[2J\033[H")
        ascii().Aircraft_list_art()
        
        
        

        all_aircrafts = LogicAircraft().get_all_aircrafts()
        fieldnames = ["Plane Insignia", "Plane Type", "Manufacturer", "Seat Capacity"]
        table = PrettyTable()
        table.field_names = fieldnames
        for aircraft in all_aircrafts:
            
            table.add_row([aircraft.plane_insignia, aircraft.plane_type_id, aircraft.manufacturer, aircraft.seat_capacity])
        print((table))

        options = """
        [N]EW 
        [B]ACK
        """
        print(options)

        while True:
            command = input("=>: ").lower()
            if command == "n":
                self.input_for_create_new_aircraft()
                break
            elif command == "b":
                return

    def update_aircraft(self):
        return
