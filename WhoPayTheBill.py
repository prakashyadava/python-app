import random

# print("Who gonna pay the bill")

a = int(input("Enter no. of people : "))

rand = random.randint(0,a-1)

b = input("Enter the names of person separated by comma: ")

names = b.split(", ")

print(f"{names[rand]} is going to pay the bill ")
