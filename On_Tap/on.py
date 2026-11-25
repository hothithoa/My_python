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
# def sap_xep_thu_cong():
#     n = int(input("Bạn muốn nhập bao nhiêu nhân viên? "))
#     ds_luong = []
    
#     for i in range(n):
#         luong = float(input(f"Nhập lương nhân viên thứ {i+1}: "))
#         ds_luong.append(luong)
    
#     ds_luong.sort()
#     print("Danh sách sau khi sắp xếp:", ds_luong)

# sap_xep_thu_cong()

# def xu_ly_ho_ten():
#     # Bước 1: Nhập chuỗi và chuẩn hóa
#     # .strip() để xóa khoảng trắng thừa ở 2 đầu
#     # .title() để viết hoa chữ cái đầu của mỗi từ (Ví dụ: "le xuan sang" -> "Le Xuan Sang")
#     nhap_ten = input("Nhập vào tên nhân viên: ").strip().title()
    
#     # Bước 2: Tách chuỗi thành một danh sách các từ
#     # Ví dụ: "Le Xuan Sang" -> ["Le", "Xuan", "Sang"]
#     danh_sach_tu = nhap_ten.split()
    
#     if len(danh_sach_tu) < 2:
#         print("Vui lòng nhập đầy đủ cả họ và tên!")
#         return

#     # Bước 3: Tách Tên (từ cuối cùng) và Họ lót (các từ còn lại)
#     ten = danh_sach_tu[-1]  # Lấy phần tử cuối cùng
#     ho_lot_list = danh_sach_tu[:-1] # Lấy từ đầu đến sát cuối
#     ho_lot = " ".join(ho_lot_list) # Nối các từ lại bằng khoảng trắng
    
#     # Bước 4: In kết quả theo đúng yêu cầu
#     print(f"\nKết quả xử lý:")
#     print(f"- Họ và tên lót của nhân viên là : {ho_lot}")
#     print(f"- Tên của nhân viên là : {ten}")
#     print(f"- Họ tên đầy đủ của nhân viên là : {nhap_ten}")

# # Đừng quên gọi hàm để chạy
# xu_ly_ho_ten()

# def tinh_diem_trung_binh():
#     # 1. Nhập số lượng môn học
#     while True:
#         try:
#             n = int(input("Tong so mon hoc can tinh DTB: "))
#             if n > 0: break
#             print("Số môn học phải lớn hơn 0!")
#         except ValueError:
#             print("Vui lòng nhập một số nguyên!")

#     tong_diem_he_so = 0
#     tong_he_so = 0

#     # 2. Vòng lặp nhập dữ liệu cho từng môn
#     for i in range(1, n + 1):
#         print(f"\n--- Nhập dữ liệu môn học {i} ---")
        
#         # Nhập và kiểm tra điểm số (phải từ 0 đến 10)
#         while True:
#             diem = float(input(f"Diem mon hoc {i}: "))
#             if 0 <= diem <= 10:
#                 break
#             print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10. Yêu cầu nhập lại!")

#         # Nhập và kiểm tra hệ số (1, 1.5, 2, 2.5 hoặc 3)
#         while True:
#             he_so = float(input(f"He so mon hoc {i} (1, 1.5, 2, 2.5, 3): "))
#             if he_so in [1, 1.5, 2, 2.5, 3]:
#                 break
#             print("Lỗi: Hệ số không đúng quy định. Vui lòng nhập lại!")

#         # Tích lũy giá trị
#         tong_diem_he_so += diem * he_so
#         tong_he_so += he_so

#     # 3. Tính toán kết quả cuối cùng
#     if tong_he_so > 0:
#         dtb = tong_diem_he_so / tong_he_so
#         print("\n" + "="*30)
#         print(f"So mon hoc: {n}")
#         print(f"Tong so he so: {tong_he_so}")
#         print(f"Diem trung binh cua {n} mon hoc: {round(dtb, 2)}")
#     else:
#         print("Không có dữ liệu để tính toán.")

# # Chạy hàm
# tinh_dieTrue: 

