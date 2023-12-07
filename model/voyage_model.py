class Voyage_Model:
    def __init__(self, id="",fligh_nr="",dep_from="",arr_at="",departure="",arrival="",plane_insignia="",captain="",copilot="",head_of_service="",flight_attendant=""):
        self.id = id
        self.fligh_nr = fligh_nr
        self.dep_from = dep_from
        self.arr_at = arr_at
        self.departure = departure
        self.arrival = arrival
        self.plane_insignia = plane_insignia
        self.captain = captain
        self.copilot = copilot
        self.head_of_service = head_of_service
        self.flight_attendant = flight_attendant


    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return f"Voyage: Id{self.id},Fligh number:{self.fligh_nr},Departing:{self.dep_from},Arrival:{self.arr_at},Departure time:{self.departure},Arrival time:{self.arrival},Plane insignia:{self.plane_insignia},Captain:{self.captain},Copilot:{self.copilot},Head of service:{self.head_of_service},Flight attendant:{self.flight_attendant}"
    

