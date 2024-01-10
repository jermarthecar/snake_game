from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.pencolor("white")

    def present_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("arial", 15, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("arial", 15, "normal"))
