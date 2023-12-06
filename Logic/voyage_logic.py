from data.data_wrapper import Data_wrapper


class VoyageLogic:
    def __init__(self):
        self.file = Data_wrapper.get_voyage_data(self)

    def get_all_voyages(self):
        flight_dict = dict()
        return flight_dict
