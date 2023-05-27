from tkinter import *



window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height = 50)

# Entry 
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

# label 
my_label= Label(text="Miles", font=("Arial", 12 , "bold")) 
my_label.grid(column=2, row=0)

second_label= Label(text="is equals to", font=("Arial", 12 , "bold")) 
second_label.grid(column=0, row=1)

third_label= Label(text="km", font=("Arial", 12 , "bold")) 
third_label.grid(column=2, row=1)

result_label= Label(window, font=("Arial", 12 , "bold")) 
result_label.grid(column=1, row=1)


def convert_miles_to_km():
    user_input = input.get()
    km = round(1.6*int(user_input),1)
    result_label.config(text=str(km))


# button 
calc_button = Button(text="convert", command=convert_miles_to_km)
calc_button.grid(column=1, row=2)










window.mainloop()