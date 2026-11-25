def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


arr = [2, 4, 8, 9, 10, 15]

x = 10

result = binary_search(arr, x)

if result != -1:
    print("Tìm thấy tại vị trí:", result)
else:
    print("Không tìm thấy")