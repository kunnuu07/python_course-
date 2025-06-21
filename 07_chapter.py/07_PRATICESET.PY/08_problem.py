# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n=int(input("Enter A Number: "))

for i in range(0,n):
    print(" "* (n-1),end="")# end="" fuction is tell compiler dont give bydefault new line after print 
    print("*"* (i+1),end="")
    print("")