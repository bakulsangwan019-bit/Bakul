list = [2, 3, 5, 5 , 6, 7,8]
list2 = []

for c in list:
    if c not in list2:
        list2.append(c)
print(list2)