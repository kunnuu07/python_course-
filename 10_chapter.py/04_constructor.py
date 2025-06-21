class employee:
    language = "py" 
    salary = 100000 

    def __init__(self , name , language , salary): # when any method star from __ that called as Dunder Method and dunder method which is autometically called
        print(" I am Using Dunder Method")
        self.salary = salary
        self.language = language
        self.name = name

    def getinfo(self):
        print(f"The Language Is {self.language} and salary is {self.salary}")



kunnu = employee("shantanu","java","90k") 
print(kunnu.name, kunnu.language,kunnu.salary)