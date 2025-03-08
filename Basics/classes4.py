class Company:
    company_name = "Google"

    def __init__(self, employee_name):
        self.employee_name = employee_name


emp1 = Company("Alice")
emp2 = Company("Bob")

print(emp1.company_name)
print(emp2.company_name)

Company.company_name = "Microsoft"
print(emp1.company_name)
print(emp2.company_name)