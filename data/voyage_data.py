FLIGHT_FILE = "../VERKLEGT_NAMSKEID1_2023_H41/Files/flight_list.csv"


class GetData:
    def __init__(self) -> None:
        pass

    def get_voyage_data(self):
        file_name = FLIGHT_FILE
        file = open(file_name, "r")
        return file