# ds = [0, 10, -5, -2, 6]
# def dem_phan_tu_am(ds):
#     dem = 0
#     for x in ds:
#         if x < 0:
#             dem += 1
# print(dem_phan_tu_am(ds))
#     return dem

# ds = [0, 10, -5, -2, 6]
# def tinh_tong_phan_tu_am(ds):
#     tong = 0
#     for x in ds:
#         if x < 0:
#             tong += x
#     print(tinh_tong_phan_tu_am(ds))
#     return tong

# ds = [10, -5, -2, 6]
# def dem_phan_tu_chan(ds):
#     dem = 0
#     for x in ds:
#         if x % 2 == 0:
#             dem += 1
#     print(dem_phan_tu_chan(ds))
#     return dem


# ds = [10, -5, -2, 6]
# def tinh_tong_phan_tu_chan(ds):
#     tong = 0
#     for x in ds:
#         if x % 2 == 0:
#             tong += x
#     return tong
# print(tinh_tong_phan_tu_chan(ds))

# ds = []
# n = int(input("Nhập số lượng phần tử: "))

# for i in range(n):
#     x = int(input(f"Nhập phần tử thứ {i+1}: "))
#     ds.append(x)

# print("Số phần tử âm:", dem_phan_tu_am(ds))
# print("Tổng phần tử âm:", tinh_tong_phan_tu_am(ds))
# print("Số phần tử chẵn:", dem_phan_tu_chan(ds))
# print("Tổng phần tử chẵn:", tinh_tong_phan_tu_chan(ds))

# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# while b!=0:
#     r = a % b
#     a = b
#     b = r
# print("USCLN là:",a) 

# n = int(input("Nhập số lượng phần tử: "))
# ds = []

# for i in range(n):
#     x = int(input(f"Nhập phần tử thứ {i+1}: "))
#     ds.append(x)

# ds.sort()

# print("Dãy sau khi sắp xếp tăng dần:", ds)

# if len(ds) >= 2:
#     print("Phần tử thứ nhất:", ds[0])
#     print("Phần tử thứ hai:", ds[1])
# else:
#     print("Dãy không đủ 2 phần tử")



# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))

# min_ab = min(a, b)
# uscln = 1

# for i in range(1, min_ab + 1):
#     if a % i == 0 and b % i == 0:
#         uscln = iZ

# print("USCLN là:", uscln)


# Tìm USCLN (giữ nguyên phần của bạn)
# while b != 0:
#     r = a % b
#     a = b
#     b = r

# print("USCLN là:", a)

# n = int(input("Nhập số lượng phần tử: "))
# ds = []

# for i in range(n):
#     x = int(input(f"Nhập phần tử thứ {i+1}: "))
#     ds.append(x)

# # Sắp xếp tăng dần KHÔNG dùng sort()
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if ds[i] > ds[j]:
#             ds[i], ds[j] = ds[j], ds[i]   # đổi chỗ

# print("Dãy sau khi sắp xếp tăng dần:", ds)

# if len(ds) >= 2:
#     print("Phần tử thứ nhất:", ds[0])
#     print("Phần tử thứ hai:", ds[1])
# else:
#     p(rint("Dãy không đủ 2 phần tử") 

# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# while b != 0:
#     r = a % b
#     a = b
#     b = r
# print("USCLN là:", a)

# n = int(input("Nhập số lượng phần tử: "))
# ds = []

# for i in range(n):
#     x = int(input(f"Nhập phần tử thứ {i+1}: "))
#     ds.append(x)
# # Sắp xếp tăng dần KHÔNG dùng sort()
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if ds[i] > ds[j]:
#             ds[i], ds[j] = ds[j], ds[i]   # đổi chỗ
# print("Dãy sau khi sắp xếp tăng dần:", ds)

# if len(ds) >= 2:
#     print("Phần tử thứ nhất:", ds[0])
#     print("Phần tử thứ hai:", ds[1])
# else:
#     print("Dãy không đủ 2 phần tử")

