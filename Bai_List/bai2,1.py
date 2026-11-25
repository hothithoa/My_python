numbers = []

while True:
    n = int(input("Nhập số: "))
    if n < 0:
        break
    numbers.append(n)
    print("Danh sách đã nhập:", numbers)