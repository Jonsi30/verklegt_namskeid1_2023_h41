import csv
from model.employee import Employee

FIELDNAMES = [
    "Name",
    "Role",
    "Rank",
    "License",
    "Phone Number",
    "Address",
    "Email Address",
    "Social Security Number",
]


class Employee_data:
    def __init__(self):
        self.file_name = "../verklegt_namskeid1_2023_h41/files/employees.csv"  # filenameið sem inniheldur info um þetta class

    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(
                    Employee(
                        row["Name"],
                        row["Role"],
                        row["Rank"],
                        row["License"],
                        row["Phone Number"],
                        row["Address"],
                        row["Email Address"],
                        row["Social Security Number"],
                    )
                )
        return ret_list

    def create_employee(self, employee: Employee):
        # User can Create Employee
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = FIELDNAMES
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "Name": employee.name,
                    "Role": employee.role,
                    "Rank": employee.rank,
                    "License": employee.license,
                    "Phone Number": employee.phone_nr,
                    "Address": employee.address,
                    "Email Address": employee.email,
                    "Social Security Number": employee.ssn,
                }
            )


    def update_employee(self, updated_employee: Employee):
        all_dest = Employee_data()
        every_employee = all_dest.get_all_employees()
        new_list = []
        for employee in every_employee:
            if employee.ssn == updated_employee.ssn:
                new_list.append(
                    ([
                        employee.name,
                        updated_employee.role,
                        updated_employee.rank,
                        updated_employee.license,
                        updated_employee.phone_nr,
                        updated_employee.address,
                        updated_employee.email,
                        employee.ssn,
                    ])
                )
            else:
                new_list.append(
                    ([
                        employee.name,
                        employee.role,
                        employee.rank,
                        employee.license,
                        employee.phone_nr,
                        employee.address,
                        employee.email,
                        employee.ssn,
                    ])
                )

        f = open(self.file_name, "w")
        f.truncate()
        f.close()

        with open(self.file_name, "w", newline="") as self.file_name:
            fields = FIELDNAMES
            writer = csv.DictWriter(self.file_name, fieldnames=fields)

            writer.writeheader()

        for i, person in enumerate(new_list):
            name, role, rank, license, phone_nr, address, email, ssn = person
            if role == '':
                role = every_employee[i].role
            if rank == '':
                rank = every_employee[i].rank
            if license == '':
                license = every_employee[i].license
            if phone_nr == '':
                phone_nr = every_employee[i].phone_nr
            if address == '':
                address = every_employee[i].address
            if email == '':
                email = every_employee[i].email
                
            Employee_data().create_employee(Employee(name, role, rank, license, phone_nr, address, email, ssn))

   