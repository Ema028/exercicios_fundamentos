from turtle import Screen
from padles import Padle
from ball import Ball
from scoreboard import Scoreboard
import time

on = True

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("bisque")
screen.title("Pastel Pong")
screen.tracer(0)

# Coordenadas x e y máximo da tela
width = screen.window_width()/2
height = screen.window_height()/2

x = width - 30
padle1 = Padle(x, 0)
padle2 = Padle(-x, 0)
ball = Ball()
score = Scoreboard()

# Interação com o usuário
screen.listen()
screen.onkey(key = "Up", fun = padle1.up)
screen.onkey(key = "w", fun = padle2.up)
screen.onkey(key = "Down", fun = padle1.down)
screen.onkey(key = "s", fun = padle2.down)

while on:
    # Delay entre as animações
    screen.update()
    time.sleep(ball.velocity)
    ball.move()

    # Detecta colisão com o teto ou com o chão
    if ball.ycor() > height - 20 or ball.ycor() < -height + 20:
        ball.bounce_vertically()

    # Detecta colisão com as raquetes e aumenta velocidade da bola
    if (ball.distance(padle1) < 50 and ball.xcor() > width - 50)  or (ball.distance(padle2) < 50 and ball.xcor() < -width + 50):
        ball.bounce_horizontally()

    # Se a bola fugir:
    if ball.xcor() > width:
        ball.reset()
        score.point(0)
    elif ball.xcor() < -width:
        ball.reset()
        score.point(180)

screen.exitonclick()
