
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

for i in range(len(x)):
    if y[i] < 3:
        continue
    x[i] = y[i]
    print(x)
