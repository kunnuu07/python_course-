mark= {
    ("kunal", 19):99,
    ("kanha",12):98
}
name=input("Ener your Name: ")
roll=int(input("Ener your roll Number: "))
mark.update({'anu':89})
print(mark[name,roll])
print(mark.items())