# 8. Write a python function to print multiplication table of a given number.
def tabel(n):
    t=n*10
    for i in range(n,t+1,n):
        print(i)
    return "done"

n=int(input("Enter a number: "))  
print(tabel(n))

