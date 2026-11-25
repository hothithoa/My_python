class SinhVien:
    def __init__(self, ma, ten, ns, diem):
        self.ma = ma
        self.ten = ten
        self.ns = ns
        self.diem = diem

    def __str__(self):
        return f"{self.ma} | {self.ten} | {self.ns} | {self.diem}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, sv):
        new_node = Node(sv)
        if not self.head:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node

    def display(self):
        p = self.head
        while p:
            print(p.data)
            p = p.next


def bubble_sort_tang(ll):
    if not ll.head:
        return

    end = None
    while end != ll.head:
        p = ll.head
        swapped = False
        while p.next != end:
            if p.data.diem > p.next.data.diem:
                p.data, p.next.data = p.next.data, p.data
                swapped = True
            p = p.next
        if not swapped:   
            break
        end = p


def bubble_sort_giam(ll):
    if not ll.head:
        return

    end = None
    while end != ll.head:
        p = ll.head
        swapped = False
        while p.next != end:
            if p.data.diem < p.next.data.diem:
                p.data, p.next.data = p.next.data, p.data
                swapped = True
            p = p.next
        if not swapped:
            break
        end = p


ll = LinkedList()

n = int(input("Nhập số sinh viên: "))
for i in range(n):
    print(f"\nSinh viên {i+1}:")
    ma = input("Mã: ")
    ten = input("Tên: ")
    ns = input("Ngày sinh: ")
    diem = float(input("Điểm: "))
    ll.append(SinhVien(ma, ten, ns, diem))

print("\nDanh sách ban đầu:")
ll.display()

bubble_sort_tang(ll)
print("\nSau khi sắp xếp TĂNG theo điểm:")
ll.display()

bubble_sort_giam(ll)
print("\nSau khi sắp xếp GIẢM theo điểm:")
ll.display()