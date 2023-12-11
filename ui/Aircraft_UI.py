import os
from ui.ASCII import ascii


class Aircraft:
    def __init__(self):
        pass

    def create_new_aircraft(self):
        os.system("cls" if os.name == "nt" else "clear")
        new_insigna = """
        Please Input The Following Details
        ----------------------------------
        plane_insigna(TF-XXX)"""
        print(new_insigna)
        insigna_input = input("-> ").lower()

        type = """ 
        
        plane_type_id(NAxxxxx)"""
        print(type)
        type_input = input("-> ").lower()

        manufacturor = """
        
        manufacturor"""
        print(manufacturor)
        manu_input = input("-> ").lower()

        seat_capacity = """
        
        number of seats"""
        print(seat_capacity)
        seat_input = input("-> ").lower()

        return insigna_input, type_input, manu_input, seat_input

    def input_for_create_new_aircraft(self):
        self.create_new_aircraft()
        while True:
            command = input("select action: ").lower()
            if command == "q":
                print("shutting down")
                break
            elif command == "b":
                return

    def get_all_aircrafts(self):
        os.system("cls" if os.name == "nt" else "clear")
        ascii().Aircraft_list_art()
        print("aircrafts")
        print("-----------------------")
        options = """
        [N]EW 
        [Q]UIT
        [B]ACK
        """
        print(options)

        while True:
            command = input("select action: ").lower()
            if command == "n":
                self.input_for_create_new_aircraft()
            elif command == "q":
                print("shutting down")
                break
            elif command == "b":
                return

    def update_aircraft(self):
        return
