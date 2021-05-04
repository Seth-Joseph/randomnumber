#Random Number guessing game.
import random
r = random.randint(1,9)
chances = 0
while chances<5:
    guess=int(input("Guess a number "))
    if(guess == r):
        print("Congratulations")
    elif(guess < r):
        print("Your guess is less than 9")
    else:
        print("Your gues is greater than 6")
    chances = chances+1
        

