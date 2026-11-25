list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

for i in range(len(list1)):
    if list1[i] + list2[i] > 6:
        list1[i] = 0
    else:
        pass

print(list1)
