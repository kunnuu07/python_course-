# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return "A is Higher number",a
    elif(b>a and b>c):
        return "b is Higher number",b
    elif(c>b and c>a):
        return "c is Higher number",c
    
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))

print(greatest(a,b,c))