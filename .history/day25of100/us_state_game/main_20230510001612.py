import turtle 
import csv

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


answer_state =  screen.textinput(title ="Guess the state", prompt="What is another state's name?").title()
print(answer_state)

if check_user_input(answer_state):
    print("Match found in CSV file.")
    x = row[1]
    y = row[2]
    turtle.penup()
                turtle.goto(x,y)
                turtle.write(row[0], align="center", font=("Arial", 12, "normal"))
                # Hide the turtle cursor
                turtle.hideturtle()
else:
    print("No match found in CSV file.")






