# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class programmer():
    company = "Microsoft"
    def __init__(self , name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary

a = programmer("Kunal",25,"90k")
print(f"Programmer Name:{a.name}.\n Salary: {a.salary} \n Age Of Programmer: {a.age} \n Working In: {a.company}\n\n")

a = programmer("Ram",26,"96k")
print(f"Programmer Name:{a.name}.\n Salary: {a.salary} \n Age Of Programmer: {a.age} \n Working In: {a.company}\n\n")

a = programmer("Anushka",25,"89k")
print(f"Programmer Name:{a.name}.\n Salary: {a.salary} \n Age Of Programmer: {a.age} \n Working In: {a.company}\n\n")

a = programmer("Shyam",16,"1.9L")
print(f"Programmer Name:{a.name}.\n Salary: {a.salary} \n Age Of Programmer: {a.age} \n Working In: {a.company}\n\n")

a = programmer("Radha",16,"2L")
print(f"Programmer Name:{a.name}.\n Salary: {a.salary} \n Age Of Programmer: {a.age} \n Working In: {a.company}\n\n")


        