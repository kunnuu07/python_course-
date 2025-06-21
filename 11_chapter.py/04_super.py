class Employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1

class programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 12

class maneger(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Maneger")
    c = 123

# k = Employee() # parent class
# print(k.a)

# u = programmer() # for 1st Child class
# print(u.a,u.b)

n = maneger() # 2nd Child classs
print(n.a , n.b , n.c)