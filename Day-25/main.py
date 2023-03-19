import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 are found", "What's next state Name ?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)

        learn = pd.DataFrame(missing_state)
        learn.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = Turtle()
        t.penup()
        t.hideturtle()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()