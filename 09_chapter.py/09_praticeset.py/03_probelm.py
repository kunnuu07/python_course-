# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old. 

def gn_tabel(n):
    tabel = ""
    for i in range(1,11):
        tabel += (f"{n} X {i} = {n*i}\n")

    with open(f"tables/tabel_{n}.txt","w") as f:
        f.write(tabel)


for i in range(2,21):# n gets its value from the loop
    gn_tabel(i) # <== here, each value of i (2 to 20) is sent as n