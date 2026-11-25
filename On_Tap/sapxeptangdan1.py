mang = []
sl = int(input("Nhap so luong phan tu: "))
for i in range(sl):
    n = int(input("Nhap phan tu: "))
    mang.append(n)
print('Cac phan tu trong mang: ', mang)

mang.sort()
print("Mang sau khi sap xep: ", mang)

x = 10

dau = 0
cuoi = len(mang)-1
giua = 0
while dau <= cuoi:
    giua = (dau + cuoi)//2
    if mang[giua] == x:
        print("Tim thay x o vi tri ", giua)
        break
    elif mang[giua] < x:
        dau = giua + 1
    else:
        cuoi = giua -1
else:
    print("Khong tim thay x")