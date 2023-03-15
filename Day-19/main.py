from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a bet", "Which color turtle will win the Race ? (VIBGYOR) ")
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
y_index = [-90, -60, -30, 0, 30, 60, 90]
all_turtle = []
is_race_on = True

for i in range(0, 7):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto((-230, y_index[i]))
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on= False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! {user_bet} is the winner of the Race ")
            else:
                print(f"You've Lost ! {winning_color} is the winner of the Race ")

        rand_distance = random.randint(1, 20)
        turtle.forward(rand_distance)
        

screen.exitonclick()

