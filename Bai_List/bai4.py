list1 = [5, 6, 7, 8]
list2 = [2, 4, 1, 3]

for i in range(len(list1)):
    if list2[i] == 1:
        break
    list1[i] = list1[i] * list2[i]

print(list1)
