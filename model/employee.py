class Employee:
    def __init__(self, name ="", role ="", rank ="", license ="", phone_nr ="", address ="", email ="", ssn =""):
        self.name = name
        self.role = role
        self.rank = rank
        self.license = license
        self.phone_nr = phone_nr
        self.address = address
        self.email = email
        self.ssn = ssn

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return f"name: {self.name}, role: {self.role}, rank: {self.rank}, license: {self.license}, phone nr: {self.phone_nr}, address: {self.address}, email: {self.email} ssn: {self.ssn} "
        

