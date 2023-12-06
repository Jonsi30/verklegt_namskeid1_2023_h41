class Destination:
    def __init__(self,destination ="",distance_from_ice ="",flight_time ="",emergency_contact ="",emergency_contact_phone_nr =""):
        self.destination = destination
        self.distance_from_ice = distance_from_ice
        self.flight_time = flight_time
        self.emergency_contact = emergency_contact
        self.emergency_contact_phone_nr = emergency_contact_phone_nr

    def __str__(self):
        return f"destination: {self.destination}, distance from Iceland(km): {self.distance_from_ice}, flight time: {self.flight_time}, emergency contact: {self.emergency_contact},{self.emergency_contact_phone_nr}"