def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j][3] > arr[j+1][3]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

ds = []
n = int(input("Số lượng sinh viên: "))

for i in range(n):
    print(f"\nNhập sinh viên thứ {i+1}:")
    ms = input("Mã số: ")
    ten = input("Họ tên: ")
    ns = input("Ngày sinh: ")
    diem = float(input("Điểm: "))
    
    ds.append((ms, ten, ns, diem))

print("\nDanh sách ban đầu:")
for sv in ds:
    print(sv)

bubbleSort(ds)

print("\nDanh sách sau khi sắp xếp theo điểm tăng dần:")
for sv in ds:
    print(sv)