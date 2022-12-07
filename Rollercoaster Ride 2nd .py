#ride the rollercoaster if your height is equal to or greater than 120 cm with price variance depending upon your age and add 3$ more if you want to take photos!!
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age"))
    if age < 12:
        bill=5
        print("You should pay " +str(int(bill))+ " for the ticket")
    elif age <= 18:
        bill = 7
        print(f"You should pay {bill} for the ticket")
    else:
        bill = 12
        print("You should pay 12$ for the ticket")
    wantphoto = input("Do you want photo?yes or no")
    if wantphoto == "yes":
        bill += 3
        print(f"You should pay {bill} for the ticket")
    else:
        print(f"You should pay {bill} for the ticket")
else:
    print("Sorry! Please grow up for the reason")

