from turtle import*
import random
t=Turtle()

t.speed(200)
c=["CornflowerBlue","DarkOrchid","DeepSkyBlue","LightSeaGreen","IndianRed","wheat","SlateGray","SeaGreen"]
t.left(180)
t.fd(600)
t.left(180)

for j in range(15):
    for i in range(90):
        t.pencolor(random.choice(c))
        t.circle(100)
        t.left(4)
    t.fd(100)

y=Screen()
y.exitonclick()