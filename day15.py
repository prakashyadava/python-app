resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}
price_menu = {
    "espresso" : 1,
    "latte" : 2.50,
    "cappuccino" : 3
}
def format_resources():
    return f"Water : {resources['Water']}ml\nCoffee : {resources['Coffee']}g\nMilk : {resources['Milk']}ml\nMoney : ${resources['Money']}"
def check_resources(ask):
    flag2 = True
    if ask == 'espresso':
        if resources['Water']<50:
            print("Sorry there's not enough water")
            flag2 = False
        if resources['Coffee']<18:
            print("Sorry there's not enough coffee")
            flag2 = False
    elif ask == 'latte':
        if resources['Water']<200:
            print("Sorry there's not enough water")
            flag2 = False
        if resources['Coffee']<24:
            print("Sorry there's not enough coffee")
            flag2 = False
        if resources['Milk']<150:
            print("Sorry there's not enough milk")
            flag2 = False
    elif ask == 'cappuccino':
        if resources['Water']<250:
            print("Sorry there's not enough water")
            flag2 = False
        if resources['Coffee']<24:
            print("Sorry there's not enough coffee")
            flag2 = False
        if resources['Milk']<100:
            print("Sorry there's not enough milk")
            flag2 = False
    if not flag2:
        return False
def update_resources(ask):
    if ask == 'espresso':
        resources['Water'] -= 50
        resources['Coffee'] -= 18
        resources['Money'] += 1
    elif ask == 'latte':
        resources['Water'] -= 200
        resources['Coffee'] -= 24
        resources['Milk'] -= 150
        resources['Money'] += 2.50
    elif ask == 'cappuccino':
        resources['Water'] -= 250
        resources['Coffee'] -= 24
        resources['Milk'] -= 100
        resources['Money'] += 3
flag = True
def check(ask):
    print("Please insert coins.")
    quaters = int(input("How many quaters ?: "))
    dimes = int(input("How many dimes ?: "))
    nickles = int(input("How many nickles ?: "))
    pennies = int(input("How many pennies ?: "))
    total = pennies*0.01 + quaters*0.25 + dimes*0.10 + nickles*0.05
    if check_resources(ask)== False:
        print(f"Here is your money ,${total}")
    elif price_menu[ask]<= total:
        update_resources(ask)
        print(f"Enjoy your {ask}\nHere is your change ${total-price_menu[ask]}")
    else:
        print("Sorry that's not enough money!!")
while flag:
    ask = input("What would you like? (espresso/latte/cappuccino) : ")
    if ask == "report":
        print(format_resources())
    elif ask =="off":
        flag = False
        break
    else:
        check(ask)

