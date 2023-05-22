import tkinter
import turtle

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label 
my_label = tkinter.Label(text="Hello!", font=("Arial", 24 , "bold"))
my_label.pack(side="left")

tim = turtle.Turtle()
tim.write("Some Text", font=("Arial", 20) )
tim.hideturtle()




window.mainloop()