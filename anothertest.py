from logic.logic_employees import LogicEmployees
from prettytable import PrettyTable
from logic.logic_wrapper import LogicEmployees
from logic.logic_wrapper import LogicDestination
from logic.logic_wrapper import Logic_wrapper
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
"""
test = LogicEmployees().get_by_ssn('1910702559')
for i in test:
    print(i)
"""
"""
pilots = LogicEmployees().get_all_pilots()
            
fieldnames = ["Name", "Role"]
table = PrettyTable()
table.field_names = fieldnames
for employee in pilots:
    name, role = employee
    table.add_row([name, role])
print((table))
"""
from logic.logic_employees import LogicEmployees
available = LogicEmployees().display_available_employees('16.12.2023')
for i in available:
    print(i)
