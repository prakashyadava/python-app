import random
from  day14_logo_data import data
from  day14_logo_data import logo
from  day14_logo_data import vs


def generate_account():
    return random.choice(data)

def format_account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check(guess,account_a,account_b):
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    if a_follower>b_follower:
        return guess=='a'
    else:
        return guess=='b'

def game():
    score =0
    game_continued = True

    while game_continued:

        account_a = generate_account()
        account_b = generate_account()
        print(logo)
        while account_a == account_b:
            account_b = generate_account()

        format_account_a = format_account(account_a)
        format_account_b = format_account(account_b)
        print(f"Compare A : {format_account_a}\n\n{vs}\n\nAgainst B : {format_account_b}")
        guess= input("Who has more followers ? A or B : ").lower()
        is_correct = check(guess,account_a,account_b)
        if is_correct:
            score += 1

            print(f"You are right , your current score is {score}")
        else:
            game_continued = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()