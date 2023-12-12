"""scrap prolly"""


from data.voyage_data import GetData


class Voyage_details:
    def __init__(self) -> None:
        self.file = GetData.get_voyage_data(self)

    def get_flight(self):
        flight_dict = dict()
        lines = self.file.readlines()[1:]
        for line in lines:
            values = line.split(",")
            if len(values) != 6:
                continue
            (
                flight_nr,
                dep_from,
                arr_at,
                departure,
                arrival,
                plane_insignia,
            ) = values
            dep_time, dep_date = departure.split(" ")
            arr_time, arr_date = arrival.split(" ")
            flight_dict[flight_nr] = {
                "Departure From": dep_from,
                "Arrival At": arr_at,
                "Departure Time": dep_time,
                "Departure Date": dep_date,
                "Arrival Time": arr_time,
                "Arrival Date": arr_date,
                "Plane Insignia": plane_insignia,
            }
        return flight_dict

    def get_voyage(self):
        flight_dict = self.get_flight()
        voyage_dict = dict()
        flight_keys = list(flight_dict.keys())
        for i in range(0, len(flight_keys), 2):
            flight1 = flight_dict[flight_keys[i]]
            flight2 = flight_dict[flight_keys[i + 1]]
            voyage_dict[i // 2] = {"flight1": flight1, "flight2": flight2}
        return voyage_dict

    def format_voyage(self):
        voyage_dict = self.get_voyage()
        formatted_voyage = ""
        for key, voyage in voyage_dict.items():
            formatted_voyage += f"Voyage {key + 1}:\n"
            for flight_key, flight_value in voyage.items():
                formatted_voyage += f"{flight_key}: "
                formatted_voyage += ", ".join(
                    f"{item_key}: {item_value}"
                    for item_key, item_value in flight_value.items()
                )
                formatted_voyage += "\n"
            formatted_voyage += "\n"
        return formatted_voyage



captain = """
        captain(fx. John Johnson)"""
        print(captain)
        captain_input = input("->: ").lower

        copilot = """
        copilot(fx. John Mikeson)"""
        print(copilot)
        copilot_input = input("->: ").lower

        head_of_service = """
        head_of_service(fx. Mike Johnson)"""
        print(head_of_service)
        copilot_input = input("->: ").lower

        flight_attendant = """
        flight_attendant(fx. Mike Mikeson)"""
        print(flight_attendant)
        flight_attendant_input = input("->: ").lower


captain_input,
            copilot_input,
            flight_attendant_input,

class ascii:
    def __init__(self):
        pass

    def landing_page(self):
        """Prints the landing page for the user"""
        reset = "\033[0m"
        orange = "\033[38;5;202m"
        landing_ui = f"""{orange}


                                   _
                                __~a~_
                                ~~;  ~_
                  _                ~  ~_                _
                 '_\;__._._._._._._]   ~_._._._._._.__;/_`
                 '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
                 (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
                (/ / / / / | | | ~(/    \) ~ | | \ \ \ \ \)
               (/ / / / /  ~ ~ ~   (/  \)    ~ ~  \ \ \ \ \)
              (/ / / / ~          / (||)|          ~ \ \ \ \)
              ~ / / ~            M  /||\M             ~ \ \ ~
               ~ ~                  /||\                 ~ ~
                                   //||\\
                                   //||\\
                                   //||\\
                                   '/||\'                                                                     
                                                                      
        /|    / /                /|    / /                                
       //|   / /      ___       //|   / /        ___       ( )      __    
      // |  / /     //   ) )   // |  / /       //   ) )   / /     //  ) ) 
     //  | / /     //   / /   //  | / /       //   / /   / /     //       
    //   |/ /     ((___( (   //   |/ /       ((___( (   / /     //        

{reset}
                                Please Login
                        [m] Manager  [d] director

                                or [q] quit
                    """
        return landing_ui