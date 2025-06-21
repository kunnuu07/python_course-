# 7. Write a program to find out the line number where python is present from ques 6. 

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if("python" in line):
        print(f"Yes Python is present . Line no: {lineno}")
        break
    lineno += 1 #is your own variable to keep track of which line number you're on.You manually increment lineno using: lineno += 1

else:
    print("No python is not present")