from turtle import Turtle
import random

new_radius = 0.8

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = new_radius, stretch_wid = new_radius)
        self.pixels = 20 * new_radius
        self.color("LightPink")
        self.speed("fastest")
        self.spam()


    def spam(self):
        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 250))
