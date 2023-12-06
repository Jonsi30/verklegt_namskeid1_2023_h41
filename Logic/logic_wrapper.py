from logic.voyage_formatter import VoyageFormatter
from logic.voyage_details import Voyage_details
from Logic.logic_destination import Logic_destination
from data.data_wrapper import Data_wrapper

class Logic_wrapper:
    def __init__(self):
        self.destinations = Logic_destination()
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = Voyagelogic()
        
    def all_destinations(self):
        return self.destinations.all_dest()

    def get_voyage_data(self):
        # puts the voyage details into voyage formatter
        voyage = Voyage_details()  # create an instance of Voyage
        voyage_formatter = VoyageFormatter(
            voyage
        )  # pass the Voyage instance to VoyageFormatter
        return voyage_formatter.format_voyage()
    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
     
    def format_voyage(self):
        return self.voyage_logic.format_voyage()
