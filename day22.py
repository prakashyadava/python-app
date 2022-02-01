import time
from turtle import Turtle, Screen
from day22_player import Player
from day22_player_2 import Player2
from day22_score import Score
from day22_divide import Divide
from day22_ball import Ball

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=1400, height=800)
player1_name = my_screen.textinput(title="Player1 name", prompt="Enter a Player 1 name : ")
player2_name = my_screen.textinput(title="Player2 name", prompt="Enter a Player 2 name : ")
total_points = my_screen.textinput(title="Total Point", prompt="total number of points : ")
total_points = int(total_points)
my_screen.tracer(0)
player_1 = Player()
player_2 = Player2()
ball = Ball()
score = Score()
score.increase_score(total_points)
part = Divide()
player_1.name(player1_name)
player_2.name(player2_name)
my_screen.update()

my_screen.listen()
my_screen.onkeypress(player_1.up, "Up")
my_screen.onkeypress(player_1.down, "Down")
my_screen.onkeypress(player_2.up, 8)
my_screen.onkeypress(player_2.down, 2)

is_game_on = True

while is_game_on:

    time.sleep(ball.speed)
    ball.move()

    my_screen.update()
    if score.plyr1_score == total_points or score.plyr2_score == total_points:
        score.final_score()

        is_game_on = False
    elif ball.ycor() > 340 or ball.ycor() < -380:
        ball.bounce_y()
    elif ball.xcor() > 690:

        score.plyr1_score += 1
        score.increase_score(total_points)
        if score.plyr1_score != total_points:
            ball.reset_position()

    elif ball.xcor() < -690:
        score.plyr2_score += 1
        score.increase_score(total_points)
        if score.plyr2_score != total_points:
            ball.reset_position()

    elif player_1.distance(ball) < 60 and ball.xcor() <= -670:
        ball.bounce_x()
        # print(f"{ball.xcor()} {player_1.distance(ball)}")

    elif player_2.distance(ball) < 60 and ball.xcor() > 670:
        ball.bounce_x()
        # print(f"{ball.xcor()} {player_2.distance(ball)}")


my_screen.exitonclick()
