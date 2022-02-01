from turtle import Turtle
FONT = ("Arial", 30, "normal")
ALLIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-480,255)
        self.score = 0
        self.increase_Score()

    def increase_Score(self):
        self.clear()

        self.write(f"Level : {self.score}", font=FONT)
        self.score += 1
    def game_over(self):

        self.goto(330, 255)
        self.write(f"G A M E  O V E R", align=ALLIGNMENT, font=FONT)



