from tkinter import *

root = Tk()
canvas = Canvas(root, width= 400, height = 300)

canvas.pack()

canvas.create_line(x1,y1, x2,y2)