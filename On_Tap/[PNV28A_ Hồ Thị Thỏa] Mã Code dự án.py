
# --- ĐỊNH NGHĨA CÁC HÀM TRƯỚC ---

def Nhap_lich():
    try:
        thang = int(input("Nhập tháng (1-12): "))
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            print(f"Tháng {thang} có 31 ngày.")
        elif thang in [4, 6, 9, 11]:
            print(f"Tháng {thang} có 30 ngày.")
        elif thang == 2:
            nam = int(input("Nhập năm: "))
            if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
                print(f"Tháng 2 năm {nam} có 29 ngày (năm nhuận).")
            else:
                print(f"Tháng 2 năm {nam} có 28 ngày.")
        else:
            print("Tháng không hợp lệ!")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên!")

def tinh_luong():
    try:
        gio_lam = float(input("Nhập số giờ làm: "))
        luong_gio = float(input("Nhập lương mỗi giờ: "))
        if gio_lam <= 40:
            tong_luong = gio_lam * luong_gio
        else:
            tong_luong = (40 * luong_gio) + ((gio_lam - 40) * luong_gio * 1.5)
        print(f"Tổng tiền lương là: {tong_luong:,.0f} VND")
    except ValueError:
        print("Lỗi: Vui lòng nhập số thực!")

def Xem_luong():
    try:
        n = int(input("Nhập số lượng nhân viên: ")) 
        ds_luong = []
        for i in range(n):
            luong = float(input(f"Nhập lương nhân viên {i+1}: "))
            ds_luong.append(luong)
        ds_luong.sort()
        print("Danh sách lương đã sắp xếp tăng dần:", ds_luong)
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không hợp lệ!")

def thong_tin_nhan_vien():
    while True:
        raw_input = input("Nhập họ tên nhân viên: ").strip()
        cac_tu = raw_input.split()
        # Kiểm tra chỉ chứa chữ cái và có ít nhất 2 từ
        if len(cac_tu) >= 2 and all(tu.replace(" ","").isalpha() for tu in cac_tu):
            break
        print("Vui lòng nhập đầy đủ họ tên (chỉ chứa chữ cái và ít nhất 2 từ)!")
    
    full_name = " ".join(cac_tu).title()
    last_space = full_name.rfind(" ")
    ho_lot = full_name[:last_space]
    ten = full_name[last_space+1:]

    print(f"1. Họ và tên lót: {ho_lot}")
    print(f"2. Tên nhân viên: {ten}")
    print(f"-> Họ tên đầy đủ: {full_name}")

def tinh_diem_hoc_sinh(): 
    try:
        n = int(input("Tổng số môn học cần tính ĐTB: "))
        tong_diem_he_so = 0
        tong_he_so = 0
        
        for i in range(n):
            while True:
                diem = float(input(f"Điểm môn học {i+1}: "))
                if 0 <= diem <= 10:
                    break
                print("Điểm không hợp lệ! Vui lòng nhập lại (0.0 - 10.0).")
            
            he_so = float(input(f"Hệ số môn học {i+1} (1, 1.5, 2, 2.5 hoặc 3): "))
            tong_diem_he_so += diem * he_so
            tong_he_so += he_so
            
        if tong_he_so == 0:
            print("Không thể tính toán do tổng hệ số bằng 0.")
            return

        dtb = tong_diem_he_so / tong_he_so
        print("-" * 20)
        print(f"Số môn học: {n}")
        print(f"Tổng số hệ số: {tong_he_so}")
        print(f"Điểm trung bình của {n} môn học: {dtb:.2f}")
    except (ValueError, ZeroDivisionError):
        print("Lỗi: Dữ liệu nhập không hợp lệ!")

# --- PHẦN LỰA CHỌN (MAIN LOOP) ---

while True:
    # Giao diện tiêu đề
    print("\n" + "\t"*2 + "*"*43)
    print("\t"*2 + "****** Chuong Trinh Hoc Thong Minh *******")
    print("\t"*2 + "*"*43)
    
    # Giao diện MENU
    print("\t"+"-"*72)
    print("\t"+"|"+"="*32, end="MENU"+"="*33+"|"+"\n")
    print("\t"+"-"*72)
    print("\t"+"_"*72)
    print("\t"+"|", "Xin vui lòng chọn:","\t"*7+"|")
    print("\t"+"|", "1. Xem lịch","\t"*8+"|")
    print("\t"+"|", "2. Tính lương","\t"*7+"|")
    print("\t"+"|", "3. Xem lương","\t"*8+"|")
    print("\t"+"|", "4. Xem thông tin nhân viên","\t"*6+"|")
    print("\t"+"|", "5. Tính điểm của học sinh","\t"*6+"|") 
    print("\t"+"|", "6. Thoát chương trình","\t"*6+"|")
    print("\t"+"|"+"\t"*9+"|")
    print("\t"+"|"+"\t"*9+"|")
    print("\t"+"|"+"_"*70+"|")

    chon = input("Nhập lựa chọn của bạn (1-6): ")

    if chon == '1':
        Nhap_lich()
    elif chon == '2':
        tinh_luong()
    elif chon == '3':
        Xem_luong()
    elif chon == '4':
        thong_tin_nhan_vien()
    elif chon == '5':
        tinh_diem_hoc_sinh()
    elif chon == '6':
        print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")

    input("Nhấn Enter để quay lại Menu...")