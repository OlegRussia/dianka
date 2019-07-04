list1 = [2, 4, 8, 9, 0, -4, 22, -16, -21]
new_list = [el for el in list1 if el % 3 == 0 and el >=0 and el % 4 !=0]
print(new_list)