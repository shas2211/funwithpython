from turtle import Turtle
import random

class Ball(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("circle")
         self.color("red")
         self.penup()
         self.xmove=10
         self.ymove=10


     def move(self):
         X = self.xcor() + self.xmove
         Y = self.ycor() + self.ymove
         self.goto(X,Y)

     def bounce(self):
         self.ymove*=-1

     def bounce1(self):
         self.xmove*=-1

     def resett(self):
         self.goto(0,0)
         self.bounce1()


    
