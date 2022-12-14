import random
import string
letters = list(string.ascii_letters)
characters = ["!","#","$","%","&","*","+","(",")"]
digits= list(string.digits)
print("Welcome to the password generator!!")
letter_key = int(input("How many letters you want on your password? "))
characters_key = int(input("How many  you want on your password? "))

digit_key = int(input("How many digits you want on your password? "))

pwletter = []

for i in range(letter_key):
    pwletter.append(random.choice(letters))
print(pwletter)
first="".join(pwletter)
pwdigit = []

for j in range(digit_key):
    pwdigit.append(random.choice(digits))

print(pwdigit)
second="".join(pwdigit)

pwcharacter = []

for k in range(characters_key):
    pwcharacter.append(random.choice(characters))

print(pwcharacter)

third = "".join(pwcharacter)

password = first+second+third
print(password)