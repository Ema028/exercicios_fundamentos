from turtle import Turtle

font = ("Verdana", 20, "normal")
align = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(x = 0, y = 270)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} Record = {self.high_score}", font = font, align = align)

    def point(self):
        self.score += 1
        self.scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.scoreboard()
