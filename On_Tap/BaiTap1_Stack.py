class SinhVien:
    def __init__(self, mssv, ten, lop):
        self.mssv = mssv
        self.ten = ten
        self.lop = lop


class StackArray:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.max = size

    def push(self, sv):
        if self.top == self.max - 1:
            print("Stack đầy!")
        else:
            self.top += 1
            self.stack[self.top] = sv

    def pop(self):
        if self.top == -1:
            print("Stack rỗng!")
        else:
            self.top -= 1

    def display(self):
        for i in range(self.top, -1, -1):
            sv = self.stack[i]
            print(sv.mssv, ":", sv.ten, ":", sv.lop)



n = int(input("Nhập số SV: "))
stack = StackArray(n)

for i in range(n):
    print(f"Sinh viên {i+1}")
    mssv = input("MSSV: ")
    ten = input("Họ tên: ")
    lop = input("Lớp: ")
    stack.push(SinhVien(mssv, ten, lop))

print("Stack (mảng):")
stack.display()