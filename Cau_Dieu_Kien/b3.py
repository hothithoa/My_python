so_thu_nhat = float(input("Nhap so a: "))
so_thu_hai = float(input("Nhap so b: "))
so_thu_ba = float(input("Nhap so c: "))

if so_thu_nhat >= so_thu_hai and so_thu_nhat >= so_thu_ba:
    print("So lon nhat la:", so_thu_nhat)
elif so_thu_hai >= so_thu_nhat and so_thu_hai >= so_thu_ba:
    print("So lon nhat la:", so_thu_hai)
else:
    print("So lon nhat la:", so_thu_ba)