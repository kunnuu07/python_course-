# 5. Repeat program 4 for a list of such ss to be censored.

words = ["donkey","gandi","bhk","galiya"]

with open("file.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)