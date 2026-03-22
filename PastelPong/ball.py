from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.velocity = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_vertically(self):
        self.y *= -1

    def bounce_horizontally(self):
        self.x *= -1
        self.velocity *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.velocity = 0.1
