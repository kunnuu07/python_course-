'''
number gussing game 
'''
import random

computer = random.randint(1,20)
attempt = 0
max_attempt=computer

print("This Is a Number Gussing Name !! \n You have 5 attempt to Guess The Correct Number")

while(attempt<max_attempt):
    guess = int(input("Enter Your Guess: "))
    print(guess)
    attempt += 1

    if(guess == computer):
        print(f"Conrats You Win!!! \n You Win In {attempt} Guesses")
        break
    elif(guess < computer):
        print("Higher Number Plz!!")
    else:
        print("Lower Number Plz!!!")
if(guess!= computer):
    print(f"Sorry You Lost! The Correct Number is {computer}")
