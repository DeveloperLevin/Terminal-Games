from tkinter import *
import pandas as pd
import random as rd

#global values
OLIVE = "#B1DDC6"

#logic
#data from csv
data = pd.read_csv('data/french_words.csv')
new_data = data.to_dict(orient='records')

known_words = []

#functions
def draw_card():
    card = rd.choice(new_data)
    return card


def next_card(card):
    """Picks a  random card from the dictionary and chages the card every 3s"""
    canvas.itemconfig(card_page, image=back_page)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=card['French'])

    root.after(3000, flipCard, card)

def flipCard(card):
    """function to flip the card"""
    canvas.itemconfig(card_page, image=front_page)
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(word, text=card['English'])

def learntCard():
    """draws card and if the user has learnt it already the card is drawn again"""
    card = draw_card()

    while ( card in known_words ):
        card = draw_card()

    if (card not in known_words):
        known_words.append(card)
        next_card(card)
        
def notLearntCard():
    card = draw_card()

    while ( card in known_words ):
        card = draw_card()

    next_card(card)


# UI
root = Tk()
root.title('Flash Card App')
root.config(padx=50, pady=50, bg=OLIVE)

canvas = Canvas(width=800, height=526, bg=OLIVE, highlightthickness=0)
front_page = PhotoImage(file='images/card_front.png')
back_page = PhotoImage(file='images/card_back.png')
correct = PhotoImage(file='images/right.png') 
wrong = PhotoImage(file='images/wrong.png')

card_page = canvas.create_image(400, 236, image=back_page)
language = canvas.create_text(400, 100, text='', font=("Ariel", 40, 'italic'))
word = canvas.create_text(400, 220, text='', font=("Ariel", 60, "bold"))

correct_button = Button(image=correct, highlightthickness=0, command=learntCard)
wrong_button = Button(image=wrong, highlightthickness=0, command=notLearntCard)

notLearntCard()

canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

root.mainloop()
