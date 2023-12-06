class Aircraft_Model:
    def __init__(self,plane_insignia ="",plane_type_id ="",manufacturer ="",seat_capacity =""):
        self.plane_insignia = plane_insignia
        self.plane_type_id = plane_type_id
        self.manufacturer = manufacturer
        self.seat_capacity = seat_capacity

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return f"plane_insignia: {self.plane_insignia}, plane_type_id: {self.plane_type_id}, manufacturer: {self.manufacturer}, seat_capacity:{self.seat_capacity}"
    