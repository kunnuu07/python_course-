# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 
import random
def game():
    print("Your Playing a Game....")
    score = random.randint(1,100)
    # fetch the score

    with open("highscore.txt") as f:
        highscore = f.read() # when we use read that means it is a string NOT a int
        if(highscore != ""):# if something is writen in file then
            highscore = int(highscore) # convert it str to int because we need compare in below steps
        else:
            highscore = 0

    print(f"your score: {score}")
    # write the highscre in the file

    if(score>highscore):
        with open("highscore.txt","w") as f1:
            f1.write(str(score))
    return score

game()


