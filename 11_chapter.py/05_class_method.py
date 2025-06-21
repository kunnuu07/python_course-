class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a Is {cls.a}")

k = Employee()
k.a=4
k.show()