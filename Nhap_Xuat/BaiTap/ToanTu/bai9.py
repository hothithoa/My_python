ten_sp = input("Nhập tên sản phẩm: ")
gia = float(input("Nhập giá sản phẩm: "))
thue = float(input("Nhập thuế (%): "))

gia_sau_thue = gia * (1 + thue / 100)

print("Tên sản phẩm:", ten_sp)
print("Giá sau thuế:", gia_sau_thue)