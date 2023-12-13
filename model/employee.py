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
        return f"Name: {self.name}, Role: {self.role}, Rank: {self.rank}, License: {self.license}, Phone Number: {self.phone_nr}, Address: {self.address}, Email: {self.email} Social Security Number: {self.ssn} "
        

