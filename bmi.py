height = float(input("What is your height in m ? "))
mass = int(input("What is your mass in kg? "))
bmi = mass/(height**2)
bmi = round(float(bmi),1)

if bmi<18.5 :
    print(f"Your bmi is {bmi} and you are underweight")

elif bmi<25 :
    print(f"Your bmi is {bmi} and you have a normal weight")

elif bmi<30:
    print(f"Your bmi is {bmi} and you are overweight")

elif bmi<35:
    print(f"Your bmi is {bmi} and you are obese")
else:
    print(f"Your bmi is {bmi} and you are clinically obese")
