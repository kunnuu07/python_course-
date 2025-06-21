a = int(input("Enter a Number: "))
b = int(input("Enter second Number: "))

if (b == 0 or a == 0):
    raise ZeroDivisionError("Hey Our Program is not meant to divide Numbers by Zero")
else:
    print(f"The Division a/b is {a/b}")