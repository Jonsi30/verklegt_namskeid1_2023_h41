import os


class destination:
    def __init__(self):
        pass

    def create_new_destination(self):
        os.system("cls" if os.name == "nt" else "clear")
        new_destination = """
        Please Input The Following Details
        ----------------------------------
        destination"""
        print(new_destination)
        dest_input = input("-> ").lower()

        distance = """ 
        
        distance from iceland (km)"""
        print(distance)
        dist_input = input("-> ").lower()

        duration = """
        
        Duration (hrs:minutes)"""
        print(duration)
        dura_input = input("-> ").lower()

        Contact = """
        
        Emergency contact"""
        print(Contact)
        contact_input = input("-> ").lower()

        Number = """
        
        emergency contact phone_nr"""
        print(Number)
        contact_nr_input = input("-> ").lower()

        return dest_input, dist_input, dura_input, contact_input, contact_nr_input

    def get_all_destinations(self):
        # vos.system("cls" if os.name == "nt" else "clear")
        print("Here Are All Destinations")
        print("-----------------------")
        print("all destinations")
        get_all_destinations = """
        [N]EW 
        [Q]UIT
        [B]ACK
        """
        print(get_all_destinations)

        while True:
            from main_UI import main_UI

            command = input("select action: ").lower()
            if command == "n":
                self.create_new_destination
            elif command == "q":
                print("shutting down")
                break
            elif command == "b":
                main_UI().director_menu_input_prompt
