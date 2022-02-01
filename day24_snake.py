from turtle import Turtle
import time
ALLIGNMENT = "left"
FONT = ("Arial", 30, "normal")

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
REFRESH_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        # super().__init__()

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")


            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(STARTING_POSITION) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def update(self):
        pos_x = self.segments[len(self.segments)-1].xcor()
        pos_y = self.segments[len(self.segments)-1].ycor()


        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")

        new_segment.color("white")
        new_segment.goto(pos_x, pos_y)
        self.segments.append(new_segment)
        position = (pos_x, pos_y)
        STARTING_POSITION.append(position)

    def reset_snake(self):
        tim = Turtle()
        tim.speed("fastest")
        tim.hideturtle()
        tim.color("white")
        tim.penup()
        for i in range(1,4):
            tim.write(f"{i}", align=ALLIGNMENT, font=FONT)
            time.sleep(1)
            tim.clear()


        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        STARTING_POSITION.clear()
        for pos in REFRESH_POSITION:
            STARTING_POSITION.append(pos)
        self.create_snake()
        self.head = self.segments[0]
