from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

game = True
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("HotPink")
screen.title("Barbie Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Right", fun = snake.right)
screen.onkey(key = "Left", fun = snake.left)

while game is True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Colisão entre a comida e a cobra
    if snake.head.distance(food) < (food.pixels + 1):
        food.spam()
        score.point()
        snake.grow()

    # Colisão com a parede
    xcor = snake.head.xcor()
    ycor = snake.head.ycor()
    if xcor < -280 or xcor > 280 or ycor > 280 or ycor < -280:
        score.reset()
        snake.reset()

    # Colisão com a cauda
    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
