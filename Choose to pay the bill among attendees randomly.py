# Bill payees selection using random number generation entering the large number of names!!
import random
names_string = input("Give me everybody's names, separated by a whitespace. ")
names = names_string.split(" ")
print(names)
#Here str.split(" ") split the given string into components based on some sort of divider  and we choosed whitespace as the divider here but we can choose any divider and return the message in form of list . So, name is list here.
choice = len(names)
random_choice = random.randint(1,choice)
message = names[random_choice]
print(f"So, {message} is going to pay the bill!! ")

