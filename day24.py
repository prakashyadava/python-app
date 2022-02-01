from turtle import Screen
from day24_snake import Snake
from day24_food import Food
from day24_score import Score

import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.setup(width=600, height=600)
my_screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score_board.update()
        food.refresh()
        snake.update()
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() < -280 or snake.head.ycor() > 270:
        # is_game_on = False
        score_board.reset()
        snake.reset_snake()
        food.refresh()
        # score_board.final()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10 :
            # is_game_on = False
            score_board.reset()
            snake.reset_snake()
            food.refresh()

my_screen.exitonclick()
