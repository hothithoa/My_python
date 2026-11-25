a = list(map(int, input("Nhập các số: ").split()))
chan = le = 0

for x in a:
    if x % 2 == 0:
        chan += 1
    else:
        le += 1

print("Số chẵn:", chan)
print("Số lẻ:", le)