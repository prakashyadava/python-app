import random
import day11_art as art

print(art.logo)
def win():
    print(
        f"your card list : {user_card} and your score : {user_sum}\nopponent card list : {com_card} and opponent score : {com_sum}")
    print(
        f"**********************************************\n                 Y O U - W I N                  \n**********************************************")

def lose():
    print(
        f"your card list : {user_card} and your score : {user_sum}\nopponent card list : {com_card} and opponent score : {com_sum}")
    print(
        f"**********************************************\n                 Y O U - L O S E               \n**********************************************")
def draw():
    print(
        f"your card list : {user_card} and your score : {user_sum}\nopponent card list : {com_card} and opponent score : {com_sum}")
    print(
        f"**********************************************\n                 D R A W                 \n**********************************************")
points = {
    'A': [1, 11],
    'J': 10,
    'Q': 10,
    'K': 10,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
card_list = ['A', 'J', 'Q', 'K', '2', '3', '4', '5', '6', '7', '8', '9']
com_card = []
com_sum = 0
user_sum = 0
user_card = []


def com_initial(com_sum, com_card):
    sum = com_sum
    card = random.choice(card_list)
    if card == 'A' and sum < 11:
        sum += points[card][1]
        com_card.append(points[card][1])
    elif card == 'A' and sum >= 11:
        sum += points[card][0]
        com_card.append(points[card][0])
    else:
        sum += points[card]
        com_card.append(points[card])
    return sum



def user_initial(user_sum, user_card):
    sum = user_sum
    card = random.choice(card_list)
    if card == 'A' and sum < 11:
        sum += points[card][1]
        user_card.append(points[card][1])
    elif card == 'A' and sum >= 11:
        sum += points[card][0]
        user_card.append(points[card][0])
    else:
        sum += points[card]
        user_card.append(points[card])
    return sum

for i in range(0,2):
    com_sum = com_initial(com_sum, com_card)

    user_sum = user_initial(user_sum, user_card)



print(f"computer card list : {com_card[0]}\nUser card list : {user_card} and current score : {user_sum}")
flag = True
if com_sum==21 and user_sum==21:
    flag = False
    print("Draw")
    print(f"computer card list : {com_card}\nUser card list : {user_card} and current score : {user_sum}")
elif com_sum==21:
    flag = False
    print("com has blackjack")
    print(f"computer card list : {com_card}\nUser card list : {user_card} and current score : {user_sum}")
elif user_sum==21:
    flag = False
    print("User has blackjack")
    print(f"computer card list : {com_card}\nUser card list : {user_card} and current score : {user_sum}")

while flag and user_sum<=21:
    ask = input("Type 'y' to get another card or type 'n' to pass : ")
    if ask=='y':
        user_sum = user_initial(user_sum, user_card)
        print(f"computer's first hand : {com_card[0]}\nUser card list : {user_card} and current score : {user_sum}")
    else:
        flag = False

flag2 = True
if user_sum>21:
    flag2 = False

while flag2 and com_sum <17:
    com_sum = com_initial(com_sum, com_card)
    if com_sum >=17:
        print(f"Computer Card list : {com_card}")
        flag2 =False
    else:
        print(f"Computer Card list : {com_card}")



print("*********************** S C O R E *************************")
if user_sum>21:
    lose()
elif com_sum==user_sum:
    draw()
elif com_sum>21:
    win()
elif com_sum<user_sum:
    win()
else:
    lose()