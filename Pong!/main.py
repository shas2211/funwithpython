from turtle import *
from ball import Ball
from pad1 import Pad1
from pad2 import Pad2
from score import Score
import time

y=Screen()
y.setup(width=1000,height=700)
y.bgcolor("black")
y.title("Pong")
y.tracer(0)


p=Pad1()
p1=Pad2()
b=Ball()
score=Score()


y.listen()
y.onkeypress(fun=p.ww,key="Up")
y.onkeypress(fun=p.ss,key="Down")
y.listen()
y.onkeypress(fun=p1.w,key="w")
y.onkeypress(fun=p1.s,key="s")


def game():
    dd=""
    game_on = True
    while game_on:
        time.sleep(0.05)
        y.update()
        b.move()
        if b.ycor() > 330 or b.ycor() < -330:
            b.bounce()

        if b.distance(p) < 50 and b.xcor() > 440:
            b.bounce1()

        if b.distance(p1) < 50 and b.xcor() < -440:
            b.bounce1()

        if b.xcor() > 460:
            b.resett()
            score.addscore1()

        if b.xcor() < -460:
            b.resett()
            score.addscore2()
        if score.score1 == 5:
            game_on = False
            dd =y.textinput(title="gameover!! PLAYER 1 WINS",prompt="do you wish to play again?? type y/n")
            if dd.lower() == "y":
                score.scorereset()
                game()
            else:
                game_on = False
        if score.score2 == 5:
            game_on = False
            dd = y.textinput(title="gameover!! PLAYER 2 WINS", prompt="do you wish to play again?? type y/n")
            if dd.lower() == "y":
                score.scorereset()
                game()
            else:
                game_on = False

game()
y.exitonclick()