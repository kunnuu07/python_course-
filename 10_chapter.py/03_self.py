class employee:
    language = "py" #this is class attribute
    salary = 100000 #this is class attribute

    def getinfo(self): # if we using self parameter or not but we need to give this parameter 
        print(f"The Language Is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

kunnu = employee()

kunnu.getinfo() # this convert as employee.getinfo(kunnu)
# employee.getinfo(kunnu)

kunnu.greet()