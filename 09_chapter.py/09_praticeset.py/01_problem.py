# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

f= open("poem.txt")
content = f.read()

if("twinkle" in content ):
        print("The word twinkle is present in the file")
else:
     print("The word twinkle is not present in the file")

f.close()