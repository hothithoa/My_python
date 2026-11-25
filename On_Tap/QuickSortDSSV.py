# ====== CLASS ======
class SinhVien:
    def __init__(self, ms, ten, ns, diem):
        self.ms = ms
        self.ten = ten
        self.ns = ns
        self.diem = diem

    def __str__(self):
        return f"{self.ms} - {self.ten} - {self.ns} - {self.diem:.2f}"


def partition(arr, l, r):
    pi = arr[l]
    i = l + 1
    j = r

    while True:
        while i <= j and arr[j].diem >= pi.diem:
            j -= 1
        while i <= j and arr[i].diem <= pi.diem:
            i += 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quickSort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        quickSort(arr, l, pi - 1)
        quickSort(arr, pi + 1, r)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, sv):
        node = Node(sv)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

def bubble_sort_linkedlist(ll):
    if not ll.head or not ll.head.next:
        return

    while True:
        swapped = False
        prev = None
        curr = ll.head

        while curr and curr.next:
            if curr.data.diem > curr.next.data.diem:
                swapped = True

                nxt = curr.next


                curr.next = nxt.next
                nxt.next = curr

                if prev is None:
                    ll.head = nxt
                else:
                    prev.next = nxt

                prev = nxt
            else:
                prev = curr
                curr = curr.next

        if not swapped:
            break

def nhap_danh_sach():
    n = int(input("Nhập số lượng sinh viên: "))
    arr = []
    ll = LinkedList()

    for i in range(n):
        print(f"\nSinh viên {i+1}:")
        ms = input("Mã số: ")
        ten = input("Tên: ")
        ns = input("Năm sinh: ")
        diem = float(input("Điểm: "))

        sv = SinhVien(ms, ten, ns, diem)
        arr.append(sv)
        ll.append(sv)

    return arr, ll

def menu():
    print("\n===== MENU =====")
    print("1. Sắp xếp ARRAY (QuickSort)")
    print("2. Sắp xếp LINKED LIST (Swap Node)")
    print("3. Nhập lại")
    print("0. Thoát")
    return int(input("Chọn: "))

def main():
    arr, ll = nhap_danh_sach()

    while True:
        print("\n--- ARRAY ---")
        for sv in arr:
            print(sv)

        print("\n--- LINKED LIST ---")
        ll.display()

        chon = menu()

        if chon == 0:
            print("Thoát!")
            break

        elif chon == 3:
            arr, ll = nhap_danh_sach()

        elif chon == 1:
            temp = arr.copy()
            quickSort(temp, 0, len(temp) - 1)
            print("\n--- ARRAY SAU SẮP XẾP ---")
            for sv in temp:
                print(sv)

        elif chon == 2:
            bubble_sort_linkedlist(ll)
            print("\n--- LINKED LIST SAU SẮP XẾP ---")
            ll.display()

        else:
            print("Sai lựa chọn!")


main()