import random
import turtle
from turtle import Turtle, Screen
import colorgram


my_screen = Screen()
my_screen.bgcolor("black")
duke = Turtle()
duke.shape("arrow")
duke.color("red","yellow")
turtle.colormode(255)

# count = 20
# duke.begin_fill()
# while count>0:
#
#     if count%2!=0:
#         duke.penup()
#         duke.forward(10)
#     else:
#         duke.pendown()
#         duke.forward(10)
#     count -= 1
# duke.end_fill()

# colors = ["cornflower blue", "green", "brown", "white", "yellow", "magenta", "orange", "dark red"]
# for i in range(3,11):
#     for j in range(i):
#         duke.color(color[i-3])
#         duke.forward(100)
#         duke.right(360 / i)
# angles = [0, 90, 180, 270]
# i = 1
duke.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
# for _ in range(200):
#
#     duke.hideturtle()
#     duke.pensize(10)
#     duke.forward(60)
#     duke.left(random.choice(angles))
#     duke.color(random_color())
#     i *= 2

# for _ in range(72):
#     duke.circle(100)
#     duke.left(5)
#     duke.color(random_color())
colors = colorgram.extract("hirst.jpg", 30)
rgb_colors = []

for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    rgb = (r,g,b)
    rgb_colors.append(rgb)
duke.width(5)
for _ in range(10):
    for i in range(15):
        duke.pendown()
        duke.color(random.choice(rgb_colors))
        duke.dot(15)
        duke.penup()
        duke.forward(30)


    duke.left(180)
    duke.penup()
    duke.forward(450)
    duke.right(90)
    duke.forward(30)
    duke.right(90)


my_screen.exitonclick()

