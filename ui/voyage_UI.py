from logic.logic_wrapper import Logic_wrapper


class voyage:
    def __init__(self):
        self.get_voyages = Logic_wrapper()

    def create_new_voyage(self):
        return

    def get_all_voyages(self):
        flight_dict = self.get_all_voyages()
        voyage_dict = dict()
        flight_keys = list(flight_dict.keys())
        for i in range(0, len(flight_keys), 2):
            flight1 = flight_dict[flight_keys[i]]
            flight2 = flight_dict[flight_keys[i + 1]]
            voyage_dict[i // 2] = {"flight1": flight1, "flight2": flight2}

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

    def get_specific_day_voyages(self):
        return

    def update_voyage(self):
        return
