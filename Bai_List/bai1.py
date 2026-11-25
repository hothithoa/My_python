
a = [2, 4, 6, 8]
b = [1, 3, 5, 7]

for i in range(len(a)):
    if b[i] == 5:
        break
    if b[i] % 2 == 1:
        a[i] = b[i]
        print(a)
        