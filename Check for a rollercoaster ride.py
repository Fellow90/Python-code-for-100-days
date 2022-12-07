# #ride the rollercoaster if your height is equal to or greater than 120 cm
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age"))
    if age < 12:
        print("You should pay 5$ for the ticket")
    elif age <= 18:
        print("You should pay 7$ for the ticket")
    else:
        print("You should pay 12$ for the ticket")
else:
    print("Sorry! Please grow up for the reason")