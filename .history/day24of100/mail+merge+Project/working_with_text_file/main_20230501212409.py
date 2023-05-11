import os 

# Read the template file
with open('starting_letter.txt' , 'r') as f:
    template = f.read()

# Read the list of names 
with open("invite_names.txt" , "r") as f:
    names = f.read().splitlines()

# Create the "Readytosend" folder if does not already exist 
if not os.path.exists("Readytosend"):
    os.makedirs()