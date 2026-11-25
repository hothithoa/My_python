import random

number = random.randint(1, 100)
guess = 0

print("Máy đã chọn một số từ 1 đến 100.")

while guess != number:
    guess = int(input("Nhập số bạn đoán: "))

    if guess < number:
        print("Số bạn đoán nhỏ hơn!")
    elif guess > number:
        print("Số bạn đoán lớn hơn!")
    else:
        print("Chúc mừng! Bạn đã đoán đúng")