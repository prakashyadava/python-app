import random
import day5Charactors as ch

print("Welcome to code generator program!!! ")

# print(letters)
letter = int(input("How many letters would you like in your password ? "))
symbol = int(input("How many symbol would you like ? "))
num = int(input("How many number would you like ? "))
password = []
for i in range(0,letter):
    password += ch.letters[random.randint(0,len(ch.letters)-1)]

for i in range(0,num):
    password += str(ch.numbers[random.randint(0,9)])

for i in range(0,symbol):
    password += ch.symbols[random.randint(0,len(ch.symbols)-1)]

random.shuffle(password)

final_password = ""
for char in password:
    final_password += char

print(f"Here is your password : {final_password}")



