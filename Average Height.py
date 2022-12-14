# height_of_students = input("Enter the height of students seperated by a whitespace")
# height_list = height_of_students.split(" ")
# print(f"So the height of student is listed as: {height_list}")
# total = 0
# for height in height_list:
#     float_height = float(height)
#     total+= float_height
#     average = total/len(height_list)
# new_average = round(average)
# print(f"The average height of student is : {new_average}")


#
#

height_of_students = input("Enter the height of students seperated by a whitespace")
height_list = height_of_students.split(" ")
print(f"So the height of student is listed as: {height_list}")
for i in range(0, len(height_list)):
    height_list[i] = int(height_list[i])
total = 0
for height in height_list:
    total+=height
print(f"Total height is: {total}")
no_of_students = 0
for n in height_list:
    no_of_students += 1
print(f"Total number of students in the list is: {no_of_students}")
average = round(total /no_of_students)
print(f"The average height is: {average}")




