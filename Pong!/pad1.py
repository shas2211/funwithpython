from turtle import Turtle

class Pad1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(460,0)


    def ww(self):
        Y=self.ycor()+20
        self.goto(self.xcor(),Y)
    def ss(self):
        Y = self.ycor() - 20
        self.goto(self.xcor(), Y)
