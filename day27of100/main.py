from tkinter import *
import turtle

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label 
my_label = Label(text="I am a label!", font=("Arial", 24 , "bold"))
my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Creating a button 

def button_clicked():
    user_input = entry.get()
    my_label.config(text=user_input)
    print(user_input)



entry = Entry(window, width=20)
entry.pack()

button = Button(window, text="Click Me" , command=button_clicked)
button.pack()










window.mainloop()