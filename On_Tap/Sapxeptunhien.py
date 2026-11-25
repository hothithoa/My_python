def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = []
n = int(input("Số lượng phần tử: "))

for i in range(n):
    arr.append(int(input(f"Nhập số thứ {i+1}: ")))

bubbleSort(arr)

print("Mảng sau khi sắp xếp tăng dần:", arr)