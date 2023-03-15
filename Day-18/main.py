import colorgram
import turtle
import random

turtle.colormode(255)
ishh = turtle.Turtle()
ishh.speed('fastest')
ishh.penup()
ishh.hideturtle()

colors = colorgram.extract('hirst.jpeg', 20)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

number_of_dots = 100

ishh.setheading(225)
ishh.forward(300)
ishh.setheading(0)

for dot_count in range(1, number_of_dots+1):
    ishh.dot(20, random.choice(rgb_colors))
    ishh.forward(50)

    if dot_count%10 == 0:
        ishh.setheading(90)
        ishh.forward(50)
        ishh.setheading(180)
        ishh.forward(500)
        ishh.setheading(0)



screen = turtle.Screen()
screen.exitonclick()