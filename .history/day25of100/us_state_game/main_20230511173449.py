import turtle 
import csv
import pandas as pd

# def get_coordinates(x,y):
#     print(f"Clicked at coordinates : ({x}, {y})")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//us_state_game//blank_states_img.gif"
csv_file = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//us_state_game//50_states.csv"
screen.addshape(image)
turtle.shape(image)




def check_user_input(answer_state):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if answer_state == row[0]:
                return True 
    return False 


game_is_on = True
score = 0
correct_guess = []
while game_is_on:
    answer_state =  screen.textinput(title ="Guess the state", prompt="What is another state's name?").title()
    print(answer_state)

    if check_user_input(answer_state):
        score += 1
        correct_guess.append(answer_state)
        print("Match found in CSV file.")
        data = pd.read_csv(csv_file)
        filtered_data = data[data["state"] == answer_state]
        print(filtered_data["x"])
        x_values = int(filtered_data["x"])
        y_values = int(filtered_data["y"])
        tr = turtle.Turtle()
        tr.penup()
        tr.goto(x_values,y_values)
        tr.write(answer_state, align="center", font=("Arial", 12, "normal"))
        # Hide the turtle cursor
        tr.hideturtle()
    else:
        print("No match found in CSV file.")
        game_is_on = False

        M1_AX_HBA01_S2P7


print(correct_guess)


screen.exitonclick()


