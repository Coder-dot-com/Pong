from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    
    def point_score_left(self):
        self.l_score += 1
        self.write_score()


    def point_score_right(self):
        self.r_score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Courier", 50, "normal"))
