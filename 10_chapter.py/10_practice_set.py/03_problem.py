# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 

# answer >> Class attribute does not change because in the absence of instance attribute class attribute is bydefault prints

class demo:
    a=4

o = demo()
print(o.a) # Prints the class attribute because instance attribute is not present

o.a = 0 # Instance attribute is set
print(o.a) # Prints the Instance attribute because instance attribute is present

print(demo.a) # prints the class attribute