import random

number = random.randint(1,100)

print("Guess a number between 1 to 100")
difficulty = input("Choose a difficulty , type 'easy' or 'hard' : ")

life = 0
if difficulty=='easy':
    life = 10
else:
    life = 5
guessed = False

while not guessed and life>0:
    print(f"You have {life} life remaining")
    guess = int(input("Guess a number : "))
    if guess < number:
        print("Too Low")
        life -=1
    elif guess > number:
        print("Too High")
        life -=1
    else:
        print("You guessed the number correctly")
        guessed = True

if not guessed:
    print(f"You guessed a wrong number ,{number} is the right number")