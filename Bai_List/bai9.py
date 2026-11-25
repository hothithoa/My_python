a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

for i in range(len(a)):
    if b[i] == 4:
        break
    if a[i] % 20 == 0:
        continue
    a[i] = a[i] + b[i]

print(a)
