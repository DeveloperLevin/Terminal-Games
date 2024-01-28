from gamedata import data
from art import logo, vs
import os
import random as rd

#Task 1: User input
def select_choice():
    """Asks user for inputs and tackles any undesired inputs"""
    choice = input("Who has more followers? Type 'A' or 'B'\n").lower()

    #check if the choice is valid
    if choice != 'a' and choice != 'b':
        print("Wrong choice !, Choose again")
        os.system('cls')
        select_choice()
    
    return choice


#Task 2: Present user with the 2 statements and a random integer to select a data from the array
def random_data(data):
    """Chooses a random person from the list of people and their followers count"""
    random_number = rd.randint(0, len(data))
    person_info = data[random_number]["name"] + ", a " + data[random_number]["description"] + ", from " + data[random_number]["country"]
    followers = data[random_number]["follower_count"]

    return person_info, followers

#Task 3: Set up the start page
def start(logo, vs):
    """Starts the program and returns the final score"""
    personA, personA_count = random_data(data)
    personB, personB_count = random_data(data)

    #Check if person A and person B are the same 
    if personA == personB:
        personB, personB_count = random_data(data)

    game = False
    score = 0

    #Task 4: Add a scoring system
    while (not game):
        os.system('cls')
        print(logo)

        if score != 0:
            print(f"Your Current Score is: {score}")

        print(f"Compare A: {personA}")
        print(vs)
        print(f"To: {personB}")

        user_choice = select_choice()

        #Task 5: Compare the followers between the two
        if user_choice == 'a' and personA_count > personB_count:
            print("Correct")
            personB, personB_count = random_data(data)
            score += 1
        elif user_choice == 'b' and personB_count > personA_count:
            print("Correct")
            personA, personA_count = random_data(data)
            
            score += 1
        else:
            game = True
            print("You Lose!")
            break

    return score

#Task 6: display final results
final_score = start(logo, vs)
print(f"Your Total score is : {final_score}")





    

