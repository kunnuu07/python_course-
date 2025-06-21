# this code will delet old data and after that add new data

with open('example.txt', 'w+') as file:
    file.write('New content')  # File is cleared before writing
    file.seek(0)
    print(file.read())         # Read what was written
