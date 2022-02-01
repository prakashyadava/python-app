from turtle import Turtle,Screen
from day23_car import Car
from  day23_player import Player
from  day23_scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=1000, height=600)
my_screen.tracer(0)
car = Car()
player = Player()
score = Scoreboard()
my_screen.listen()
my_screen.onkeypress(player.move, "Up")
for i in range(200):
    car.create_car()
    car.move_car()
# time.sleep(5)
is_game_on = True


while is_game_on:
    time.sleep(0.1)
    my_screen.update()
    car.create_car()
    car.move_car()
    for cr in car.all_Car:
        if cr.distance(player) < 20:
            is_game_on = False
            score.game_over()


    if player.ycor() >= 275:
        score.increase_Score()
        player.goto(0,-280)
        car.increase_speed()


my_screen.exitonclick()