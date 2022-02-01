from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 30, "normal")

POSITION = (-688, 0)


class Player(Turtle):

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

        plyr_1 = Turtle()
        plyr_1.speed("fastest")
        plyr_1.hideturtle()
        plyr_1.color("white")
        plyr_1.penup()
        plyr_1.goto(-600, 350)
        plyr_1.write(f"{name}", align=ALLIGNMENT, font=FONT)




