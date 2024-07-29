from turtle import Turtle

class Pad2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(-460,0)


    def w(self):
        Y=self.ycor()+20
        self.goto(self.xcor(),Y)
    def s(self):
        Y = self.ycor() - 20
        self.goto(self.xcor(), Y)
