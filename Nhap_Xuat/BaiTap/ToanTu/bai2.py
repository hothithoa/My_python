# Nhập số giây và đổi sang phút + giây
tong_giay = int(input("Nhập số giây:"))
phut = tong_giay // 60
giay_con_lai = tong_giay % 60
print(f"Kết quả: {phut} phút {giay_con_lai} giây")