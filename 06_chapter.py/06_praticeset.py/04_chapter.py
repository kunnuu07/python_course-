# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 

user_name = input("Enter Your User Name: ")


if(len(user_name) < 10):
    print("Your Username Less Than 10 Characters \n ")

else:
    print("Your Username Greater Than 10 characters")