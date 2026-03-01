class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Manager(Employee):
    def calculate_salary(self):
        bonus = 5000
        return self.base_salary + bonus

class Developer(Employee):
    def calculate_salary(self):
        bonus = 3000
        return self.base_salary + bonus

class Intern(Employee):
    def calculate_salary(self):
        deduction = 2000   
        return self.base_salary - deduction

manager = Manager("Rahul", 50000)
developer = Developer("Anita", 40000)
intern = Intern("Kiran", 20000)

employees = [manager, developer, intern]

for emp in employees:
    print("Employee Name:", emp.name)
    print("Base Salary:", emp.base_salary)
    print("Final Salary:", emp.calculate_salary())
    print()