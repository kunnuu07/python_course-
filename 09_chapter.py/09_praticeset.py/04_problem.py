# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

word = "donkey"

with open("file.txt","r") as f:
    content = f.read()

newcontet = content.replace("donkey","######")

with open("file.txt", "w") as f:
    f.write(newcontet)