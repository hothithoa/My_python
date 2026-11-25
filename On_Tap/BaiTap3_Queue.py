#bai 3
queue = []
n = int(input("Nhập số lượng sinh viên: "))


for i in range(n):
    print(f"\nSinh viên {i+1}:")
    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))


    queue.append((ma, ten, diem))


print("\nDanh sách sinh viên (theo thứ tự nhập):")


while queue:
    sv = queue.pop(0)
    print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}")

Q = [None] * 100
front = 0
rear = -1


n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):
    print(f"\nSinh viên {i+1}:")

    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))

    rear += 1
    Q[rear] = (ma, ten, diem)

print("\nDanh sách sinh viên (theo thứ tự nhập):")

while front <= rear:
    sv = Q[front]
    print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}")
    front += 1