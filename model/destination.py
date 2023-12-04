class Destination:
    def __init__(self, id="",destination ="",numeric_id =""):
        self.id = id
        self.destination = destination
        self.numeric_id = numeric_id

    def __str__(self):
        return f"id: {self.id}, destination: {self.destination}, numeric id: {self.numeric_id} "