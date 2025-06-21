def fun():
    class Employee:
        a = 1

        @classmethod
        def show(cls):
            result = f"The class attribute of a Is {cls.a}"
            print(result)
            return result

        @property
        def name(self):
            return self.ename
        @name.setter
        def name(self,value):
            self.fname = value.split(" ")[0]
            self.lname = value.split(" ")[1]

    k = Employee()
    k.a=4
    k.ename = "kunal dada"
    print(k.ename)
    k.show()

info = fun()

