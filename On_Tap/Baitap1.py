import copy

ds = nhap_danh_sach()

print("\nDanh sach ban dau:")
xuat(ds)

# Selection sort tăng
ds1 = copy.deepcopy(ds)
selection_sort_tang(ds1)
print("Selection Sort tang dan:")
xuat(ds1)

# Selection sort giảm 
ds2 = copy.deepcopy(ds)
selection_sort_giam(ds2)
print("Selection Sort giam dan:")
xuat(ds2)

# Insertion sort tăng
ds3 = copy.deepcopy(ds)
insertion_sort_tang(ds3)
print("Insertion Sort tang dan:")
xuat(ds3)

# Insertion sort giảm
ds4 = copy.deepcopy(ds)
insertion_sort_giam(ds4)
print("Insertion Sort giam dan:")
xuat(ds4)