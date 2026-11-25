list1 = [1, 4, 2, 3, 8, 4, 5, 9] 
list2 = [4, 10, 5, 7, 3, 3, 2, 1] 
for i in range (len(list1)): 
    if list2[i] == 1: 
        break 
    elif (list2[i] %2 == 1): 
     list1[i] = list2[i] 
print(list1) 
list1 = list1 + list2 
print(list1) 