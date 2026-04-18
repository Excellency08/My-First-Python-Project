import sys, datetime

print("python version:", sys.version)
print("Todays is:", datetime.date.today())

# check year

year = int(input("What year were you born?: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# bmi calculation

height = float(input("what is your height in m: "))
weight = float(input("what is your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi <= 18.5:
    print(f"Your BMI is, {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is, {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is, {bmi}, you are overweight.")
elif bmi <= 35:
    print(f"Your BMI is, {bmi}, you are obese.")
else:
    print(f"Your BMI is, {bmi}, you are clinically obese.")
   