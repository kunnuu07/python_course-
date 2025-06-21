import random
n = random.randint(1,100)
u = None
guesses = 0
while(u != n):
    guesses += 1
    u = int(input("GUess The Number:  "))
    if(u > n ):
        print("Lower Number PLease!!!")
    else:
        print("Higher Number PLease!!!")
    
print(f"You Guessed The Corect Number {n} in {guesses} Attempt")

    