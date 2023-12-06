import os


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

    def get_all_aircrafts(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Here Are All Aircrafts")
        print("-----------------------")
        print("all aircrafts")
        get_all_destinations = """
        [N]EW 
        [Q]UIT
        [B]ACK
        """
        print(get_all_destinations)
        input_str = input("select action: ").lower()
        return input_str

    def update_aircraft(self):
        return
