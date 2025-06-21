a=int(input("Enter Your marks: "))
if(a>=35):
    if(a>=90 or a == 90):
        print("You Got A grade ")

elif( a==89 or a>=80):
    print("You Got B Grade")

elif(a<=80 or a>=70):
    print("You Got C Grade")

elif(a>=60 or a<=70):
    print("You Got D Grade")

else:
    print("You Got E Grade")

if(a<35):
    print("Your Fail")


