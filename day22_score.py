from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 30, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.plyr1_score = 0
        self.plyr2_score = 0
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-50,350)
        self.write(f"{self.plyr1_score}", align=ALLIGNMENT, font=FONT)
        self.goto(50, 350)
        self.write(f"{self.plyr2_score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self, total):
        self.clear()
        self.goto(-50, 350)
        self.write(f"{self.plyr1_score}/{total}", align=ALLIGNMENT, font=FONT)
        self.goto(50, 350)
        self.write(f"{self.plyr2_score}/{total}", align=ALLIGNMENT, font=FONT)

    def final_score(self):
        final = Turtle()
        final.speed("fastest")
        final.hideturtle()
        final.color("white")
        final.penup()
        final.goto(0, 0)
        final.write(f"G A M E  O V E R", align=ALLIGNMENT, font=FONT)
