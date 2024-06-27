from tkinter import *
from tkinter import messagebox
import pyperclip as pi
import random as rd
import string

#global values
ALPHABET = list(string.ascii_letters)   
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHARACTER = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#logic
def create_password():   
    """Creates a unintelligble password from letters, number and symbols and inserts it into the password entry when generate
    button is clicked"""
    nr_letters = rd.randint(8, 10)
    nr_symbols = rd.randint(2, 4)
    nr_numbers = rd.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(rd.choice(ALPHABET))

    for char in range(nr_symbols):
        password_list.append(rd.choice(CHARACTER))

    for char in range(nr_numbers):
        password_list.append(rd.choice(NUMBERS))

    rd.shuffle(password_list)
    password = ''.join(password_list)
    pi.copy(password)
    password_value.insert(0, password)

def search():
    search_key = website_value.get()

    with open('pass.txt', 'r') as file:
        user_information = file.readlines()

    for line in user_information:
        web, email, key = map(str, line.strip().split(' | '))

        if web != search_key:
            raise ValueError(messagebox.showerror(message='This website does not exist'))
        else:
            messagebox.showinfo(title='Result', message=f'Website: {web}\nEmail: {email}\nPassword: {key}')
            break
    

def submit_form():    
    user_web = website_value.get()
    user_email = email_value.get()
    user_password = password_value.get()

    field_value_count = [len(user_web), len(user_email), len(user_password)]
    if 0 in field_value_count:
        messagebox.showinfo(title='Error', message='Do not leave any fields empty')
        field_value_count = []
    else:
        confirmation = messagebox.askokcancel(title="website", message="do you want to proceed")

        if confirmation:
            with open("pass.txt", "a") as file:
                file.write(f"{user_web} | {user_email} | {user_password}\n")
                website_value.delete(0, END)
                password_value.delete(0, END)

#UI
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=20)

#labels
website_label = Label(text="Website:", font=("Times New Roman", 10, "bold"))
email_label = Label(text="Email/Username:", font=("Times New Roman", 10, "bold"))
password_label = Label(text="Password:", font=("Times New Roman", 10, "bold"))
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#entry
website_value = Entry(width=21)
website_value.focus()
email_value = Entry(width=40)
email_value.insert(0, '21f26.levin@sjec.ac.in')
password_value = Entry(width=21)

search = Button(text='Search', width=12, command=search)
generate_value = Button(text="Generate", width=12, command=create_password)

website_value.grid(row=1, column=1)
email_value.grid(row=2, column=1, columnspan=2)
password_value.grid(row=3, column=1)
search.grid(row=1, column=2)
generate_value.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=submit_form)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=224, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 112, image=lock_img)
canvas.grid(row=0, column=1)

root.mainloop()