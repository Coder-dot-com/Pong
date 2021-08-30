from paddle import Paddle
from turtle import Screen
from paddle import Paddle
from ball import Ball
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



game_is_on = True

while game_is_on == True:
    screen.update()
    ball.move()
    time.sleep(0.1)







screen.exitonclick()