# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class animals:
    pass

class Pets(animals):
    pass

class dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!!")

a = dog()
a.bark()