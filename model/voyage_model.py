class Voyage_Model:
    def __init__(self, id="",flight_nr="",dep_from="",arr_at="",dep_time="",arr_time="", dep_time_back="", arr_time_back="", plane_insignia="",captain="",copilot="",head_of_service="",flight_attendant=""):
        self.id = id
        self.flight_nr = flight_nr
        self.dep_from = dep_from
        self.arr_at = arr_at
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.dep_time_back = dep_time_back
        self.arr_time_back = arr_time_back
        self.plane_insignia = plane_insignia
        self.captain = captain
        self.copilot = copilot
        self.head_of_service = head_of_service
        self.flight_attendant = flight_attendant


    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return f"Voyage: Id {self.id}, Flight number:{self.flight_nr}, Departing:{self.dep_from}, Arrival:{self.arr_at}, Departure time: {self.dep_time}, Arrival time: {self.arr_time}, Departure time back: {self.dep_time_back}, Arrival time back: {self.arr_time_back}, Plane insignia:{self.plane_insignia}, Captain:{self.captain}, Copilot:{self.copilot}, Head of service:{self.head_of_service}, Flight attendant:{self.flight_attendant}"
    

