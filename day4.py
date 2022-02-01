import random
import day4img as img

print("Welcome to rock paper scissor game")

item = ['rock' , 'paper' , 'scissor']
graphic = [img.rock , img.paper, img.scissor]
saras_score=0
computer_score =0
count = 5

while count>0:
    a = int(input("Enter 0 for rock, 1 for paper and 2 for scissor : "))
    user = item[a]
    b = random.randint(0, 2)
    comp = item[b]
    if a == 0 and b == 2:

        print(f"You choose {user}\n"
              f"{graphic[a]}\n"
              f"and computer choose {comp}\n"
              f"{graphic[b]}\n"
              f"You won")
        saras_score +=1
    elif b == 0 and a == 2:
        print(f"You choose {user}\n"
              f"{graphic[a]}\n"
              f"and computer choose {comp}\n"
              f"{graphic[b]}\n"
              f"You loose")
        computer_score +=1
    elif b > a:
        print(f"You choose {user}\n"
              f"{graphic[a]}\n"
              f"and computer choose {comp}\n"
              f"{graphic[b]}\n"
              f"You loose")
        computer_score += 1
    elif b == a:
        print(f"You choose {user}\n"
              f"{graphic[a]}\n"
              f"and computer choose {comp}\n"
              f"{graphic[b]}\n"
              f"It's a  Draw")
    else:
        print(f"You choose {user}\n"
              f"{graphic[a]}\n"
              f"and computer choose {comp}\n"
              f"{graphic[b]}\n"
              f"You won")
        saras_score += 1
    count -=1

print(f"your score {saras_score}\ncomputer score {computer_score}")

if saras_score>computer_score:
    print("You won")
elif saras_score==computer_score:
    print("It's a draw")
else:
    print("You loose")