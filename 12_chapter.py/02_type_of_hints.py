# Variable type hint 
age: int = 25 
# Function type hints 

name = input("Enter Your Name: ")
def greeting(name: str) -> str: 
    return f"Hello, {name}!" 
# Usage 
print(greeting(name))  # Output: Hello, Alice! 