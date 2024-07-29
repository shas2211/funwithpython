from turtle import *

pos=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.seg=[]
        self.create()

    def left(self):
        self.seg[0].setheading(180)

    def up(self):
        self.seg[0].setheading(90)
        
    def down(self):
        self.seg[0].setheading(270)
    def right(self):
        self.seg[0].setheading(0)


    def create(self):
        for i in pos:
            self.addseg(i)

    def addseg(self,i):
        p = Turtle("square")
        p.color("white")
        p.penup()
        p.goto(i)
        self.seg.append(p)
    def extend(self):
        self.addseg(self.seg[-1].position())

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            X = self.seg[i - 1].xcor()
            Y = self.seg[i - 1].ycor()
            self.seg[i].goto(X, Y)
        self.seg[0].fd(20)

        