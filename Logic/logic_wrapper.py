from logic.voyage_formatter import VoyageFormatter

from data.data_wrapper import Data_wrapper
from logic.voyage_logic import VoyageLogic


class logic_wrapper:
    def __init__(self):
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic(self.data_wrapper)

    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
