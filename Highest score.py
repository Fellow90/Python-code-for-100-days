# students_score= input("Enter the list of students score separated by a whitespace:").split(" ")
# for i in range(0, len(students_score)):
#     students_score[i] = int(students_score[i])
# print(students_score)
# highest = 0
# for score in students_score:
#     if score > highest:
#         highest = score
#
# print(highest)

#print the lowest score
student_score = input("Enter the scores obtained by the students separated by the comma: ").split(",")
for i in range(0, len(student_score)):
    student_score[i] = int(student_score[i])

least = student_score[0]

for score in student_score:
    if least>score:
        least = score
print(least)
