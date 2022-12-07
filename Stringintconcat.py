name = input("Enter your name: ")
print("Your name is : ",name)
messages = len(name)
print(type(messages))
#Here the value of messages has integer data type
message = str(messages)
print(type(message))
#so to convert int to string, we use the str() function and finally we concatenate int and string
print("Your name has "+message+' characters.')

naam = input("Enter your girlfriend name:")
age = int(input("Enter her age:"))
ismale = False
print("So, the thing I know about your girlfriend is : \n She is Mrs. ", naam , " of ",age, "years old and it is ",ismale," that she is male")
print(f"The details is : {naam},{age},{ismale}")

