# 4. Add a static method in problem 2, to greet the user with hello.

class claculator:
    def __init__(self,n):
        self.n=n

    @staticmethod
    def greet():
        print("hello Dear!!\n")

    def squre(self):
        print(f"The square Of {self.n} Is {self.n*self.n}")

    def cube(self):
        print(f"The Cube of {self.n} Is {self.n*self.n*self.n}")

    def squreroot(self):
        print(f"The Squreroot of {self.n} Is {self.n**1/2}")

a = claculator(4)
a.greet()
a.squre()
a.cube()
a.squreroot()
