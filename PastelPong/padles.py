from turtle import Turtle

class Padle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("salmon")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 5)
        self.goto(x, y)
        self.setheading(90)

    def up(self):
        if self.ycor() < self.screen.window_height() / 2 - 50:
            self.forward(50)

    def down(self):
        if self.ycor() > -self.screen.window_height() / 2 + 50:
            self.backward(50)
