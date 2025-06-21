# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enter a Number: "))

for i in range(2,n):
    if(n%i)==0:
        print("Number Is not Prime")
        break

else:
    print("Number Is Prime")