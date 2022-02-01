from turtle import Turtle

class Divide:

    def __init__(self):

        # self.partition()
        self.hori()

    def partition(self):
        part = Turtle()
        part.speed("fastest")
        part.shape("square")
        part.shapesize(0.3, 0.3)
        part.penup()
        part.color("white")

        part.goto(0,380)
        part.setheading(270)
        for i in range(38):
            part.pendown()
            part.forward(10)
            part.penup()
            part.forward(10)
        part.hideturtle()
    def hori(self):
        hor = Turtle()
        hor.speed("fastest")
        hor.shape("square")
        hor.shapesize(0.3, 0.1)
        hor.penup()
        hor.color("white")

        hor.goto(-700,350)
        hor.pendown()
        hor.forward(1660)
        hor.hideturtle()