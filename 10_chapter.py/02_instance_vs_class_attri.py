class employee:
    language = "py" #this is class attribute
    salary = 100000 #this is class attribute

anuu = employee()
# Note: Instance attributes, take preference over class attributes during assignment & retrieval. >>>>>
anuu.language="java" #this is Instance attribute 
print(anuu.language,anuu.salary)

k=employee()
print(k.language)