#fuction definition
def avg():
    a=int(input("Enter Number: "))
    b=int(input("Enter Number: "))
    c=int(input("Enter Number: "))
    average = (a+b+c)/3
    print(average)
    return average

a=avg() # Function call
print(a) # a variable stores average value
