from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.score1}|{self.score2}", align="center", font=("Arial",70,"normal"))
        self.hideturtle()

    def addscore1(self):
        self.clear()
        self.score1 += 1
        self.write(f"{self.score1}|{self.score2}", align="center", font=("Arial", 70, "normal"))
    def addscore2(self):
        self.clear()
        self.score2 += 1
        self.write(f"{self.score1}|{self.score2}", align="center", font=("Arial", 70, "normal"))

    def scorereset(self):
        self.score1=0
        self.score2=0
        self.clear()
        self.write(f"{self.score1}|{self.score2}", align="center", font=("Arial", 70, "normal"))

