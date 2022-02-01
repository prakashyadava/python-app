import random
import day7_hangman as hangman
import day7_word_list as states
# import os
# import time
# import sys
# clear = lambda: os.system('cls')


print(hangman.logo)

# chosen_word = word_list[random.randint(0,len(word_list)-1)] or we can also use
word = random.choice(states.word_list).strip()
chosen_word = word.lower()

# for i in range(0,len(chosen_word)):
#     if chosen_word[i]==guess:
#         print("Right")
#     else:
#         print("Wrong")
# or we can also use
life = 6
display = []
for i in range(0, len(chosen_word)):
    display.append("_")
while life > 0 and display.count("_") > 0:
    # sleep(0.1)
    # screen_clear()
    # clear()
    print(f"Remaining life {life}!!!")
    print(display)
    print(hangman.stages[life])
    guess = input("Guess a letter : ")
    if guess not in chosen_word:
        life = life - 1
    else:
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess


if life == 0:
    print(hangman.stages[life])
    print(f"You loose!!!,{word} is the right word")
else:
    print(f"{display}\n{word}\nScore :{life*10}\nYou won!!!")
