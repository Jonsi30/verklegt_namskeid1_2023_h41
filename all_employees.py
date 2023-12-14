from logic.logic_wrapper import Logic_wrapper
from prettytable import PrettyTable
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
all_employees = Logic_wrapper().get_all_crew()
employee_table = PrettyTable()
fieldnames = FIELDNAMES
employee_table.field_names = (fieldnames)

for employee in all_employees:
    employee_table.add_row([employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn])

print(employee_table)

