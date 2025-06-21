print("This program checks if the student name is inside the list or not!")

name = input("Enter your name: ")

def check_name_in_file(name):
    with open("database_file.txt", "r") as f:
        students = f.read().splitlines() # using .splitlines() function create a list and now student variable store a list of database_file.txt file inside data
    return name in students

if check_name_in_file(name):
    print("Congrats! You're eligible for the scholarship!!")
else:
    print("Sorry, better luck next time.")
