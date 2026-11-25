x = [0, 1, 2, 3, 4]
y = [5, 4, 3, 2, 1]

for i in range(len(x)):
    if x[i] == y[i]:
        pass
    elif x[i] > y[i]:
        x[i] = 0
    else:
        x[i] = y[i]

print(x)
