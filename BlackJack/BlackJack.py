import random as rd
import os

logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
"""

def deal_card():
    """Gives a card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the total score of the card and lets user know if its a blackjack and if it isnt, then whether it has crossed 21 or not"""
    #User has got a BlackJack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #if the sum is over 21 replace any ace cards of value 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)
    
def compare(user_score, computer_score):
    """Checks various conditions for potential win while playing BlackJack"""
    if user_score > 21 and computer_score > 21:
        return "You went over, You lose"
    
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, Opponent has BlackJack"
    elif user_score == 0:
        return "You won with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def game():
    """Starts the game by giving user and computer two cards that are less than 21"""
    user = []
    computer = []
    playable = True

    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while playable:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)

        print(f"The users cards are {user} and your score is {user_score} ")
        print(f"Computer's first card {computer[0]}")

        #If user has won 
        if user_score == 0 or computer_score == 0 or user_score > 21:
            print(compare(user_score, computer_score))
            playable = False
        #let user pick another card or pass
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user.append(deal_card())
                user_score = calculate_score(user)
            else:
                while computer_score != 0 and computer_score < 17:
                    computer.append(deal_card())
                    computer_score = calculate_score(computer)

                print(f"Your final hand: {user}, final score: {user_score}")
                print(f"Computer's final hand: {computer}, final score: {computer_score}")

                print(compare(user_score, computer_score))
                playable = False


while input("Do you want to play BlackJack y/n: ").lower() == 'y':
    os.system('cls')
    print(logo)
    game()