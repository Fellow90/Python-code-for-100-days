#switch the values stored in two different variables

first_storage = input("Enter the first value:")
second_storage = input("Enter the second value:")
temp_storage = first_storage
first_storage = second_storage
second_storage = temp_storage
print("The value of first storage is :", first_storage)
print("The value of second storage is:", second_storage)