# f1 = f0 =1 
# fn = f (n-1) + f (n-2) ; (n>1)

# def  Fibonaci(n):
#     f=1
#     if n<2:
#         f=1
#     else:
#         f=Fibonaci(n-1) + Fibonaci(n-2)
#     return f

# n=int(input("nhập n: "))
# print(Fibonaci(n))

# def Giaithua(n):
#     gt=1
#     if n==1:
#         gt=1
#     else:
#         gt=n*Giaithua(n-1)
#     return gt

# a=int(input("nhập a: "))
# print(Giaithua(a))

# a = int(input("Nhập: "))
# for a - 1 in range (a):
#     a = a(a-1)
# print

# class SinhVien:
#     def __init__(self, ma_sv, ho_ten, dlt, dth):
#         self.ma_sv = ma_sv
#         self.ho_ten = ho_ten
#         self.dlt = dlt
#         self.dth = dth

#     # Tính tổng điểm
#     def tinh_tong_diem(self):
#         return (self.dlt + self.dth)/2

#     # Xếp loại
#     def xep_loai(self):
#         tong = self.tinh_tong_diem()
#         return "DAT" if tong >= 10 else "HONG"   # tránh lỗi font

#     # Hiển thị
#     def __str__(self):
#         tong = self.tinh_tong_diem()
#         status = self.xep_loai()
#         return f"{self.ma_sv:<10} | {self.ho_ten:<20} | {self.dlt:<5} | {self.dth:<5} | Tong: {tong:<5} | {status}"


# # ====== Chạy thử ======
# if __name__ == "__main__":
#     sv1 = SinhVien("SV001", "Nguyen Van A", 6, 8)
#     sv2 = SinhVien("SV002", "Tran Thi B", 4, 3)
#     sv3 = SinhVien("SV003", "Ho Thi Thoan", 10, 10) 

#     print(sv1)
#     print(sv2)
#     print(sv3)

# class SinhVien:
#     def __init__(self, ma_sv, ho_ten, dlt, dth):
#         self.ma_sv = ma_sv
#         self.ho_ten = ho_ten
#         self.dlt = dlt
#         self.dth = dth

#     # Tính điểm trung bình
#     def tinh_tong_diem(self):
#         return (self.dlt + self.dth) / 2

#     # Xếp loại
#     def xep_loai(self):
#         tong = self.tinh_tong_diem()
#         return "DAT" if tong >= 5 else "HONG"

#     # Hiển thị
#     def __str__(self):
#         tong = self.tinh_tong_diem()
#         status = self.xep_loai()
#         return f"{self.ma_sv:<10} | {self.ho_ten:<20} | {self.dlt:<5} | {self.dth:<5} | TB: {tong:<5.2f} | {status}"


# # ====== Nhập từ bàn phím ======
# if __name__ == "__main__":
#     danh_sach = []

#     n = int(input("Nhập số lượng sinh viên: "))

#     for i in range(n):
#         print(f"\nNhập sinh viên thứ {i+1}:")
#         ma_sv = input("Mã SV: ")
#         ho_ten = input("Họ tên: ")
#         dlt = float(input("Điểm lý thuyết: "))
#         dth = float(input("Điểm thực hành: "))

#         sv = SinhVien(ma_sv, ho_ten, dlt, dth)
#         danh_sach.append(sv)

#     print("\n===== DANH SÁCH SINH VIÊN =====")
#     for sv in danh_sach:
#         print(sv)


# class SinhVien:
#     def __init__(self, ms, hoten, dlt, dth):
#         self.ms = ms
#         self.hoten = hoten
#         self.dlt = dlt
#         self.dth = dth
#         self.dtb = (dlt + dth) / 2

# # Nhập danh sách sinh viên
# n = int(input("Nhập số lượng sinh viên: "))
# ds = []

# for i in range(n):
#     print("Sinh viên", i+1)
#     ms = input("Mã số: ")
#     hoten = input("Họ tên: ")
#     dlt = float(input("Điểm lý thuyết: "))
#     dth = float(input("Điểm thực hành: "))

