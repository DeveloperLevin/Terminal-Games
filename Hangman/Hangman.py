from time import sleep
import random
import os
from art import hangman, game_over, congrats, stages
#make changes to clear logss in terminal
#make changes to no not have stages after game won or game over

#List of random words
words = ['apple','banana','orange','pineapple','peach','pear','pomegranate','dragonfruit','grapes','watermelon']
print(hangman)

#chances
chance = 6

#choose a random word from the list prior
chosen_word = list(random.choice(words))

#create a list with underscores
hidden_word = ['_' for _ in range(len(chosen_word))]
print(f"{' '.join(hidden_word)}")

endOfGame = False

#Asks users to input values to check in the list
#while user has life remaining and there are blank spaces present in the hidden word keep executing the loop 
while not endOfGame:
    guess = input("Enter a guess: ")

    #checks if the user has entered the same input and return with a retry
    if guess in hidden_word:
        print("You've already guessed this, try something new")

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            hidden_word[pos] = guess
#if the value entered by the user is not matching the chosen word it deducts the players life
# and if the player life were to be zero then the endofgame state is set to true         
    print(f"{' '.join(hidden_word)}")

    
    if guess not in chosen_word:
        chance -= 1
        print(f"{guess} is not in the word , you lose a life. Lives remaining {chance}")
        if chance == 0:
            endOfGame = True
            print(game_over)

    print(stages[chance])
    sleep(1)
    os.system('clear')

#if there are no more blank spaces in the list it automatically means the player has won
    if "_" not in hidden_word:
        endOfGame = True
        print(congrats)

    

