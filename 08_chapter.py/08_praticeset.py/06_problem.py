# 6. Write a python function which converts inches to cms.

def inches(inches):
    if(inches==0):
        return 0
    return inches*2.54

n=int(input("Enter a number: "))
print(inches(n))