#     sv = SinhVien(ms, hoten, dlt, dth)
#     ds.append(sv)

# # Xuất danh sách
# print("DANH SÁCH SINH VIÊN")
# for sv in ds:
#     print(sv.ms, sv.hoten, sv.dlt, sv.dth, sv.dtb)

# # Tìm sinh viên có điểm trung bình cao nhất
# sv_max = ds[0]
# for sv in ds:
#     if sv.dtb > sv_max.dtb:
#         sv_max = sv

# print("SINH VIÊN ĐIỂM TRUNG BÌNH CAO NHẤT")
# print(sv_max.ms, sv_max.hoten, sv_max.dtb)

# # Sắp xếp theo họ tên)
# for i in range(len(ds) - 1):
#     for j in range(len(ds) - i - 1):
#         if ds[j].hoten > ds[j+1].hoten:
#             temp = ds[j]
#             ds[j] = ds[j+1]
#             ds[j+1] = temp
# # Xuất danh sách sau khi sắp xếp
# print("SAU KHI SẮP XẾP")
# for sv in ds:
#     print(sv.ms, sv.hoten, sv.dtb)
# # In tất cả sinh viên có ĐTB cao nhất
# max_dtb = ds[0].dtb
# for sv in ds:
#     if sv.dtb > max_dtb:
#         max_dtb = sv.dtb
# print("CÁC SV ĐIỂM TRUNG BÌNH CAO NHẤT")
# for sv in ds:
#     if sv.dtb == max_dtb:
#         print(sv.ms, sv.hoten, sv.dtb)
#         f = open("sinhvien.txt", "w", encoding="utf-8")

# for sv in ds:
#     f.write(sv.ms + " " + sv.hoten + " " + str(sv.dtb) + "\n")

# f.close()


# class SinhVien:
#     def __init__(self, ms, hoten, dlt, dth):
#         self.ms = ms
#         self.hoten = hoten
#         self.dlt = dlt
#         self.dth = dth
#         self.dtb = (dlt + dth) / 2

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Thêm vào cuối danh sách
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     # In danh sách
#     def print_list(self):
#         temp = self.head
#         while temp:
#             sv = temp.data
#             print(sv.ms, sv.hoten, sv.dlt, sv.dth, sv.dtb)
#             temp = temp.next

#     # Tìm sinh viên có DTB cao nhất
#     def find_max(self):
#         temp = self.head
#         sv_max = temp.data

#         while temp:
#             if temp.data.dtb > sv_max.dtb:
#                 sv_max = temp.data
#             temp = temp.next
#         return sv_max

#     # Sắp xếp theo họ tên (bubble sort - đổi DATA)
#     def sort_by_name(self):
#         i = self.head
#         while i:
#             j = i.next
#             while j:
#                 if i.data.hoten > j.data.hoten:
#                     i.data, j.data = j.data, i.data
#                 j = j.next
#             i = i.next

#     # In các sinh viên có DTB cao nhất
#     def print_max_students(self):
#         max_dtb = self.head.data.dtb
#         temp = self.head

#         # tìm max
#         while temp:
#             if temp.data.dtb > max_dtb:
#                 max_dtb = temp.data.dtb
#             temp = temp.next

#         # in ra
#         print("CÁC SV ĐIỂM TRUNG BÌNH CAO NHẤT")
#         temp = self.head
#         while temp:
#             if temp.data.dtb == max_dtb:
#                 sv = temp.data
#                 print(sv.ms, sv.hoten, sv.dtb)
#             temp = temp.next

# ll = LinkedList()

# n = int(input("Nhập số lượng sinh viên: "))

# for i in range(n):
#     print("Sinh viên", i+1)
#     ms = input("Mã số: ")
#     hoten = input("Họ tên: ")
#     dlt = float(input("Điểm lý thuyết: "))
#     dth = float(input("Điểm thực hành: "))

#     sv = SinhVien(ms, hoten, dlt, dth)
#     ll.append(sv)

# print("\nDANH SÁCH SINH VIÊN")
# ll.print_list()

