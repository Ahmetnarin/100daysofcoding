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


answer_state = screen.textinput(title ="Guess the state", prompt="What is another state's name?")
print(answer_state)

def check_user_input(answer_state):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if answer_state == row






