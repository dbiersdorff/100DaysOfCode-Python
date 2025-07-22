from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.title("Pong")
screen.bgcolor("black")
screen.canvheight = 600
screen.canvwidth = 800
screen.tracer(0)

paddle1 = Paddle(-450)
paddle2 = Paddle(450)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle2.go_up, "Up")
screen.onkey(paddle2.go_down, "Down")

screen.onkey(paddle1.go_up, "w")
screen.onkey(paddle1.go_down, "s")

game_is_on = True

while(game_is_on):
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.distance(paddle2) < 35 and ball.xcor() > 190 or ball.distance(paddle1) < 35 and ball.xcor() < -190:
        ball.bounce_x()


    if ball.xcor() > 450:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -470:
        ball.reset_pos()
        scoreboard.r_point()



screen.exitonclick()