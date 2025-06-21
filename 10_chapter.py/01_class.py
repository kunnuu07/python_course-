class employee:
    language = "py" #this is class attribute
    salary = 100000 #this is class attribute

anuu = employee()
anuu.name="kunal" #this is Instance attribute
print(anuu.name,anuu.language,anuu.salary)

rohan = employee()
rohan.name="mannu" #this is Instance attribute
print(rohan.name,rohan.language,rohan.salary)

# here name is Instance (object) attribute and
# salary and language are class attrinute as they directly belongs to they class 