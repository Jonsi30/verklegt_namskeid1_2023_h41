from data.data_wrapper import Data_wrapper
from logic.voyage_logic import VoyageLogic


class logic_wrapper:
    def __init__(self):
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic()

    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
