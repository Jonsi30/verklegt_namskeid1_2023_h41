# import os
from data.data_wrapper import Data_wrapper


class VoyageLogic:
    def __init__(self):
        self.data_wrapper = Data_wrapper()
        self.file = self.data_wrapper.get_voyage_data()

    def get_all_voyages(self):
        return self.file


# os.system("cls" if os.name == "nt" else "clear")
