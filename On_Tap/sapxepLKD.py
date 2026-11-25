import copy

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def nhap_mang():
    arr = []
    n = int(input("Số lượng phần tử: "))
    for i in range(n):
        arr.append(int(input(f"Nhập số thứ {i+1}: ")))
    return arr 

class SinhVien:
    def __init__(self, maSo, hoTen, ngaySinh, diem):
        self.maSo = maSo
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diem = diem

    def __str__(self):
        return f"{self.maSo} | {self.hoTen} | {self.ngaySinh} | {self.diem}"

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"Nhập sinh viên thứ {i+1}:")
        maSo = input("Mã số: ")
        hoTen = input("Họ tên: ")
        ngaySinh = input("Ngày sinh: ")
        diem = float(input("Điểm: "))
        ds.append(SinhVien(maSo, hoTen, ngaySinh, diem))
    return ds

def xuat(ds):
    for sv in ds:
        print(sv)
    print()


def selection_sort_tang(ds):
    n = len(ds)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if ds[j].diem < ds[min_index].diem:
                min_index = j
        ds[i], ds[min_index] = ds[min_index], ds[i]

def selection_sort_giam(ds):
    n = len(ds)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if ds[j].diem > ds[max_index].diem:
                max_index = j
        ds[i], ds[max_index] = ds[max_index], ds[i]

def insertion_sort_tang(ds):
    for i in range(1, len(ds)):
        key = ds[i]
        j = i - 1
        while j >= 0 and ds[j].diem > key.diem:
            ds[j+1] = ds[j]
            j -= 1
        ds[j+1] = key

def insertion_sort_giam(ds):
    for i in range(1, len(ds)):
        key = ds[i]
        j = i - 1
        while j >= 0 and ds[j].diem < key.diem:
            ds[j+1] = ds[j]
            j -= 1
        ds[j+1] = key

while True:
    print("\n===== MENU =====")
    print("1. Sắp xếp mảng số nguyên (Bubble Sort)")
    print("2. Quản lý sinh viên & sắp xếp")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        arr = nhap_mang()
        bubbleSort(arr)
        print("Mảng sau khi sắp xếp tăng dần:", arr)

    elif choice == "2":
        ds = nhap_danh_sach()
        print("\nDanh sách ban đầu:")
        xuat(ds)

        
        ds1 = copy.deepcopy(ds)
        selection_sort_tang(ds1)
        print("Selection Sort tăng dần:")
        xuat(ds1)

        ds2 = copy.deepcopy(ds)
        selection_sort_giam(ds2)
        print("Selection Sort giảm dần:")
        xuat(ds2)

        ds3 = copy.deepcopy(ds)
        insertion_sort_tang(ds3)
        print("Insertion Sort tăng dần:")
        xuat(ds3)

        ds4 = copy.deepcopy(ds)
        insertion_sort_giam(ds4)
        print("Insertion Sort giảm dần:")
        xuat(ds4)

    elif choice == "0":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ!")