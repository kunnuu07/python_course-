class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): #for Addition
        return self.n + num.n
    
    def __sub__(self, num): # For Substraction
        return self.n - num.n
    
    def __mul__(self , num ): # for Multiplication
        return self.n * num.n
    
    def __truediv__(self,num): # for division
        return self.n / num.n
    
    def __floordiv__(self , num): # it same as division but give output in integer
        return self.n // num.n
    
    def __str__(self): 
         return f"string representation {self.n}\n"
    
    def __len__(self):
        return len(str(self.n))

n = number(10)
m = number(10)

print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)
print(n)
