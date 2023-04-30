import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")



game_is_on = True
while game_is_on:    
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect colision with car 
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect succesfull crosing 
    if player.yposition():
        player.go_to_start()
        cars.speed_up()
        score.score_of_player()


screen.exitonclick()