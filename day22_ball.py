from turtle import Turtle
import time
from random import randint
ALLIGNMENT = "left"
FONT = ("Arial", 30, "normal")

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 15
        self.y_move = 15
        self.speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed  *= 0.9

    def reset_position(self):
        tim = Turtle()
        tim.speed("fastest")
        tim.hideturtle()
        tim.color("white")
        tim.penup()
        for i in range(1,4):
            tim.write(f"{i}", align=ALLIGNMENT, font=FONT)
            time.sleep(1)
            tim.clear()
        self.goto(0,randint(-300,300))
        self.bounce_x()
        self.speed = 0.1







