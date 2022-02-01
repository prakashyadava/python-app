from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 30, "normal")

POSITION = (680, 0)


class Player2(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(POSITION)

    def up(self):
        if self.ycor()<300:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor()>-340:
            self.goto(self.xcor(), self.ycor() - 20)

    def name(self, name):
        plyr_2 = Turtle()
        plyr_2.speed("fastest")
        plyr_2.hideturtle()
        plyr_2.color("white")
        plyr_2.penup()
        plyr_2.goto(600, 350)
        plyr_2.write(f"{name}", align=ALLIGNMENT, font=FONT)