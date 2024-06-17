from turtle import Screen
import time
from snake import Snake
from snakefood import Food
from snakescore import Score
import random
y=Screen()
y.setup(width=500,height=500)
y.bgcolor("black")
y.title("my snake game")
y.tracer(0)
y.listen()
food=Food()
from score import Score
score=Score()

snake=Snake()
y.onkey(fun=snake.up,key="Up")
y.onkey(fun=snake.down,key="Down")
y.onkey(fun=snake.left,key="Left")
y.onkey(fun=snake.right,key="Right")
r=True

while r:
    y.update()
    time.sleep(0.2)
    snake.move()
    if snake.seg[0].distance(food) < 15:
        food.newfood()
        snake.extend()
        score.addscore()

    if snake.seg[0].xcor()>750 or snake.seg[0].ycor()>380 or snake.seg[0].xcor()<-750 or snake.seg[0].ycor()<-380:
        r=False
        score.clear()
        score.gameover()

    for s in snake.seg:
        if snake.seg[0]==s:
            pass
        elif snake.seg[0].distance(s)<10:
            r=False
            score.clear()
            score.gameover()










y.exitonclick()
