list1 = ['Киви', 'Яблоко', 'Виноград', 'Груша']
list2 = ['Яблоко', 'Банан', 'Персик', 'Виноград']
new_list = list (set (list1) & set (list2))
print(new_list)