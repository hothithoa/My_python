# students = []

# n = int(input("Nhập số lượng sinh viên: "))

# for i in range(n):

#     print(f"\nSinh viên {i+1}")

#     ma = input("Mã SV: ")
#     ten = input("Tên SV: ")
#     diem = float(input("Điểm ĐTB: "))

#     students.append((ma, ten, diem))

# print("\n===== DANH SÁCH SINH VIÊN =====")

# for i in range(len(students)):
#     print(f"Mã: {students[i][0]}, Tên: {students[i][1]}, ĐTB: {students[i][2]}")

# min_diem = students[0][2]

# for i in range(1, len(students)):

#     if students[i][2] < min_diem:
#         min_diem = students[i][2]


# print("\n===== SINH VIÊN CÓ ĐTB NHỎ NHẤT =====")

# for i in range(len(students)):

#     if students[i][2] == min_diem:

#         print(f"Vị trí: {i}")
#         print(f"Mã: {students[i][0]}")
#         print(f"Tên: {students[i][1]}")
#         print(f"ĐTB: {students[i][2]}")

# max_diem = students[0][2]

# for i in range(1, len(students)):

#     if students[i][2] > max_diem:
#         max_diem = students[i][2]


# print("\n===== SINH VIÊN CÓ ĐTB LỚN NHẤT =====")

# for i in range(len(students)):

#     if students[i][2] == max_diem:

#         print(f"Vị trí: {i}")
#         print(f"Mã: {students[i][0]}")
#         print(f"Tên: {students[i][1]}")
#         print(f"ĐTB: {students[i][2]}")


# x = float(input("\nNhập giá trị ĐTB cần tìm: "))

# found = False

# print("\n===== KẾT QUẢ TÌM KIẾM =====")

# for i in range(len(students)):

#     if students[i][2] == x:

#         print(f"Vị trí: {i}")
#         print(f"Mã: {students[i][0]}")
#         print(f"Tên: {students[i][1]}")
#         print(f"ĐTB: {students[i][2]}")

#         found = True


# if not found:
#     print("Không tìm thấy sinh viên có ĐTB =", x)




class SinhVien:

    def __init__(self, maSo, hoTen, ngaySinh, diem):
        self.maSo = maSo
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diem = float(diem)

    def __str__(self):
        return f"{self.maSo} | {self.hoTen} | {self.ngaySinh} | {self.diem}"

# HAM NHAP DANH SACH
def nhap_danh_sach():

    ds = []
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        print(f"\nNhap sinh vien thu {i+1}:")

        maSo = input("Ma so: ")
        hoTen = input("Ho ten: ")
        ngaySinh = input("Ngay sinh: ")
        diem = float(input("Diem trung binh: "))

        sv = SinhVien(maSo, hoTen, ngaySinh, diem)

        ds.append(sv)

    return ds

# HAM XUAT DANH SACH
def xuat(ds):

    print("\nDANH SACH SINH VIEN:\n")

    for sv in ds:
        print(sv)

    print()

# SAP XEP TANG DAN THEO DIEM

def sap_xep(ds):

    for i in range(len(ds) - 1):

        for j in range(len(ds) - 1 - i):

            if ds[j].diem > ds[j + 1].diem:

                temp = ds[j]
                ds[j] = ds[j + 1]
                ds[j + 1] = temp

# TIM KIEM NHI PHAN
def tim_nhi_phan(ds, x):

    left = 0
    right = len(ds) - 1

    while left <= right:

        mid = (left + right) // 2

        if ds[mid].diem == x:

            return mid

        elif ds[mid].diem < x:

            left = mid + 1

        else:

            right = mid - 1

    return -1

# CHUONG TRINH CHINH

ds = nhap_danh_sach()

# Sap xep danh sach
sap_xep(ds)

print("\nDanh sach sau khi sap xep:")
xuat(ds)

# TIM DTB NHO NHAT

min_dtb = ds[0].diem

vi_tri_min = tim_nhi_phan(ds, min_dtb)

print("Diem trung binh nho nhat:", min_dtb)
print("Vi tri xuat hien:", vi_tri_min)
print(ds[vi_tri_min])

# TIM DTB LON NHAT

max_dtb = ds[0].diem

for sv in ds:

    if sv.diem > max_dtb:

        max_dtb = sv.diem

vi_tri_max = tim_nhi_phan(ds, max_dtb)

print("\nDiem trung binh lon nhat:", max_dtb)
print("Vi tri xuat hien:", vi_tri_max)
print(ds[vi_tri_max])

x = float(input("\nNhap diem trung binh can tim: "))

vi_tri_x = tim_nhi_phan(ds, x)

if vi_tri_x != -1:

    print(f"\nTim thay DTB = {x}")
    print("Vi tri xuat hien:", vi_tri_x)
    print(ds[vi_tri_x])

else:

    print(f"\nKhong tim thay DTB = {x}")