balance = 1000000  # số dư ban đầu

while True:
    print("\n===== ATM MENU =====")
    print("1. Xem số dư")
    print("2. Rút tiền")
    print("3. Nạp tiền")
    print("4. Thoát")

    choice = int(input("Chọn chức năng (1-4): "))

    if choice == 1:
        print("Số dư hiện tại:", balance, "VNĐ")

    elif choice == 2:
        money = int(input("Nhập số tiền muốn rút: "))
        if money <= balance:
            balance -= money
            print("Rút tiền thành công!")
        else:
            print("Số dư không đủ!")

    elif choice == 3:
        money = int(input("Nhập số tiền muốn nạp: "))
        balance += money
        print("Nạp tiền thành công!")

    elif choice == 4:
        print("Cảm ơn bạn đã sử dụng ATM!")
        break

    else:
        print("Lựa chọn không hợp lệ!")