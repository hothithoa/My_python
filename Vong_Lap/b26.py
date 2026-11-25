n = int(input("Nhập n: "))

print("Các số Armstrong nhỏ hơn", n, "là:")

for num in range(1, n):
    temp = num
    digits = 0
    total = 0

    # Đếm số chữ số
    t = num
    while t > 0:
        digits += 1
        t //= 10

    # Tính tổng lũy thừa các chữ số
    t = num
    while t > 0:
        digit = t % 10
        total += digit ** digits
        t //= 10

    if total == num:
        print(num)