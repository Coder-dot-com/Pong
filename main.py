from paddle import Paddle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle_right = Paddle("right")
paddle_left = Paddle("left")
screen.onkey(fun=paddle_right.move_up, key="Up")
screen.onkey(fun=paddle_right.move_down, key="Down")
screen.onkey(fun=paddle_left.move_up, key="w")
screen.onkey(fun=paddle_left.move_down, key="s")


ball = Ball()

scoreboard = Scoreboard()
scoreboard.write_score()

game_is_on = True



while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #detect if ball hit wall
    if ball.ycor() > 290 or ball.ycor() <-280:
        ball.bounce_y()

    #has ball hit paddle?
    if (ball.distance(paddle_right) < 50 and 320 < ball.xcor() <350) or (ball.distance(paddle_left) < 50 and -350 < ball.xcor() < -320):
        ball.bounce_x()

    #ball out of bounds?
    if (ball.xcor() > 380):  #right
        ball.reset_position()
        scoreboard.point_score_left()

    if (ball.xcor() < -380): #left
        ball.reset_position()
        scoreboard.point_score_right()

    # game plays till anyone reaches 3 points

    if (scoreboard.l_score >= 3 or scoreboard.r_score >= 3):
        game_is_on = False
    
if (game_is_on == False):
    scoreboard.game_over()


screen.exitonclick()