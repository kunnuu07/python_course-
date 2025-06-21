# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

class twoDvector:
    def __init__(self ,k,u):
        self.k = k
        self.u = u

    def show(self):
        print(f"The Vector is {self.k}k  and {self.u}u")

class threeDvector(twoDvector):
    def __init__(self, k, u , n):
        super().__init__(k, u)
        self.n = n
    def show(self):
         print(f"The Vector is {self.k}k  and {self.u}u and {self.n}n")

a = twoDvector(2,3)
a.show()
b = threeDvector(2,3,8)
b.show()