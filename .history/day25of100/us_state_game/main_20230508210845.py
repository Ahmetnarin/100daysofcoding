import turtle 

def get_coordinate(x,y):
    print(f"Clicked at coordinates : ({x}, {y})")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C://Users//AHNARIN//Desktop//Ahnarin//100_days_of_coding//day25of100//us_state_game//blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Register the function to handkle mouse click 
screen.onscreenclick









screen.exitonclick()