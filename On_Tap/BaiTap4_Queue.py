#bai 4
class Node:
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None  


    def enqueue(self, ma, ten, diem):
        new_node = Node(ma, ten, diem)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def display(self):
        temp = self.front
        print("\nDanh sách sinh viên (theo thứ tự nhập):")
        while temp:
            print(f"Mã: {temp.ma}, Tên: {temp.ten}, Điểm: {temp.diem}")
            temp = temp.next


queue = Queue()


n = int(input("Nhập số lượng sinh viên: "))


for i in range(n):
    print(f"\nSinh viên {i+1}:")
    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))
    queue.enqueue(ma, ten, diem)


queue.display()