from logic.logic_destination import Logic_destination
from data.data_wrapper import Data_wrapper
from logic.voyage_logic import VoyageLogic


class Logic_wrapper:
    def __init__(self):
        self.destinations = Logic_destination()
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic()

    def all_destinations(self):
        return self.destinations.all_dest()

    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
