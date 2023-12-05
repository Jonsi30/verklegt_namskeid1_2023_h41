EMPLOYEE_FILE = "../Files/flight_list.csv"


class GetData:
    def __init__(self) -> None:
        pass

    def get_voyage_data():
        # file_name = EMPLOYEE_FILE
        file = open(EMPLOYEE_FILE, "r")
        return file


print(GetData.get_voyage_data())
