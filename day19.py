import random
from turtle import Turtle,Screen
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=1000 , height=800)
is_race_on = True

turtle_name = ["duke", "shanky", "saras", "harsh", "pratyush", "himanshu"]
colors = ["red", "blue", "green", "purple", "orange", "yellow"]
i = 300
player_details = {"red" : "Computer", "blue" : "Computer", "green": "Computer", "purple": "Computer", "orange": "Computer", "yellow": "Computer"}
number= my_screen.textinput(title="How many Players",prompt="Enter total Number of players (not more than 6): ")
number = int(number)
for _ in range(number):
    name = my_screen.textinput(title="Player Name",prompt=f"Player {_+1}, Enter your name: ")
    color = my_screen.textinput(title="color Name",prompt=f"{name} enter your color name: ")
    player_details[color] = name

turtle_obj = []
for name in turtle_name:
    name = Turtle()
    name.shape("turtle")
    name.shapesize(2)
    col = random.choice(colors)
    name.color(col)
    colors.remove(col)

    name.penup()
    name.goto(x=-460,y= i)
    turtle_obj.append(name)
    i -= 70
print(player_details)
#
# chotu_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (Shanky) Enter a color: ")
# prakash_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? (Prakash) Enter a color: ")

while is_race_on:
    for turt in turtle_obj:
        if turt.xcor() > 470 and is_race_on:
            is_race_on = False
            result = f"{player_details[turt.pencolor()]} is the winner"
            print(result)

        turt.forward(random.randint(0,15))



# duke = Turtle()
# shanky = Turtle()
# saras = Turtle()
# harsh = Turtle()
# duke.shape("turtle")
# shanky.shape("turtle")
# saras.shape("turtle")
# harsh.shape("turtle")



# duke.goto(x=-230, y=0)
# shanky.goto(x=-230, y=100)
# saras.goto(x=-230, y=-50)
# harsh.goto(x=-230, y=50)
# duke.shape("arrow")
# duke.speed("fastest")
# def move_forword():
#     duke.forward(15)
# def move_backword():
#     duke.backward(15)
# def move_counter_clkwise():
#     new_heading = duke.heading() +10
#     duke.setheading(new_heading)
# def move_clkwise():
#     new_heading = duke.heading() - 10
#     duke.setheading(new_heading)
# def clear():
#     duke.clear()
#     duke.penup()
#     duke.home()
#     duke.pendown()
# my_screen.listen()
# my_screen.onkey(move_forword, "w")
# my_screen.onkey(move_backword, "s")
# my_screen.onkey(move_counter_clkwise, "a")
# my_screen.onkey(move_clkwise, "d")
# my_screen.onkey(clear,"space")
my_screen.exitonclick()