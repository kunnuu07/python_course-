# Write a program to find the greatest of four numbers entered by the user. 

a1=int(input("Enter number 1: "))
a2=int(input("Enter number 2: "))
a3=int(input("Enter number 3: "))
a4=int(input("Enter number 4: "))

if(a1>a2 and a1 >a3 and a1 > a4):
    print("a1 Is Greater Number a1: ",a1)

elif(a2>a1 and a2 >a3 and a2 > a4):
    print("a1 Is Greater Number a2: ",a2)

elif(a3>a2 and a3 >a1 and a3 > a4):
    print("a1 Is Greater Number a3: ",a3)

else:
    print(f"A4 Is Greatest Number a4: ",a4)