# Bài 1: Tính số ngày trong tháng
# def tinh_ngay_trong_thang():
#     thang = int(input("Nhập vào tháng: "))
#     if thang in [1, 3, 5, 7, 8, 10, 12]:
#         print(f"Tháng {thang} có 31 ngày.")
#     elif thang in [4, 6, 9, 11]:
#         print(f"Tháng {thang} có 30 ngày.")
#     elif thang == 2:
#         print(f"Tháng {thang} có 28 hoặc 29 ngày.")
#     else:
#         print("Tháng không hợp lệ!")
# Bài 2: Tính lương nhân viên (Tăng ca)
# def tinh_luong():
#     gio_lam = float(input("Nhập số giờ làm: "))
#     luong_gio = float(input("Nhập lương mỗi giờ: "))
#     if gio_lam > 40:
#         tong_luong = (40 * luong_gio) + ((gio_lam - 40) * luong_gio * 1.5)
#     else:
#         tong_luong = gio_lam * luong_gio
#     print(f"Tổng tiền lương: {tong_luong}")
# Bài 3: Nhập danh sách lương và sắp xếp tăng dần
# def sap_xep_luong():
#     ds_luong = list(map(float, input("Nhập danh sách lương (cách nhau bằng khoảng trắng): ").split()))
#     ds_luong.sort()
#     print("Mảng lương đã sắp xếp tăng dần:", ds_luong)
# Bài 4: Xử lý họ tên (Viết hoa chữ cái đầu và tách tên)
# def xu_ly_ho_ten():
#     ho_ten = input("Nhập vào tên nhân viên: ").title() # Viết hoa chữ cái đầu
#     parts = ho_ten.split()
#     ho_lot = " ".join(parts[:-1])
#     ten = parts[-1]
    
#     print(f"Họ và tên lót của nhân viên là: {ho_lot}")
#     print(f"Tên của nhân viên là: {ten}")
#     print(f"Họ tên đầy đủ của nhân viên là: {ho_ten}")
# Bài 5: Tính điểm trung bình (Có hệ số và kiểm tra điều kiện)
# def tinh_diem_trung_binh():
#     n = int(input("Tong so mon hoc can tinh DTB: "))
#     tong_diem_he_so = 0
#     tong_he_so = 0
# for i in range(1, n + 1):
 # Kiểm tra điểm hợp lệ
# while True:
#     diem = float(input(f"Diem mon hoc {i}: "))
#     if 0 <= diem <= 10:
#             break
#             print("Điểm không hợp lệ, vui lòng nhập lại (0-10)!")
            
#     he_so = float(input(f"He so mon hoc {i}: "))
#     tong_diem_he_so += diem * he_so
#     tong_he_so += he_so

# dtb = tong_diem_he_so / tong_he_so if tong_he_so > 0 else 0
# print("-" * 20)
# print(f"So mon hoc: {n}")
# print(f"Tong so he so: {tong_he_so}")
# print(f"Diem trung binh cua {n} mon hoc: {dtb:.1f}")

# def bai_1():
#     thang = int(input("Nhập tháng: "))
#     if thang in [1, 3, 5, 7, 8, 10, 12]: print("31 ngày")
#     elif thang == 2: print("28 hoặc 29 ngày")
#     else: print("30 ngày")

# def bai_2():
#     gio = float(input("Số giờ làm: "))
#     luong = float(input("Lương/giờ: "))
#     if gio > 40:
#         tong = (40 * luong) + ((gio - 40) * luong * 1.5)
#     else:
#         tong = gio * luong
#     print(f"Tổng lương: {tong}")

# # Menu chọn bài
# print("1. Tính ngày trong tháng")
# print("2. Tính lương")
# chon = input("Bạn muốn chạy bài mấy? (1 hoặc 2): ")

# if chon == "1":
#     bai_1()
# elif chon == "2":
#     bai_2()

# def sap_xep_luong():
#     print("--- Bài 3: Sắp xếp danh sách lương ---")
    
#     # Bước 1: Nhập chuỗi số, ví dụ: "500 200 400"
#     chuoi_nhap = input("Nhập danh sách lương (các số cách nhau bằng dấu cách): ")
    
#     # Bước 2: Chuyển chuỗi thành danh sách các số thực (float)
#     # .split() sẽ tách chuỗi dựa trên khoảng trắng
#     try:
#         ds_luong = [float(x) for x in chuoi_nhap.split()]
        
#         # Bước 3: Sắp xếp tăng dần
#         ds_luong.sort()
        
#         # Bước 4: In kết quả
#         print("Mảng lương đã được sắp xếp tăng dần:")
#         print(ds_luong)
        
#     except ValueError:
#         print("Lỗi: Vui lòng chỉ nhập số, không nhập chữ hay ký tự đặc biệt!")

# # QUAN TRỌNG: Phải có dòng này để chương trình thực thi
# sap_xep_luong() 

# def tinh_tong_le(n):
#     if n == 1:
#         return 1
#     else:
#         so_le_thu_n = 2 * n - 1
#         return so_le_thu_n + tinh_tong_le(n - 1)

# try:
#     n = int(input("Bạn muốn tính tổng của bao nhiêu số lẻ đầu tiên? "))
#     if n > 0:
#         ket_qua = tinh_tong_le(n)
#         print(f"Tổng của {n} số lẻ đầu tiên là: {ket_qua}")
#     else:
#         print("Vui lòng nhập một số nguyên dương!")
# except ValueError:
#     print("Vui lòng nhập số nguyên hợp lệ.")

# def Q(a, b):
#     # Điều kiện dừng
#     if a < b:
#         return 0
#     # Bước đệ quy
#     else:
#         return Q(a - b, b) + 1

# # Chương trình chính
# try:
#     print("--- Chương trình tính hàm đệ quy Q(a, b) ---")
#     a = int(input("Nhập số nguyên dương a: "))
#     b = int(input("Nhập số nguyên dương b: "))

#     if a > 0 and b > 0:
#         ket_qua = Q(a, b)
#         print(f"\nKết quả Q({a}, {b}) là: {ket_qua}")
#     else:
#         print("\nVui lòng nhập các số nguyên lớn hơn 0.")
# except ValueError:
#     print("\nLỗi: Bạn phải nhập vào một số nguyên.")

def find_gcd(a, b):
    # Sử dụng thuật toán Euclid đệ quy
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

# Ví dụ chạy thử:
num1 = 30
num2 = 20
print(f"USCLN của {num1} và {num2} là: {find_gcd(num1, num2)}")