import tkinter as tk

def start_timer():
    button.config(state=tk.DISABLED)  # Disable the button
    # Your timer logic here

def enable_button():
    button.config(state=tk.NORMAL)  # Enable the button

# Create a Tkinter window
window = tk.Tk()

# Create a button to start the timer
button = tk.Button(window, text="Start Timer", command=start_timer)
button.pack()

# Start the Tkinter event loop
window.mainloop()
