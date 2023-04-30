from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        
        self.score = 1 
        self.update_score()  
        
    def update_score(self):
        self.clear()
        self.goto(-150,200) 
        self.write(f"Level: {self.score}",  align = "center" , font = FONT)
        
    def score_of_player(self):
        self.score += 1
        self.update_score()




