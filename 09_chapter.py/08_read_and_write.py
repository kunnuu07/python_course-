with open('example.txt', 'r+') as file:
    content = file.read()       # Read existing content
    file.seek(0)                # Go back to the beginning
    file.write('Updated data')  # Overwrite from start