# # Tìm max
# sv_max = ll.find_max()
# print("\nSINH VIÊN ĐTB CAO NHẤT")
# print(sv_max.ms, sv_max.hoten, sv_max.dtb)

# # Sắp xếp
# ll.sort_by_name()
# print("\nSAU KHI SẮP XẾP")
# ll.print_list()

# # In các sv max
# ll.print_max_students()
# class SinhVien:
#     def __init__(self, ms, hoten, dlt, dth):
#         self.ms = ms
#         self.hoten = hoten
#         self.dlt = dlt
#         self.dth = dth
#         self.dtb = (dlt + dth) / 2

# # Node của danh sách liên kết
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Linked List
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Thêm vào cuối danh sách
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     # In danh sách
#     def print_list(self):
#         temp = self.head
#         while temp:
#             sv = temp.data
#             print(sv.ms, sv.hoten, sv.dlt, sv.dth, sv.dtb)
#             temp = temp.next

#     # Tìm sinh viên có DTB cao nhất
#     def find_max(self):
#         temp = self.head
#         sv_max = temp.data

#         while temp:
#             if temp.data.dtb > sv_max.dtb:
#                 sv_max = temp.data
#             temp = temp.next
#         return sv_max

#     # Sắp xếp theo họ tên (bubble sort - đổi DATA)
#     def sort_by_name(self):
#         i = self.head
#         while i:
#             j = i.next
#             while j:
#                 if i.data.hoten > j.data.hoten:
#                     i.data, j.data = j.data, i.data
#                 j = j.next
#             i = i.next

#     # In các sinh viên có DTB cao nhất
#     def print_max_students(self):
#         max_dtb = self.head.data.dtb
#         temp = self.head

#         # tìm max
#         while temp:
#             if temp.data.dtb > max_dtb:
#                 max_dtb = temp.data.dtb
#             temp = temp.next

#         # in ra
#         print("CÁC SV ĐIỂM TRUNG BÌNH CAO NHẤT")
#         temp = self.head
#         while temp:
#             if temp.data.dtb == max_dtb:
#                 sv = temp.data
#                 print(sv.ms, sv.hoten, sv.dtb)
#             temp = temp.next

# ll = LinkedList()

# n = int(input("Nhập số lượng sinh viên: "))

# for i in range(n):
#     print("Sinh viên", i+1)
#     ms = input("Mã số: ")
#     hoten = input("Họ tên: ")
#     dlt = float(input("Điểm lý thuyết: "))
#     dth = float(input("Điểm thực hành: "))

#     sv = SinhVien(ms, hoten, dlt, dth)
#     ll.append(sv)

# print("\nDANH SÁCH SINH VIÊN")
# ll.print_list()

# # Tìm max
# sv_max = ll.find_max()
# print("\nSINH VIÊN ĐTB CAO NHẤT")
# print(sv_max.ms, sv_max.hoten, sv_max.dtb)

# # Sắp xếp
# ll.sort_by_name()
# print("\nSAU KHI SẮP XẾP")
# ll.print_list()

# # In các sv max
# ll.print_max_students() 
# class SinhVien:
#     def __init__(self, mssv, hoten, lop, diem):
#         self.mssv = mssv
#         self.hoten = hoten
#         self.lop = lop
#         self.diem = diem
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Xóa phần tử đầu danh sách
#     def xoa_dau(self):
#         if self.head is None:
#             print("Danh sách rỗng, không thể xóa!")
#         else:
#             self.head = self.head.next
              
#     # Nhập danh sách sinh viên
#     def nhap_danh_sach(self, n):
#         for i in range(n):
#             print(f"Nhập sinh viên thứ {i+1}:")
#             mssv = input("MSSV: ")
#             hoten = input("Họ tên: ")
#             lop = input("Lớp: ")
#             diem = float(input("Điểm: "))

#             sv = SinhVien(mssv, hoten, lop, diem)
#             self.them_cuoi(sv)

