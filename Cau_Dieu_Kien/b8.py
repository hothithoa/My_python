diem = float(input("Nhập điểm của bạn (0-10): "))
if 8.5 <= diem <= 10.0:
    print("Điểm A")
elif 7.0 <= diem <= 8.4:
    print("Điểm B")
elif 5.5 <= diem <= 6.9:
    print("Điểm C")
elif 4.0 <= diem <= 5.4:
    print("Điểm D")
else:
    print("Điểm F")