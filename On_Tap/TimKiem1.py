import array as arr

arr = arr.array('i', [])

n = int(input("Nhập số phần tử: "))

for i in range(n):
    arr.append(int(input('Nhập phần tử thứ %d: ' % (i + 1))))

x = 10

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(search(arr, x)) 