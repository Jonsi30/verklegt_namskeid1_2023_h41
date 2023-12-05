from logic.voyage_formatter import VoyageFormatter
from model.voyage_details


class logic_wrapper:
    def __init__(self):
        pass

    def get_voyage_data(self):
        voyage = Voyage_model()  # create an instance of Voyage
        voyage_formatter = VoyageFormatter(
            voyage
        )  # pass the Voyage instance to VoyageFormatter
        return voyage_formatter.format_voyage()
