import random

print("Welcome to virtual coin toss program")
outcomes =['head','tail']
user_call = input("what's your call, head or tail : ")
comp_call = random.choice(outcomes)
if user_call==comp_call:
    print("You won")
else:
    print("You loose")
