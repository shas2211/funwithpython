from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score:{self.score} ",align="center",font=("Arial",16,"bold"))
        self.hideturtle()
        self.highscore=0
    def addscore(self):
        self.clear()

        self.score+=1
        self.write(f"score:{self.score} High score:{self.highscore} ", align="center", font=("Arial", 16, "bold"))
    def gameover(self):
        self.write(" GAME OVER !!!", align="center", font=("Arial", 16, "bold"))
        if self.score>self.highscore :
            self.highscore=self.score
            self.score=0








