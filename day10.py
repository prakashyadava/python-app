def calculator(num1,num2,op):
    if op=='+':
        return num1 + num2
    elif op=='-':
        return num1 - num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2
    else:
        print("Invalid operation!!")
        calculator(num1,num2,input("Enter valid operartion"))

num1 = float(input("What's the first number: "))
print("+\n-\n*\n/")
op = input("Pick an operation : ")
next = True
while next:
    num2 = float(input("What's the second number : "))
    ans = calculator(num1,num2,op)
    print(f"{num1} {op} {num2} = {ans}")
    ask = input(f"Type 'y' to continue calculating with {ans}, or Type 'n' for exit: " )

    if ask=='y':
        op = input("Pick an operation : ")
        num1 = ans
    else:
        next = False