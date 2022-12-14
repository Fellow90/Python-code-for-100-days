# for i in range(1,10,3):
#     print(i)
#
# total = 0
# for i in range(1,51,1):
#     total+=i
# print(total)

##using total - odd
# all_total = 0
# for i in range(1,101,1):
#     print(i)
#     all_total += i
# odd_total = 0
# for n in range(1,100,2):
#     print(n)
#     odd_total+= n
# print(all_total-odd_total)


##filtering even numbers
total = 0
for i in range(1,101,1):
    if i%2==0:
        total+=i
print(total)