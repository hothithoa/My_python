class SinhVien:
    def __init__(self, mssv, hoten, lop, diem):
        self.mssv = mssv
        self.hoten = hoten
        self.lop = lop
        self.diem = diem

    def hien_thi(self):
        print(f"{self.mssv} | {self.hoten} | {self.lop} | {self.diem}")


class Nut:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class DSLK:
    def __init__(self):
        self.head = None

    def them_cuoi(self, sv):
        nut_moi = Nut(sv)

        if self.head is None:
            self.head = nut_moi
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nut_moi

    def hien_thi(self):
        temp = self.head
        if not temp:
            print("Danh sách rỗng!")
            return

        while temp:
            temp.data.hien_thi()
            temp = temp.next

    def xoa_dau(self):
        if not self.head:
            print("Danh sách rỗng!")
            return
        self.head = self.head.next
        print("Đã xóa đầu!")

    def xoa_cuoi(self):
        if not self.head:
            print("Danh sách rỗng!")
            return

        if not self.head.next:
            self.head = None
            print("Đã xóa cuối!")
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        print("Đã xóa cuối!")

    def xoa_giua(self, mssv):
        if not self.head:
            print("Danh sách rỗng!")
            return

        if self.head.data.mssv == mssv:
            self.head = self.head.next
            print("Đã xóa!")
            return

        temp = self.head
        while temp.next:
            if temp.next.data.mssv == mssv:
                temp.next = temp.next.next
                print("Đã xóa!")
                return
            temp = temp.next

        print("Không tìm thấy!")


# ===== MAIN =====
dslk = DSLK()       
dslk_goc = DSLK()

n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):
    print(f"Sinh viên {i+1}:")
    mssv = input("Nhập MSSV: ")
    hoten = input("Họ và tên: ")
    lop = input("Lớp: ")
    diem = float(input("Điểm: "))

    sv = SinhVien(mssv, hoten, lop, diem)
    sv_copy = SinhVien(mssv, hoten, lop, diem)  

    dslk.them_cuoi(sv)
    dslk_goc.them_cuoi(sv_copy)


while True:
    print("===== MENU =====")
    print("1. Hiển thị danh sách ban đầu")
    print("2. Hiển thị danh sách hiện tại")
    print("3. Xóa đầu")
    print("4. Xóa cuối")
    print("5. Xóa theo MSSV")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        print("Danh sách ban đầu:")
        dslk_goc.hien_thi()

    elif chon == "2":
        print("Danh sách hiện tại:")
        dslk.hien_thi()

    elif chon == "3":
        dslk.xoa_dau()
        dslk.hien_thi()

    elif chon == "4":
        dslk.xoa_cuoi()
        dslk.hien_thi()

    elif chon == "5":
        ms = input("Nhập MSSV bạn muốn xóa: ")
        dslk.xoa_giua(ms)
        dslk.hien_thi()

    elif chon == "0":
        break