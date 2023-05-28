from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def stat_timer():
    countdown(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time 

def countdown(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)
    elif count == 0:
        window.after(enable_button)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas( width= 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(103,130, text= "00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

# countdown(50)


# Create a label for Timer 
timer_label = Label(text="Timer", font=(FONT_NAME, 40 , "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

def reset_timer():
    pass 

def period():
    pass 

# Create a button for start 
start_button = Button(text="Start", command=stat_timer, highlightthickness=0 ).grid(column=0, row=3) #, command=pass ) , command=countdown(1)

# Create a button for reset 
reset_button = Button(text="Reset", command=reset_timer,  highlightthickness=0).grid(column=3, row=3) #, command=pass )

# create a check_mark 
check_mark = Label(text="✔", font=(FONT_NAME, 24 , "bold"), fg=GREEN, bg=YELLOW).grid(column=1, row=4)

window.mainloop()