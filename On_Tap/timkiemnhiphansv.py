students = []

n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):

    print(f"\nSinh viên {i+1}")

    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))

    students.append((ma, ten, diem))

students.sort(key=lambda x: x[0])

print("\nDanh sách sinh viên sau khi sắp xếp:")

for sv in students:
    print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}")

target = input("\nNhập mã sinh viên cần tìm: ")

def binary_search(data, target):

    left = 0
    right = len(data) - 1

    while left <= right:

        middle = (left + right) // 2

        if data[middle][0] == target:
            return middle

        elif data[middle][0] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


result = binary_search(students, target)

if result != -1:

    sv = students[result]

    print("\nTìm thấy sinh viên:")
    print(f"Mã: {sv[0]}")
    print(f"Tên: {sv[1]}")
    print(f"Điểm: {sv[2]}")

else:
    print("Không tìm thấy sinh viên") 