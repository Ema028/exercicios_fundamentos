import turtle as t
import random

turtles = []

for i in range (5):
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.speed("fastest")
    new_turtle.penup()
    turtles.append(new_turtle)

directions = [0, 90, 180, 270]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def win():
    for turtle in turtles:
        for i in range (20):
            turtle.color(random_color())
            turtle.setheading(random.choice(directions))
            turtle.forward(50)
