from Logic.logic_destination import Logic_destination
from data.data_wrapper import Data_wrapper
from Logic.voyage_logic import VoyageLogic


class Logic_wrapper:
    def __init__(self):
        self.destinations = Logic_destination()
        self.data_wrapper = Data_wrapper()
        self.voyage_logic = VoyageLogic()

    def all_destinations(self):#Þetta gefur alla destinations listaða
        #Logic.Logic wrapper -> Logic.Logic_destination -> data.Data_wrapper -> data.destination_data
        #Hægt að keyra þetta fyrir utan þessa möppu með þessu formatti:
        '''
        from Logic.logic_wrapper import Logic_wrapper

        dest = Logic_wrapper()

        dest.all_destinations()
        return self.destinations.all_dest()
        '''
    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
