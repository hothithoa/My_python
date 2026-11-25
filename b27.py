n = int(input("Nhập số cần kiểm tra: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Đây là số Palindrome")
else:
    print("Đây không phải là số Palindrome")