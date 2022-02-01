from turtle import Turtle, Screen
import time
import pandas

ALLIGNMENT = "left"
FONT = ("Arial", 20, "normal")
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
tur = Turtle()
tur.shape(img)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
score = 0

score_tur = Turtle()
score_tur.penup()
score_tur.ht()
score_tur.goto(100, 250)






# def timer():
#     tim = Turtle()
#     tim.speed("fastest")
#     tim.hideturtle()
#     tim.color("black")
#     tim.penup()
#     tim.goto(0,250)
#     for i in range(4, -1,-1):
#         for j in range(59, -1,-1):
#             tim.write(f"Remaining Time: {i}:{j}", align=ALLIGNMENT, font=FONT)
#             time.sleep(1)
#             tim.clear()
#


def score_update(score):
    score_tur.clear()
    score_tur.write(f"Score: {score}/50", align=ALLIGNMENT, font=FONT)

is_Game_on = True
while is_Game_on:

    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name? ").title()

    if(answer_state == "Exit"):
        is_Game_on = False
    else:
        answer_state_row = data[data["state"] == answer_state]
        if (state_list.count(answer_state) == 1):
            score += 1
            score_update(score)
            xcor = int(answer_state_row["x"])
            ycor = int(answer_state_row["y"])
            place = Turtle()
            place.ht()
            place.penup()
            place.goto(xcor, ycor)
            place.write(answer_state)
        score_update(score)

# screen.exitonclick()
