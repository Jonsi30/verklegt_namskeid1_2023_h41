from Data_layer.voyaga_data import GetData

class Voyage:
    def __init__(self) -> None:
        self.file = GetData.get_voyage_data()
    