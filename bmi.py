height = float(input("Enter your height in meters: "))
mass = int(input("Enter your weight in kilogram: "))
exact_bmi = mass/height**2
#"{:.nf}".format(variable) round off the given variable to nth significant figures
bmi = "{:.3f}".format(exact_bmi)
print("So your bmi is:",bmi)

# print(25//3) prints the integer value of 25/3