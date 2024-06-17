from turtle import Turtle
import random
from snake import Snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed(10)
        Z=random.randint(-240,240)
        Zz=random.randint(-240,240)

        self.goto( Z,Zz)

    def newfood(self):
        Z = random.randint(-240, 240)
        Zz = random.randint(-240, 240)
        self.goto(Z, Zz)


