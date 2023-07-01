from tkinter import *
from tkinter import messagebox 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random 
import string

def generate_password():
    entry_password.delete(0,END)  
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    # entry_email_or_username_text.insert(END, "ahmetnarin568@gmail.com")
    entry_password.insert(END ,  password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
# import numpy as np 
# def save(*args):
#     arr = np.array(args)
#     print(arr)
#     with open("passwords.txt" , "w") as file:
#         for i in arr:
#             file.write("{} | ".format(i) )
#         file.write("\n-----------------------------------")

def save():

    website = entry_website_text.get()
    email = entry_email_or_username_text.get()
    password = entry_password.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(title="Sure?" , message=f"Email: {email}\nPassword: {password}\nWould you like to save this password?")

        if is_ok:
            with open("passwords.txt" , "a") as data_file: 
                data_file.write(f"{website} | {email} | {password}")
                data_file.write("\n-----------------------------------------------------------------------------------------\n")
                entry_website_text.delete(0,END)
                entry_email_or_username_text.delete(0,END)
                entry_password.delete(0,END)
    else:
        # messagebox.WARNING("you have to fill all field?")   
        messagebox.askretrycancel(title="Try again?" , message="You have to fill all field?")
        print("I am working")    
        
        

# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME =  "courier"

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(height=200,width=200)

canvas.pack()

# 5 rows and 3 cols 
# logo 
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1 , row = 0)

# Labels
website_label = Label(text="Website", font=(FONT_NAME, 12), justify="left")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", font=(FONT_NAME, 12), justify="left")
email_label.grid(column=0, row=2)
password_label = Label(text="Password", font=(FONT_NAME, 12), justify="left")
password_label.grid(column=0, row=3)

# Entries  
entry_website_text = Entry(window, width=35)
entry_website_text.grid(column=1 , row=1)
entry_email_or_username_text = Entry(window, width=35)
# entry_email_or_username_text.insert(END, "ahmetnarin568@gmail.com")
entry_email_or_username_text.grid(column=1 , row=2 )
entry_password = Entry(window, width=35)
entry_password.grid(column=1 , row=3)




# Buttons 
generate_password_button = Button(text="Generate Password", command=lambda: generate_password(), width=30, highlightthickness=0)
generate_password_button.grid(row=4,column=1)

print(type(entry_website_text))
button_add= Button(text="Add", command=lambda: save(), highlightthickness=0, width=30)
button_add.grid(column=1, row=5)






window.mainloop()