class Student:
    def __init__(self, name):
        self._name = name  # _name is a "protected" variable

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

# Usage
s = Student("John")
print(s.name)       # Calls the getter method

s.name = "Alice"    # Calls the setter method
print(s.name)

# s.name = ""       # This will raise a ValueError
