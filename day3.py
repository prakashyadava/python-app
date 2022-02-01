print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go?Type "+ '"left"' + " or " +'"right" : ')
if(choice1 == "left"):
    choice2 = input("You cane to a lake. There is an island in the middle of the lake. Type" + '"wait" to waot for a boat. Type' + '"swin" to swin across. : ')
    if(choice2 == "wait") :
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door do you choose ? ")
        if (choice3 =="yellow"):
            print("!!!!!!!!!!!!!!!!Congratulation , you got the treasure !!!!!!!!!!!!!!!!!!!!!")
        elif (choice3 == "blue"):
            print("You are eaten by beats \n"
                  "Game Over")
        elif (choice3 =="red"):
            print("you are burned by fire \n"
                  "Game Over")
        else:
            print("Game Over")
    else:
        print("You are attacked by trout \n"
              "Game Over")
else:
    print("You are fallen into a hole \n"
          "Game Over")