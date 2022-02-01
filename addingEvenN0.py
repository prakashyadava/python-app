num = input("Enter the range of number : ").split()
a = int(num[0])
b = int(num[1])
sum =0
for i in range (a,b+1):
    if i % 2 == 0 :
        sum += i

print(f"Sum of even number from {a} to {b} is {sum}")

