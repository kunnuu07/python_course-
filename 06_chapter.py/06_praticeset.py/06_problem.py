# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

html = int(input("Enter Your HTML marks: "))
c_Programing = int(input("Enter Your C Programing marks: "))
Python = int(input("Enter Your Python marks: "))
java = int(input("Enter Your Java marks: "))

total= (100*(html+c_Programing+Python+java))/400

    
if(html,c_Programing,Python,java<=35):
    if(total>=90):
     print("Exelent Work You Got ",total)
elif(total<=90 and total>= 80):
       print("You Got A Grade ",total)
    
elif(total<=80 and total>= 70):
    print("You Got B Grade ",total)

elif(total<=70 and total>= 60):
    print("You Got C Grade ",total)

elif(total<=60 and total>= 50):
    print("You Got D Grade ",total)

elif(total<=50 and total>= 35):
    print("Improve Your Self ",total)

else:
    print("Your Failed Due To Low Marks")


if(Python<35):
    print(f"You Failed In Python: {Python} \n Better Luck Next Time")
if(c_Programing<35):
    print(f"You Failed In C Programing:{c_Programing} \n Better Luck Next Time")
if(html<35):
    print(f"You Failed In Html: {html} \n Better Luck Next Time")
if(java<35):
    print(f"You Failed In Java: {java} \n Better Luck Next Time")