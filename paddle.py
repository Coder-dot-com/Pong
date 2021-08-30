from turtle import Turtle

#Directions
NORTH = 90
RIGHT = 0
SOUTH = 270
LEFT = 180



class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.setheading(RIGHT)
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(0)

        #Positions paddle and sets direction required for movement during game

        if direction == "right":
            self.forward(350)
            self.setheading(NORTH)

        else:
            self.forward(-350)
            self.setheading(NORTH)



    def move_up(self):
        if (self.ycor() < 250):
            self.forward(20)
    def move_down(self):
        if (self.ycor() > -250):
            self.forward(-20)