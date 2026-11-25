x = [3, 6, 9, 12]
y = [1, 2, 3, 4]

for i in range(len(x)):
    if y[i] == 3:
        x[i] = x[i] * 2
    elif y[i] == 4:
        break
    else:
        continue

print(x)
