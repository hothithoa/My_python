gio = int(input("Nhap gio (0-23): "))

if 5 <= gio <= 11:
    print("Buoi sang")
elif 12 <= gio <= 17:
    print("Buoi chieu")
elif 0 <= gio <= 23:
    print("Buoi toi")
else:
    print("Gio khong hop le")
