# import turtle
# from turtle import Turtle,Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
#
# my_screen = Screen()
# timmy.color("red","yellow")
# timmy.forward(200)
# timmy.left(200)
# my_screen.exitonclick()
#
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)