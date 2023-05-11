import os 

# Read the template file
with open('day24of100\mail+merge+Project\working_with_text_file\starting_letter.txt' , 'r') as f:
    template = f.read()

# Read the list of names 
with open("invite_names.txt" , "r") as f:
    names = f.read().splitlines()

# Create the "Readytosend" folder if does not already exist 
if not os.path.exists("Readytosend"):
    os.makedirs("Readytsend")

# Loop through the names and generate a letter for each one 
for name in names:
    # Replace the [name] placeholder with the actual name
    letter = template.replace("[name]", name)

    # Write the personalized letter to a new file in the "Readytosend" folder
    with open(f'Readytosend/Letter_to_{name.replace(" ", "_").lower()}.txt', "w") as f:
        f.write(letter)    





#  # Write the personalized letter to a new file in the "Readytosend" folder
#     with open(f'Readytosend/letter_to_{name.replace(" ", "_").lower()}.txt', 'w') as f:
#         f.write(letter)

