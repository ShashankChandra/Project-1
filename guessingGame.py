from random import random


number = (int)(random()*10)+1
answer = "Yes"
while answer == "Yes":
    chances = 5
    while chances > 0:
        guess = int(input("What number would you like to guess?"))
        if(guess > number):
            print("Number is too big")
            chances=chances-1
        elif(guess < number):
            print("Number is too small")
            chances=chances-1
        else:
            print("You guessed correctly, you win!")
            break
        if(chances==0):
            print("You guessed incorrectly, the number is: ", number)
    answer = input("Would you like to play again? (Yes/No)")



