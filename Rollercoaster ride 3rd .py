#ride the rollercoaster if your height is equal to or greater than 120 cm and the charge is free if your age is between 45-55
print("Welcome to the Rollercoaster!!")
height = int(input("Enter your height in cm."))
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age."))
    bill = 0
    if age<=12:
        bill += 5
    elif age <= 18:
        bill+=7
    elif age >= 45 and age <=55:
        bill+=0
        print("Congratulations!! You are under our special age category. You dont need to pay the fee!!")
    else:
        bill += 12
    want_photos = input("Do you want to click photos and videos? Y or N")
    if want_photos == "Y":
        bill +=3
    print(f"Please pay ${bill} for the ticket!!")
else:
    print("Sorry! You are smaller than the average height! Cant let you go!!")
