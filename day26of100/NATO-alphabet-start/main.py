student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import csv 
csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day26of100//NATO-alphabet-start//nato_phonetic_alphabet.csv"

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    data_dict = {key: value for (key, value) in reader }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Give me your name!  ").upper()
character_list = [char for char in user_input]
print(character_list)


# for (key, value) in data_dict.items():
#     # print(key)
#     # print(value)
#     print(character_list)

my_data = pandas.DataFrame(data_dict)

# for (index , row) in my_data.iterrows():
#     print(index,row)

for letter in character_list:
    if letter in data_dict:
        print(data_dict[letter])





