import random

print("Welcome to tic tac toe!!!")
def valid(pos,b):
    while b.count(pos)!=1:
        if pos<=9:
            print(f"try again position {pos} is already filled")
            a = int(input("Enter the position: "))
            pos = a
        else:
            print(f"try again position {pos} is not there")
            a = int(input("Enter the position: "))
            pos = a

    return pos

def check(board,who):
    if (board[0][0]==board[0][1] and board[0][1]==board[0][2]) or (board[0][0]==board[1][0] and board[1][0]==board[2][0]):
        print("*****************************************************************************************************")
        print(f"                                     {who} won                                                        ")
        print("*****************************************************************************************************")
        return 2
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) or (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        print("*****************************************************************************************************")
        print(f"                                     {who} won                                                        ")
        print("*****************************************************************************************************")
        return 2
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) or (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        print("*****************************************************************************************************")
        print(f"                                     {who} won                                                        ")
        print("*****************************************************************************************************")
        return 2
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        print("*****************************************************************************************************")
        print(f"                                     {who} won                                                        ")
        print("*****************************************************************************************************")
        return 2
    return 1

def update_board(a, board, choices):
    if a == 1:
        board[0][0] = choices
    elif a == 2:
        board[0][1] = choices
    elif a == 3:
        board[0][2] = choices
    elif a == 4:
        board[1][0] = choices
    elif a == 5:
        board[1][1] = choices
    elif a == 6:
        board[1][2] = choices
    elif a == 7:
        board[2][0] = choices
    elif a == 8:
        board[2][1] = choices
    elif a == 9:
        board[2][2] = choices
    return 0


count = 9
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [["pos1", "pos2", "pos3"], ["pos4", "pos5", "pos6"], ["pos7", "pos8", "pos9"]]
print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}")
user_won = True
outcomes =['head','tail']
user_call = input("what's your call, head or tail : ")
comp_call = random.choice(outcomes)
if user_call==comp_call:
    print("You won")

else:
    print("You loose")
    user_won = False


user_sym='👨'
com_sym ='💻'
user = True
com =  True
if user_won:
    com = False
else:

    user=False


res = 1

while count != 0  and res==1:


    if user:
        count -= 1
        print("----------------------------Your Turn----------------------------------------------------------------\n")
        pos = int((input("Enter the position: ")))
        a =valid(pos,b)
        print("\n")
        b.remove(a)
        update_board(a, board, user_sym)
        com = True
        user = False
        print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}\n")
        res = check(board, "You")


    elif com:
        count -= 1
        print("----------------------------Computer Turn------------------------------------------------------------\n")

        com_choice = random.choice(b)
        b.remove(com_choice)
        print(f"Computer choose {com_choice}\n")
        update_board(com_choice, board, com_sym)

        com = False
        user = True
        print(f"{board[0]}\n\n{board[1]}\n\n{board[2]}\n")
        res = check(board, "Com")





if res==1:
    print("*****************************************************************************************************")
    print("                                       Draw                                                          ")
    print("*****************************************************************************************************")