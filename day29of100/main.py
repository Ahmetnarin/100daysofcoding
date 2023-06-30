from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def add_new_passwort(self):
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

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
entry_email_or_username_text.grid(column=1 , row=2 )
entry_password_or_username_text = Entry(window, width=35)
entry_password_or_username_text.grid(column=1 , row=3)





generate_password_button = Button(text="Generate Password", width=30)
generate_password_button.grid(row=4,column=1)

button_add= Button(text="Add", command=add_new_passwort, highlightthickness=0, width=30)
button_add.grid(column=1, row=5)





window.mainloop()