from logic.logic_destination import LogicDestination
from data.data_wrapper import Data_wrapper
from logic.voyage_logic import VoyageLogic
from logic.logic_employees import LogicEmployees

class Logic_wrapper:
    def __init__(self):
        self.destinations = LogicDestination()
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic()
        self.employee_logic = LogicEmployees()

    def all_destinations(self):  # Þetta gefur alla destinations listaða
        # Logic.Logic wrapper -> Logic.Logic_destination -> data.Data_wrapper -> data.destination_data
        # Hægt að keyra þetta fyrir utan þessa möppu með þessu formatti:
        """
        from Logic.logic_wrapper import Logic_wrapper

        dest = Logic_wrapper()

        dest.all_destinations()
        return self.destinations.all_dest()
        """

    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
