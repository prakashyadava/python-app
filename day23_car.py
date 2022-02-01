from turtle import Turtle
import random
colors = ["pink", "orange", "yellow", "green", "white", "grey"]
STARTING_MOVING_DISTANCE = 5
MOVING_INCREMENT = 10

class Car(Turtle):

    def __init__(self):
        self.all_Car = []
        self.div = []
        # self.random_div()
        # self.previous_random_y_value = 0
        self.car_speed = STARTING_MOVING_DISTANCE
        # self.time_delay = 0.1
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 2 or random_chance == 5:
            new_car = Turtle()
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-255, 255)
            # while random_y == self.previous_random_y_value:
            #     random_y = random.choice(self.div)
            # self.previous_random_y_value = random_y
            new_car.goto(450, random_y)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_Car.append(new_car)




    def move_car(self):
        for car in self.all_Car:
            car.backward(self.car_speed)
    # def random_div(self):
    #     for i in range(-260,261):
    #         if i % 22 == 0 :
    #             self.div.append(i)
    def increase_speed(self):
        self.car_speed += MOVING_INCREMENT
        # self.time_delay *= 0.9

