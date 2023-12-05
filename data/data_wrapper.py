from data.destination_data import Destination_data
from data.voyage_data import GetData

class Data_wrapper:
    def __init__(self):
        self.destination_data = Destination_data()
        self.voyage_data = GetData()

    def get_all_destinations(self):
        return self.destination_data.get_all_destination()
    
    def create_destination(self, new_destination):
        return self.destination_data.create_destination(new_destination)
    
    def get_voyage_data(self):
        return self.voyage_data.get_voyage_data()
