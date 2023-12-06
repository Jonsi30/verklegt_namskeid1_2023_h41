#from Logic.voyage_formatter import VoyageFormatter
#from Logic.voyage_details import Voyage_details
from Logic.logic_destination import Logic_destination

class Logic_wrapper:
    def __init__(self):
        self.destinations = Logic_destination()
        
    """
    def get_voyage_data(self):
        # puts the voyage details into voyage formatter
        voyage = Voyage_details()  # create an instance of Voyage
        voyage_formatter = VoyageFormatter(
            voyage
        )  # pass the Voyage instance to VoyageFormatter
        return voyage_formatter.format_voyage()
    """
    def all_destinations(self):
        return self.destinations.all_dest()

