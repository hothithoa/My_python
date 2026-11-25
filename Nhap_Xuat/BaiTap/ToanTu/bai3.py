import math
#ban_kinh_hinh_tron = int(input("Nhap so vao: "))
ban_kinh_hinh_tron = float(input("Nhập bán kính hình tròn: "))
chu_vi = 2 * math.pi * ban_kinh_hinh_tron
dien_tich = math.pi * (ban_kinh_hinh_tron ** 2)
print(f"Chu vi hình tròn: {chu_vi:.2f}")
print(f"Diện tích hình tròn: {dien_tich:.2f}")
