import random

def guessing_game():

    secret_number = random.randint(1, 100)
    
    attempts = 0 
    
    while True:
        user_guess = int(input("Guess the number: "))
        attempts += 1 
        
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break 
        elif user_guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

guessing_game()
