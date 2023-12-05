from logic.voyage_formatter import VoyageFormatter
from logic.voyage_details import Voyage_details
from data.data_wrapper import Data_wrapper
from logic.voyage_logic import VoyageLogic


class logic_wrapper:
    def __init__(self):
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic(self.data_wrapper)
        self.voyage_details = Voyage_details()
        self.voyage_formatter = VoyageFormatter(self.voyage_details)

    def format_voyages(self):
        return self.voyage_details.format_voyage()

    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
