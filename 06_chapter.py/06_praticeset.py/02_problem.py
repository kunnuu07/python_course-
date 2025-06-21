# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

a= int(input("Enter your Python Marks: "))
b= int(input("Enter your C Programing Marks: "))
c= int(input("Enter your Html Marks: "))

# check fo total Marks
total_percentage = (100*(a+b+c))/300

if(total_percentage>=40 and a >33 and b > 33 and c > 33):
    print("Your are Passed: ",total_percentage)

else:
    print("Your Failed, Try Next Year!\n You Got: ",total_percentage)

if(a<33):
    print("You Failed In Python: ",a)
elif(b<33):
    print("You Failed In C Programing: ",b)
elif(c<33):
    print("You Failed In Html: ",c)