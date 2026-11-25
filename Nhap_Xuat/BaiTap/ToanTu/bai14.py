luong_co_ban = float(input("Nhập lương cơ bản: "))
bao_hiem = float(input("Nhập % bảo hiểm: "))

luong_thuc_nhan = luong_co_ban * (1 - bao_hiem / 100)

print("Lương thực nhận:", luong_thuc_nhan)