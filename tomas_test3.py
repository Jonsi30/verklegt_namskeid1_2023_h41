class VoyageLogic:
    def __init__(self, data_connection):
        self.data_connection = data_connection

    def get_all_voyages(self):
        return ["this is a voyage example", "this is the next example", "3rd", "4th"]
        return self.data_connection.get_all_voyages()
