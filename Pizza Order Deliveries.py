#pizza order deliveries
print("Welcome to the pizza order delivery program!")
cost = 0
size = input("What size of pizza do you want to order? S for small, M for medium and L for large!!")
add_pepperoni = input("Do you want pepperoni? Y for yes and N for no!!")
extra_cheese= input("Do you want extra cheese? Y for yes and N for no!!")
if size == "S":
    cost += 15
elif size == "M":
    cost += 20
elif size == "L":
    cost += 25
else:
    print("Enter the valid size as mentioned:")
if add_pepperoni == "Y":
    if size=="S":
        cost += 2
    else:
        cost += 3
if extra_cheese == "Y":
    cost += 1
print(f"Please pay ${cost} for your ordered pizza!!")