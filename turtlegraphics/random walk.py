from turtle import *
import random
t=Turtle()
t.speed(200)

c=["CornflowerBlue","DarkOrchid","DeepSkyBlue","LightSeaGreen","IndianRed","wheat","SlateGray","SeaGreen","red"]
d=[0,90,180,270,360]
while True:

    t.left(random.choice(d))
    t.dot(15,random.choice(c))
    t.penup()
    t.fd(30)

y=Screen()
y.exitonclick()