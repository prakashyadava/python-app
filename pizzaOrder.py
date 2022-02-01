print("Welcome to Pizza Deliveries ")
print(f"********************************************\n"
      " Price list                                \n"
      " Small pizza :                         $15 \n"
      " Medium pizza :                        $20 \n"
      " Large pizza:                          $25 \n"
      " Pepperoni for small pizza :           $2  \n"
      " Pepperoni for medium or large pizza : $3  \n"
      " Extra chesse for any size of pizza:   $1  \n"
      "*********************************************")
size = input("What size of Pizza do you want ? S,M or L : ")
add_pepperoni = input("Do you want Pepperoni? Y or N : ")
extra_chesse = input("Do you want extra chesse?Y or N: ")
price = 0
if size=='S':
      price += 15
      if add_pepperoni =='Y':
            price +=2
      if extra_chesse =='Y':
            price +=1
      print(f"Your final bill is ${price} ")
elif size=='M':
      price += 20
      if add_pepperoni =='Y':
            price +=3
      if extra_chesse =='Y':
            price +=1
      print(f"Your final bill is ${price} ")
elif size=='L':
      price += 25
      if add_pepperoni =='Y':
            price +=3
      if extra_chesse =='Y':
            price +=1
      print(f"Your final bill is ${price} ")



