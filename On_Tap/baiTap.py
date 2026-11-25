class SinhVien:
    def __init__(self, maSo, hoTen, ngaySinh, diem):
        self.maSo = maSo
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diem = diem

    def __str__(self):
        return f"{self.maSo} | {self.hoTen} | {self.ngaySinh} | {self.diem}"
    
# ham nhap danh sach
def nhap_danh_sach():
    ds = []
    n = int(input("Nhap so luong sinh vien: "))

    for i in range(n):
        print(f"\nNhap sinh vien thu {i+1}:")
        maSo = input("Ma so: ")
        hoTen = input("Ho ten: ")
        ngaySinh = input("Ngay sinh: ")
        diem = float(input("Diem: "))

        sv = SinhVien(maSo, hoTen, ngaySinh, diem)
        ds.append(sv)

    return ds

def xuat(ds):
    for sv in ds:
        print(sv)
    print()

# selection sort tang dan
def selection_sort_tang(ds):
    n = len(ds)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if ds[j].diem < ds[min_index].diem:
                min_index = j
        ds[i], ds[min_index] = ds[min_index], ds[i]

# selection sort giam dan
def selection_sort_giam(ds):
    n = len(ds)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if ds[j].diem > ds[max_index].diem:
                max_index = j
        ds[i], ds[max_index] = ds[max_index], ds[i]

# insert sort tang dan
def insertion_sort_tang(ds):
    n = len(ds)
    for i in range(1, n):
        key = ds[i]
        j = i - 1
        while j >= 0 and ds[j].diem > key.diem:
            ds[j + 1] = ds[j]
            j -= 1
        ds[j + 1] = key

# insert sort giam dan
def insertion_sort_giam(ds):
    n = len(ds)
    for i in range(1, n):
        key = ds[i]
        j = i - 1
        while j >= 0 and ds[j].diem < key.diem:
            ds[j + 1] = ds[j]
            j -= 1
        ds[j + 1] = key


# ham xuat
ds = nhap_danh_sach()
print("\nDanh sach ban dau:")
xuat(ds)


# Selection sort tăng
selection_sort_tang(ds)
print("Selection Sort tang dan:")
xuat(ds)


# Selection sort giảm 
selection_sort_giam(ds)
print("Selection Sort giam dan:")
xuat(ds)


# Insertion sort tăng
insertion_sort_tang(ds)
print("Insertion Sort tang dan:")
xuat(ds)

