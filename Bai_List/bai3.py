a = [10, 20, 30, 40]
b = [1, 2, 3, 4]

for i in range(len(a)):
    if b[i] == 3:
        pass
    else:
        a[i] = a[i] + b[i]

print(a)