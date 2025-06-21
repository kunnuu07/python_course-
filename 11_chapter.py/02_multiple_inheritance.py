class Employee:  # Parent/Base class
    company = "Google"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_salary(self):
        print(f"The Name Of employee is {self.name} and The salary of employee is {self.salary}")

class intrest:
    def coder(self):
        print(f"Coder Is Inrested IN this Language {self.language}")

class Programmer(Employee,intrest):  # Multiple Inheritance
    company = "GOOGLE COMPANY"
    language = "Python and C Programming"
    
    def show_salary(self):
        print(f"The Name Of employee is {self.name} and The salary of programmer is {self.salary}")
    
    def show_language(self):
        print(f"The Programmer is expert in {self.language}")

# Creating object of Employee
a = Employee("Raj", 50000)
a.show_salary()

# Creating object of Programmer
b = Programmer("Kunal", 70000)
b.show_salary()
b.show_language()
print("")
b.coder()

# Printing some info
print(a.company)
print(b.company)
print(a.salary)
print(b.language)
print("")



