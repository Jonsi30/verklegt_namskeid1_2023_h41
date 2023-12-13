from logic.logic_employees import LogicEmployees
from prettytable import PrettyTable

"""
test = LogicEmployees().get_all_crew()
for i in test:
    print(i)
"""
"""
fieldnames = ["Name", "Role", "Rank", "License", "Phone Number", "Address", "Email Adress", "Social Security Number"]
table = PrettyTable()
table.field_names = fieldnames
for employee in test:
    table.add_row([employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn])
print((table))
"""

"""
test = LogicEmployees().get_employee_info('John Stones')
fieldnames = ["Name", "Role", "Rank", "License", "Phone Number", "Address", "Email Address", "Social Security Number"]
table = PrettyTable()
table.field_names = fieldnames
for employee in test:
    table.add_row([employee.name, employee.role, employee.rank, employee.license, employee.phone_nr, employee.address, employee.email, employee.ssn])
print((table))
"""

test = LogicEmployees().get_by_ssn('1910702559')
for i in test:
    print(i)