import pandas as pd

csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//us_state_game//50_states.csv"

satate_name = "Alaska"

def check_user_input(answer_state):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if answer_state == row[0]:
                return True 
    return False 

data = pd.DataFrame(csv_file)

us_state_name = "Alaska"

