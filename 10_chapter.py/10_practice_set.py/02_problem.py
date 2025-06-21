# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class claculator:
    def __init__(self,n):
        self.n=n

    def squre(self):
        print(f"The square Of {self.n} Is {self.n*self.n}")

    def cube(self):
        print(f"The Cube of {self.n} Is {self.n*self.n*self.n}")

    def squreroot(self):
        print(f"The Squreroot of {self.n} Is {self.n**1/2}")

a = claculator(4)
a.squre()
a.cube()
a.squreroot()
