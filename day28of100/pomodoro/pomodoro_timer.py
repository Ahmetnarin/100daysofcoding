import time

# def countdown(minutes):
#     seconds = minutes * 60
#     while seconds > 0:
#         mins, secs = divmod(seconds, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")  # Print the timer on the same line
#         time.sleep(1)
#         seconds -= 1

#     print("Timer completed!")

# countdown(25)



import tkinter as tk
import time

def enable_button():
    button.config(state=tk.NORMAL)

def button_click():
    print("Button clicked!")

# Create a Tkinter window
window = tk.Tk()

# Create a button (initially disabled)
button = tk.Button(window, text="Click Me", command=button_click, state=tk.DISABLED)
button.pack()

# Define the desired waiting time in seconds
waiting_time = 1 * 60  # 25 minutes

# Calculate the end time by adding the waiting time to the current time
end_time = time.time() + waiting_time

# Start a timer to enable the button when the waiting time elapses
window.after(int(waiting_time * 1000), enable_button)

# Start the Tkinter event loop
window.mainloop()

