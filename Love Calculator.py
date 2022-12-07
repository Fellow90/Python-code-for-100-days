#Love calculator
print("Welcome to the Love Calculator!")
first_name = input("What is your name? \n")
second_name = input("What is their name? \n")
name1 = first_name.lower()
name2 = second_name.lower()
count = 0
t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
l = name2.count("l")
o = name2.count("o")
v = name2.count("v")
s = name2.count("e")
true = t + r + u + e
love = l + o + v + s
score1 = str(true) + str(love)
score = int(score1)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")