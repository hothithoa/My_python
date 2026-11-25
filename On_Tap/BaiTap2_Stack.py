#Bai 2
class Node:
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, ma, ten, diem):
        new_node = Node(ma, ten, diem)
        new_node.next = self.top
        self.top = new_node


    def display(self):
        temp = self.top
        print("\nDanh sách sinh viên (từ trên xuống):")
        while temp:
            print(f"Mã: {temp.ma}, Tên: {temp.ten}, Điểm: {temp.diem}")
            temp = temp.next


stack = Stack()


n = int(input("Nhập số lượng sinh viên: "))


for i in range(n):
    print(f"\nSinh viên {i+1}:")
    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))
    stack.push(ma, ten, diem)


stack.display()