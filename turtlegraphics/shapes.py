from turtle import *
t=Turtle()
t.speed(30)
t.left(180)
t.fd(750)
t.left(180)
for k in range(10):
    for i in range(3, 15, 1):
        for j in range(i):
            t.fd(100)
            t.right(360 / i)
    for i in range(3, 15, 1):
        for j in range(i):
            t.fd(100)
            t.left(360 / i)

    t.fd(200)















y=Screen()
y.exitonclick()