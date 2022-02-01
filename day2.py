#bill tip calculator
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
no_of_people = int(input("How many people to split the bill? "))
total_bill += (total_bill*(tip/100))
one_person_bill = total_bill/no_of_people
print(f"Each person should pay: ${round(one_person_bill,2)}")
