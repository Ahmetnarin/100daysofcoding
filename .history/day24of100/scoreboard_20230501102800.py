from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.load_high_score()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.load_high_score():
            self.highscore = self.score 
            self.save_highscore(highscore=self.highscore)
        self.score = 0 
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        # self.highscore.write(f"{self.score}")
        self.update_scoreboard()

    # Load high score from file 
    def load_high_score(self):
        try:
            with open("data.txt", "r") as file:
                self.highscore = int(file.read())
        return self.highscore
    

    # Save high score to file  
    def save_highscore(self, highscore):
        with open("data.txt" , "w") as file:
            file.write(str(self.highscore))

