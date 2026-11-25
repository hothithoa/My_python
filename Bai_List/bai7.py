a = [2, 4, 6, 8]
b = [3, 6, 9, 12]

for i in range(len(a)):
    if b[i] % 3 != 0:
        continue
    if b[i] > 10:
        break
    a[i] = b[i]

print(a)
