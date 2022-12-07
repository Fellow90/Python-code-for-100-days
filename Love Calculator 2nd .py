#Love Calculator revised
print("Welcome to the love calculator")
name1 = input("Enter the first name")
name2 = input("Enter the second name")
name3 = name1 + name2
name = name3.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
first_digit = t+r+u+e
second_digit = l+o+v+e
score = int(str(first_digit) + str(second_digit))
if score < 10 or score > 90:
    print(f"Your score is {score}, you are like coke and mentos.")
elif score >=40 and score <= 50:
    print(f"Your score is {score}, you are better when you are together.")
else:
    print(f"Your score is {score}.")