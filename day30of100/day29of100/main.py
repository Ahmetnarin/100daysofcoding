from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data 
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json" , "w") as data_file:
                # Updating old data with new data
                json.dump(new_data, data_file, indent=4)
        else: 
            # Updating old data with new data 
            data.update(new_data) 
            with open("data.json",  "w") as data_file:
                # Saving updated data 
                json.dump(data, data_file , indent=4)
        finally: 
            website_entry.delete(0,END)
            password_entry.delete(0,END)

def search():

    try:
        # Reading the data from json file 
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            # print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error" , message="Not found a file. Pls make sure if a data file exist")
    else:
        # What is input 
        website = website_entry.get()
        
        if website in data:
            password = data[website]["password"]
            password_entry.delete(0,END)
            password_entry.insert(0,password)
            print(password)
        else: 
            print("Not found")
            website_entry.delete(0,END)
            password_entry.delete(0,END)


def copy():
    password = password_entry.get()
    pyperclip.copy(password)
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ahmetnarin568@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
# search button 
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)
# copy password button 
copy_button = Button(text="Copy Password",width=36, command=copy)
copy_button.grid(row=5, column=1, columnspan=2)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()