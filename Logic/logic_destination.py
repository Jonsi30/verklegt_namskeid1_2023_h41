from data.data_wrapper import Data_wrapper

class Logic_destination:
    def __init__(self) -> None:
        self.name = Data_wrapper()

    def all_dest(self):
        all_destinations = self.name.get_all_destinations()

        for i in all_destinations:
            print(i)