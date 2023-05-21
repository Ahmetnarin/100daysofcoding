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

data = pandas.read_csv(csv_file)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows() }
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Give me your name!  ").upper()
character_list = [phonetic_dict[letter] for letter in user_input]
print(character_list)






