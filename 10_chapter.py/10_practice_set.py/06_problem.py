# 6. Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects. 

class programmer():
    company = "Microsoft"
    def __init__(slf , name , age , salary):
        print(f"Hello {name} sir !! \n")
        slf.name = name
        slf.age = age
        slf.salary = salary

a = programmer("Kunal",25,"90k")
print(f"Programmer Name:{a.name}.\n Salary: {a.salary} \n Age Of Programmer: {a.age} \n Working In: {a.company}\n\n")