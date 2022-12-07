# #bmi calculator with interpretation of bmi
mass = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = round(mass/(height*height),2)
if bmi < 18:
    print("You are underweight:")
elif bmi <25:
    print("You are normal weight:")
elif bmi < 30:
    print("You are overweight:")
elif bmi < 35:
    print("You are obese:")
else:
    print("You are clinically above:")
print(f"Your BMI is:",bmi)
