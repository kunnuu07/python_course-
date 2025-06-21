# 5. Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them. 

class vector:
    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self , other):
        result = vector(self.x + other.x , self.y + other.y , self.z + other.z)
        return result
    
    def __mul__(self ,other):
        result = self.x * other.x , self.y * other.y , self.z * other.z
        return result
    
    def __str__(self):
        return f"vector ({self.x} , {self.y} , {self.z})"
    
v1 = vector(1,3,2)
v2 = vector(8,7,9)

print(v1 + v2)
print("vector ",v1 * v2)