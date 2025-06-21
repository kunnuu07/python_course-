f = open("file.txt")


# line1= f.readline()
# print(line1,type(line1))

# line2= f.readline()
# print(line2,type(line2))

# line3= f.readline()
# print(line3,type(line3))

# line4= f.readline()
# print(line4,type(line4))

# line5= f.readline()
# print(line5,type(line5 == ""))

# using loop we can print the line of the file
line = f.readline()
while(line != ""): # we use empty string because readline function readline on that while whenever "" is not find.
    print(line)
    line = f.readline()


f.close()