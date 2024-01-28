import random

logo ="""


 _   _                 _                 _____                     _               _____                      
| \ | |               | |               |  __ \                   (_)             |  __ \                     
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                                                            __/ |                             
                                                                           |___/                              

""" 

storedValue = random.randint(1, 101)

#Algorithm when user choses easy mode
def easyGame():
    #Total number of chances ineasy mode
    easyChances = 10

    #While loop runs continuesly as long as user has chances
    while easyChances > 0:
        print(f"You have {easyChances} chances left")
        guess = int(input("Make a guess: "))
        
        if guess == storedValue:
            print("You Gusessed it right")
            break
        elif guess > storedValue:
            easyChances -= 1
            print("Too high\nGuess again")
        else:
            easyChances -= 1
            print("Too low\nGuess again")

    if easyChances == 0:
        print("You've run out of chances")
    else:
        print("You Won")

    return

#Algorithm when user choses hard mode
def hardGame():
    #Total number of chances in hard mode
    hardChances = 5

    #While loop runs continuesly as long as user has chances
    while hardChances > 0:
        print(f"You have {hardChances} chances left")
        guess = int(input("Make a guess: "))
        
        if guess == storedValue:
            print("You Gusessed it right")
            break
        elif guess > storedValue:
            hardChances -= 1
            print("Too high\nGuess again")
        else:
            hardChances -= 1
            print("Too low\nGuess again")

    if hardChances == 0:
        print("You've run out of chances")
    else:
        print("You Won")

    return


#Select the game mode, either easy or hard difficulty
def mode():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    gameMode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if gameMode == "easy":
        easyGame()
    elif gameMode == "hard":
        hardGame()
    else:
        print("Invalid Input")
        mode()
    
    return


mode()