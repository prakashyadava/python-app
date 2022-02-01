print("Welcome to love calculator")
name = input("Enter your name: ")
partner = input("Enter your partner name: ")
check_name = name +partner
check_name = check_name.lower()
count1 = check_name.count("t") + check_name.count("r") + check_name.count("u") + check_name.count("e")
count2 = check_name.count("l") + check_name.count("o") + check_name.count("v") + check_name.count("e")
score = str(count1) + str(count2)
score = int(score)
if (score<10) or (score>90):
    print(f"Your score is {score}%,you go together like coke and mentos")
elif (score>40) and (score<50):
    print(f"Your score is {score}%,you are alright together")
else:
    print(f"Your score is {score}%")



