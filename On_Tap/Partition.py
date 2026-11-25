def partition(arr, l, r):
    pi = arr[l]      
    i = l + 1
    j = r

    while True:
        while i <= j and arr[j] >= pi:
            j -= 1

        while i <= j and arr[i] <= pi:
            i += 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi - 1)
        quickSort(arr, pi + 1, end)


n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(x)

print("Mảng ban đầu:", arr)

quickSort(arr, 0, n - 1)

print("Mảng sau khi sắp xếp:", arr)


