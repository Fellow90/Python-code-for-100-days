# import random
# import string
# letters = list(string.ascii_letters)
# characters = ["!","#","$","%","&","*","+","(",")"]
# digits= list(string.digits)
# print("Welcome to the password generator!!")
# letter_key = int(input("How many letters you want on your password? "))
# characters_key = int(input("How many  you want on your password? "))
#
# digit_key = int(input("How many digits you want on your password? "))
#
# pwletter = []
#
# for i in range(letter_key):
#     pwletter.append(random.choice(letters))
# print(pwletter)
# first="".join(pwletter)
# pwdigit = []
#
# for j in range(digit_key):
#     pwdigit.append(random.choice(digits))
#
# print(pwdigit)
# second="".join(pwdigit)
#
# pwcharacter = []
#
# for k in range(characters_key):
#     pwcharacter.append(random.choice(characters))
#
# print(pwcharacter)
#
# third = "".join(pwcharacter)
#
# password = first+second+third
# print(password)

import random
import string
letters = list(string.ascii_letters)
characters = ["!","#","$","%","&","*","+","(",")"]
digits= list(string.digits)
print("Welcome to the password generator!!")
letter_key = int(input("How many letters you want on your password? "))
characters_key = int(input("How many  you want on your password? "))

digit_key = int(input("How many digits you want on your password? "))

password = ""

for i in range(1,letter_key+1):
    randomletter = random.choice(letters)
    password+= randomletter

# print(password)
for i in range(1,digit_key+1):
    randomdigit = random.choice(digits)
    password+= randomdigit

# print(password)
for i in range(1,characters_key+1):
    randomletter = random.choice(letters)
    password+= randomletter

# print(password)

### to shuffle the password which is in form of string, we use "".join(random.sample(password, len(password)))
new_password = ''.join(random.sample(password, len(password)))
print(new_password)

#     pwletter.append(random.choice(letters))
# print(pwletter)
# first="".join(pwletter)
# pwdigit = []
#
# for j in range(digit_key):
#     pwdigit.append(random.choice(digits))
#
# print(pwdigit)
# second="".join(pwdigit)
#
# pwcharacter = []
#
# for k in range(characters_key):
#     pwcharacter.append(random.choice(characters))
#
# print(pwcharacter)
#
# third = "".join(pwcharacter)
#
# password = first+second+third
# print(password)