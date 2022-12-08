first_row = ["😁","😁","😁"]
second_row = ["😁","😁","😁"]
third_row = ["😁","😁","😁"]
# first_row = ["A","B","C"]
# second_row = ["D","E","F"]
# third_row = ["G","H","I"]
map = [first_row,second_row,third_row] #Here map is the nested list with list as map = [row1,row2,row3]
map_row = f"{first_row}\n{second_row}\n{third_row}"
print(map_row)
choose_row = int(input("Please select the row : 1 for 1st, 2 for 2nd and 3 for 3rd "))
choose_column = int(input("Please select the column : 1 for 1st, 2 for 2nd and 3 for 3rd "))
# selected_row = map[choose_row-1] #It selects the row with the help of index postion of nested list map
# selected_row[choose_column-1] = "X" # it replace the emoji in the selected row of map with the help of selected column

map[choose_row-1][choose_column-1] = "X" # Here map[choose_row - 1] becomes the list and this line of code selects the index position of choosed column of the particular list
print(f"{first_row}\n{second_row}\n{third_row}")