# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

n=int(input("Enter A Number: "))

for i in range(1,n+1):
    print(" "* (n-1),end="")# end="" fuction is tell compiler dont give bydefault new line after print 
    print("*"* (2*i-1),end="") # (2*i-1) this formula used t print odd numbers like 
    print("")

    # Explanation of this formula (2*i-1)
    # when i=1 the evaluated like 2*1=2-1=1 then print  one (*)
    # when i=2 the evaluated like 2*2=4-1=3 then print  three (*)
    # when i=3 the evaluated like 2*3=6-1=5 then print  five (*)
    # this process will repeate untile condition become false