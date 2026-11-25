import array as arr
ds = arr.array('i',[])
n = int(input("Nhập số lượng cần thêm vào danh sách: "))
for i in range(n):
    sn = int(input(f"Nhập số thứ {i+ 1}: "))
    ds.append(sn)
tong = 0
for j in range(len(ds)):
    tong += ds[j]
print(f"Danh sách: {ds}")
print(f"Tổng của các số nguyên trong dãy là: {tong}")
tong_so_chan = 0
for g in range(len(ds)):
    if ds[g] % 2 == 0:
        tong_so_chan += ds[g]
print(f"Tổng các số chẵn trong dãy là: {tong_so_chan}")
tong_so_chan_tai_vi_tri_le = 0
for k in range(len(ds)):
    if ds[k] % 2 == 0 and k % 2 != 0:
        tong_so_chan_tai_vi_tri_le += ds[k] 
print(f"Tổng các số chẵn tại vị trí lẻ là: {tong_so_chan_tai_vi_tri_le}")
