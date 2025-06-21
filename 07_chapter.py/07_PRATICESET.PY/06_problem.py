# import math
# print(math.factorial(4))

# 6. Write a program to calculate the factorial of a given number using for loop

n=int(input("Enter A Number: "))
product=1
for i in range(1,n+1):#we use n+1 because they work as i<=n , 
    product *= i
    
print(f"The Factorial Of {n} is {product}")
