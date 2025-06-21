class Employee:
    a = 1

class programmer(Employee):
    b = 12

class maneger(programmer):
    c = 123

k = Employee() # parent class
print(k.a)

u = programmer() # for 1st Child class
print(u.a,u.b)

n = maneger() # 2nd Child classs
print(n.a , n.b , n.c)