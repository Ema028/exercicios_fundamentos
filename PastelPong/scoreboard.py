from turtle import Turtle

font = ("Verdana", 30, "normal")
align = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("DarkSalmon")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x = 0, y = self.screen.window_height() / 2 - 50)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"{self.r_score} : {self.l_score}", font=font, align=align)

    # Atualiza o placar
    def point(self, direction):
        if direction == 0:
            self.r_score += 1
        elif direction == 180:
            self.l_score += 1
        self.clear()
        self.scoreboard()
