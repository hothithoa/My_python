numbers = []

while True:
    n = int(input("Nhập số: "))
    if n < 0:
        break
    numbers.append(n)
    tong = sum(numbers)
print("Tổng các số:", tong)