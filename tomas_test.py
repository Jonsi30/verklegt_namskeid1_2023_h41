from model.voyage_model import Voyage_model


class VoyageFormatter:
    def __init__(self, voyage):
        self.voyage = voyage
        self.get_voyage = self.voyage.get_voyage()

    def format_voyage(self):
        voyage_dict = self.get_voyage
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


voyage = Voyage_model()  # create an instance of Voyage
voyage_formatter = VoyageFormatter(
    voyage
)  # pass the Voyage instance to VoyageFormatter
print(voyage_formatter.format_voyage())
