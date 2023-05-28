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
reps = 0 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text= "00:00")
    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
import datetime 

def start_timer():
    global reps
    work_sec = 1 * 60
    short_break_sec =  1 * 60
    long_break_sec = 1 * 60

    reps += 1
    if reps % 2 != 0:
        countdown(work_sec)
        # print("reps % 2 != 0--> ", reps)
        timer_label.config(text="WORK" ,font=(FONT_NAME, 40 , "bold"), fg=GREEN, bg=YELLOW)
        
    if reps == 8:
        countdown(long_break_sec)
        # print("reps == 8--> ", reps)
        timer_label.config(text="LONG BREAK" ,font=(FONT_NAME, 40 , "bold"), fg=RED, bg=YELLOW)
    if reps % 2 == 0:
        countdown(short_break_sec)
        # print("reps % 2 == 0--> ",reps)
        timer_label.config(text="SHORT BREAK", font=(FONT_NAME, 40 , "bold"), fg=PINK, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time 
import math 

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text="{:02d}:{:02d}".format(count_min,count_sec))
    if count > 0:
        global timer 
        timer = window.after(1000, countdown, count - 1)
        
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)
            
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


    

# Create a button for start 
start_button = Button(text="Start", command=start_timer, highlightthickness=0 )
start_button.grid(column=0, row=3) #, command=pass ) , command=countdown(1)

# Create a button for reset 
reset_button = Button(text="Reset", command=reset_timer,  highlightthickness=0)
reset_button.grid(column=3, row=3) #, command=pass )

# create a check_mark 
check_mark = Label(font=(FONT_NAME, 24 , "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)

window.mainloop()