'''
Created on Sep 8, 2015

@author: meglena
'''
import random


def main():


    secretNumber = random.randint(1, 10)  # Integer from 1 to 10, end points included
    
    guess = 0
    numberOfTries = 0
    win = None
    
    while (win != True) and (numberOfTries < 3):
        guess = input("Enter a guess (1-10): ")
        numberOfTries = numberOfTries + 1
        if guess == str(secretNumber):
            print("Your guess is correct. Congratulations!")
            win = True 
        elif numberOfTries > 2:   
            print("GAME OVER! The correct number was: " + str(secretNumber) + ".")
        elif guess < str(secretNumber):
            print("Your guess is smaller than the secret number.")
        else: 
            print("Your guess is greater than the secret number.")
    
   

main()