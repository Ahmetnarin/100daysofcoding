import tkinter as tk

def retrieve_input():
    user_input = entry.get()
    print("User input:", user_input)

root = tk.Tk()

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Retrieve Input", command=retrieve_input)
button.pack()

root.mainloop()
  