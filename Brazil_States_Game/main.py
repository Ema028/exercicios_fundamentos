from time import sleep
from unicodedata import normalize
from tkinter import messagebox
import turtle
import pandas
import pop_up

screen = turtle.Screen()
screen.title("Estados do Brasil")

img = "mapa_brasil.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("estados.csv")

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

guessed_states = []

while len(guessed_states) < 26:
    answer = screen.textinput(title = f"{len(guessed_states)}/26 Estados Corretos",
                              prompt = "Qual o nome de outro estado?").title()
    ascii_answer = normalize('NFKD', answer).encode('ASCII', 'ignore').decode('ASCII')

    if answer == 'Sair':
        missing_states = [state for state in data.states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states).to_csv("estados_faltando.csv")
        break

    if ascii_answer in guessed_states:
        messagebox.showinfo("Repetido", f"Você já acertou o estado do {answer}")
        continue

    found = False
    for state in data.state:
        ascii_state = normalize('NFKD', state).encode('ASCII', 'ignore').decode('ASCII')
        if ascii_answer == ascii_state:
            guessed_states.append(ascii_state)
            data_row = data[data.state == state]
            turtle.goto(data_row.x.item(), data_row.y.item())
            turtle.write(state)
            found = True

    if not found:
        messagebox.showinfo("Errado",f"{answer} não é um estado" )

sleep(1)
turtle.clear()
turtle.goto(-(screen.window_width()/4), 0)
turtle.write("Parabéns", font=("Arial", 58, "normal"))
pop_up.win()
screen.exitonclick()
