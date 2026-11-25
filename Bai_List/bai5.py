a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

for i in range(len(a)):
    if b[i] % 4 == 0:
        continue
    a[i] = a[i] + b[i]

print(a)