students = []

n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):

    print(f"\nSinh viên {i+1}")

    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))

    students.append((ma, ten, diem))

students.sort(key=lambda x: x[0])

target = input("\nNhập mã sinh viên cần tìm: ")


def binary_search(data, target):

    low = 0
    high = len(data) - 1

    while low <= high:

        mid = (high + low) // 2

        if data[mid][0] < target:
            low = mid + 1

        elif data[mid][0] > target:
            high = mid - 1

        else:
            return mid

    return -1


result = binary_search(students, target)

print("\nDanh sách sinh viên sau khi sắp xếp:")

for sv in students:
    print(f"Mã: {sv[0]}, Tên: {sv[1]}, Điểm: {sv[2]}")


if result != -1:

    sv = students[result]

    print("\nTìm thấy sinh viên:")
    print(f"Mã SV: {sv[0]}")
    print(f"Tên SV: {sv[1]}")
    print(f"Điểm: {sv[2]}")

else:
    print("\nKhông tìm thấy sinh viên")