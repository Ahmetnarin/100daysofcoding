from tkinter import *

def button_clicked():
    user_input = entry.get()
    my_label.config(text=user_input)
    print(user_input)

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height = 300)

# label 
my_label= Label(text="I am a label", font=("Arial", 24 , "bold")) 
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# button 
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# new button 
new_button = Button(text="click new button")
new_button.grid(column=2, row=0)


# Entry 
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)





window.mainloop()