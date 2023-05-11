import os 

starting_letter =  'C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day24of100//mail+merge+Project//working_with_text_file//starting_letter.txt'
invite_names = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day24of100//mail+merge+Project//working_with_text_file//invite_names.txt"
# ready_to_send = f'C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day24of100//mail+merge+Project//working_with_text_file//Readytosend/Letter_to_{name.replace(" ", "_").lower()}.txt'

# Read the template file
with open( starting_letter , 'r') as f:
    template = f.read()

# Read the list of names 
with open(invite_names , "r") as f:
    names = f.read().splitlines()

# Loop through the names and generate a letter for each one 
for name in names:
    #Replace the [name] placeholder with the actual name
    letter = template.replace("[name]", name)
    date = template.replace("[date]", "17/05/2023")
    location = template.replace("[location]", "Istanbul")

    # Write the personalized letter to a new file in the "Readytosend" folder
    with open(f'C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day24of100//mail+merge+Project//working_with_text_file//Readytosend/Letter_to_{name.replace(" ", "_").lower()}.txt', "a") as f:
        f.write(letter)    

    with open(f'C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day24of100//mail+merge+Project//working_with_text_file//Readytosend/Letter_to_{name.replace(" ", "_").lower()}.txt', "a") as f:
        f.write(date)

    with open(f'C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day24of100//mail+merge+Project//working_with_text_file//Readytosend/Letter_to_{name.replace(" ", "_").lower()}.txt', "a") as f:
        f.write(location)


