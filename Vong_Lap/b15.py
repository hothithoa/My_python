a = list(map(int, input("Nhập các số: ").split()))
max_val = a[0]

for x in a:
    if x > max_val:
        max_val = x

print("Số lớn nhất là:", max_val)