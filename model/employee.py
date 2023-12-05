class Employee:
    def __init__(self, name="", role="", rank="", license="", phone_nr="", adress="", ssn=""):
        self.name = name
        self.role = role
        self.rank = rank
        self.license = license
        self.phone_nr = phone_nr
        self.adress = adress
        self.ssn = ssn

    def __str__(self):
        return f"name: {self.name} role: {self.role}, rank: {self.role}, license: {self.license}, phone_nr: {self.phone_nr}, adress: {self.adress}, ssn: {self.ssn}"