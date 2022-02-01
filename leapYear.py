year = int(input("which year do you want to check : "))

if year % 4==0:
    if (year % 4 ==0 and year % 100 !=0) :
        print(f"{year} is leap year")
    elif (year % 4 ==0 and year % 100 ==0 and year%400 ==0) :
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

else:
    print(f"{year} is not leap year")