#     # Xuất danh sách sinh viên
#     def xuat_danh_sach(self):
#         print("Danh sách sinh viên:")
#         temp = self.head
#         while temp:
#             sv = temp.data
#             print(f"MSSV: {sv.mssv}")
#             print(f"Họ tên: {sv.hoten}")
#             print(f"Lớp: {sv.lop}")
#             print(f"Điểm: {sv.diem}")
#             print("----------------------")
#             temp = temp.next


# # Chương trình chính
# if __name__ == "__main__":
#     ds = LinkedList()
#     n = int(input("Nhập số lượng sinh viên: "))
#     ds.nhap_danh_sach(n)
#     ds.xuat_danh_sach()


# class SinhVien:
#     def __init__(self, mssv, hoten, lop, diem):
#         self.mssv = mssv
#         self.hoten = hoten
#         self.lop = lop
#         self.diem = diem

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None


#     # Thêm vào đầu
#     def them_dau(self, sv):
#         new_node = Node(sv)
#         new_node.next = self.head
#         self.head = new_node

#     # Thêm vào cuối
#     def them_cuoi(self, sv):
#         new_node = Node(sv)
#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node

#     # Xóa đầu
#     def xoa_dau(self):
#         if self.head is None:
#             print("Danh sách rỗng!")
#         else:
#             self.head = self.head.next

#     # Nhập danh sách
#     def nhap_danh_sach(self, n):
#         for i in range(n):
#             print(f"Nhập sinh viên thứ {i+1}:")
#             mssv = input("MSSV: ")
#             hoten = input("Họ tên: ")
#             lop = input("Lớp: ")
#             diem = float(input("Điểm: "))

#             sv = SinhVien(mssv, hoten, lop, diem)

#       
#             self.them_cuoi(sv)

#     # Xuất danh sách
#     def xuat_danh_sach(self):
#         temp = self.head
#         while temp:
#             sv = temp.data
#             print(f"MSSV: {sv.mssv}")
#             print(f"Họ tên: {sv.hoten}")
#             print(f"Lớp: {sv.lop}")
#             print(f"Điểm: {sv.diem}")
#             print("Danh sách thứ hai")
#             temp = temp.next


# if __name__ == "__main__":
#     ds = LinkedList()
#     n = int(input("Nhập số lượng sinh viên: "))
#     ds.nhap_danh_sach(n)

#     print("\nDanh sách ban đầu:")
#     ds.xuat_danh_sach()

#     # Thêm 1 sinh viên vào đầu
#     # sv_moi = SinhVien("001", "Nguyen Van A", "CTK42", 9.0)
#     # ds.them_dau(sv_moi)

#     print("\nSau khi thêm vào đầu:")
#     ds.xuat_danh_sach()

# class SinhVien:
#     def __init__(self, mssv, hoten, lop, diem):
#         self.mssv = mssv
#         self.hoten = hoten
#         self.lop = lop
#         self.diem = diem


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def them_dau(self, sv):
#         new_node = Node(sv)
#         new_node.next = self.head
#         self.head = new_node

#     def nhap_danh_sach(self, n):
#         for i in range(n):
#             print(f"Nhập sinh viên thứ {i+1}:")
#             mssv = input("MSSV: ")
#             hoten = input("Họ tên: ")
#             lop = input("Lớp: ")
#             diem = float(input("Điểm: "))

#             sv = SinhVien(mssv, hoten, lop, diem)
#             self.them_dau(sv)   

#     def xuat_danh_sach(self):
#         print("Danh sách sinh viên:")
#         temp = self.head
#         while temp:
#             sv = temp.data
#             print(f"MSSV: {sv.mssv}")
#             print(f"Họ tên: {sv.hoten}")
#             print(f"Lớp: {sv.lop}")
#             print(f"Điểm: {sv.diem}")
#             print("Danh sách thứ hai")
#             temp = temp.next

# if __name__ == "__main__":
#     ds = LinkedList()
#     n = int(input("Nhập số lượng sinh viên: "))
#     ds.nhap_danh_sach(n)

#     print("\nDanh sách sau khi thêm vào đầu:")
#     ds.xuat_danh_sach()