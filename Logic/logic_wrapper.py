from logic.voyage_formatter import VoyageFormatter
from logic.voyage_details import Voyage_details


class logic_wrapper:
    def __init__(self):
        pass

    def get_voyage_data(self):
        voyage = Voyage_details()  # create an instance of Voyage
        voyage_formatter = VoyageFormatter(
            voyage
        )  # pass the Voyage instance to VoyageFormatter
        return voyage_formatter.format_voyage()
