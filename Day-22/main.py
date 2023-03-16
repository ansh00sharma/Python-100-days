from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() >270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(l_paddle)<50 and ball.xcor() < -320 or ball.distance(r_paddle)<50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_update()

    if ball.xcor() < -380 :
        ball.reset_position()
        score.r_update()

screen.exitonclick()