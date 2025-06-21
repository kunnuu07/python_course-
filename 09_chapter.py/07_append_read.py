with open('file.txt', 'a+') as file:
    file.write('\nAppended line')
    file.seek(0)               # Move to the beginning for reading
    print(file.read())
