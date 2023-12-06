from logic.logic_wrapper import Logic_wrapper
from data.data_wrapper import Data_wrapper

class UIWrapper:
    def __init__(self) -> None:
        self.Logic_wrapper = Logic_wrapper()
        self.data_wrapper = Data_wrapper()
        